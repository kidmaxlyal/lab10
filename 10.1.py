from PIL import Image

img = Image.open("Гонка.jpg")

crop_image = img.crop((400, 40, 700, 400))
crop_image.save("crop_image.png")

crop_image.show()
