# AUTOGENERATED! DO NOT EDIT! File to edit: ../app.ipynb.

# %% auto 0
__all__ = ['learn', 'categories', 'image', 'label', 'examples', 'intf', 'classify_image']

# %% ../app.ipynb 1
from fastai.vision.all import *
import gradio as gr

# %% ../app.ipynb 2
learn = load_learner('model.pkl')

# %% ../app.ipynb 6
categories = ('didgeridoo','tambourine','xylophone','acordian','alphorn','bagpipes','banjo','bongo drum','casaba','castanets','clarinet','clavichord','concertina','drums','dulcimer','flute','guiro','guitar','harmonica','harp','marakas','ocarina','piano','saxaphone','sitar','steel drum','trombone','trumpet','tuba','violin')
def classify_image(img):
    pred,idx,probs = learn.predict(img)
    return dict(zip(categories,map(float,probs)))

# %% ../app.ipynb 8
image = gr.inputs.Image(shape=(224,224))
label=gr.outputs.Label()
examples=['banjo.jpg']
intf = gr.Interface(fn=classify_image,inputs=image,outputs=label,examples=examples)
intf.launch(inline=False)
