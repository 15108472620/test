from PIL import Image
path='image/timg.jpg'
image=Image.open(path)
print(image)
print(image.size,image.format)