import gradio as gr
import skimage
import fastai
from fastai.vision.all import *
# from torchvision.models.utils import load_state_dict_from_url


learn = load_learner('model.pkl')

categories = ('Curly', 'Straight')

def predict(img):
    img = PILImage.create(img)
    pred,pred_idx,probs = learn.predict(img)
    return dict(zip(categories, map(float,probs)))


print(learn.predict('test3.jpg')[0])



# Logic for sending products depending on curly or straight
if learn.predict('test3.jpg')[0] == 'curly hair':
    pass
    # pass through curly hair products
elif learn.predict('test3.jpg')[0] == 'straight hair':
    pass
    # pass through straight hair products