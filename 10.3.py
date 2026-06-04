from PIL import Image, ImageDraw, ImageFont

o = {"Новый год": "Открытки/Новый год.jpg",
            "День рождения": "Открытки/День рождения.jpg",
            "День победы": "Открытки/День победы.jpg"}

p = input("Праздник? ")
n = input("Имя? ")

if p in o:
    img = Image.open(o[p])
    draw = ImageDraw.Draw(img)
    text = f"{n}, поздравляем!"
    font = ImageFont.truetype("arial.ttf", 50)
    draw.text((img.width // 2 - 50, 25), text, font = font, fill = "black")
    draw.text((img.width // 2 - 52, 25), text, font = font, fill="white")
    img.save("pozdravlenie.png")
    img.show()
else:
    print("Нет такого")
