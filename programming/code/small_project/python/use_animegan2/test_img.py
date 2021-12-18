from PIL import Image
import torch
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# model = torch.hub.load('bryandlee/animegan2-pytorch:main', 'generator', pretrained='celeba_distill')
# model = torch.hub.load('bryandlee/animegan2-pytorch:main', 'generator', pretrained='face_paint_512_v1')
model = torch.hub.load('bryandlee/animegan2-pytorch:main', 'generator', pretrained='face_paint_512_v2')
# model = torch.hub.load('bryandlee/animegan2-pytorch:main', 'generator', pretrained='paprika')

face2paint = torch.hub.load('bryandlee/animegan2-pytorch:main', 'face2paint', size=512)

img = Image.open('img.jpg').convert('RGB')

out = face2paint(model, img)
out.show()
out.save()
