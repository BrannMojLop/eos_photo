from wand.image import Image
from wand.drawing import Drawing
import pandas as pd
import time

# Iniciando ejecucion
inicio = time.time()
print("Starting program...")

# Leer dataset
df = pd.read_excel('./docs/data.xlsx')

# Iteracion y edicion de imagenes
for i in range(len(df)):

    # Ajuste de textos
    letters = 34
    initial_text = 1000
    letter_spacing = 30

    # Tipo de texto
    draw = Drawing()
    draw.font_size = 48
    draw.font_family = 'Arial'
    draw.color = '#b5b5b5'

    code = df.iloc[i]['code']
    desc = df.iloc[i]['description'] + " | " + df.iloc[i]['measure']

    img = Image(
        filename='./img_original/' + code + '.jpg')

    if len(desc) > letters:
        extra = len(desc) - letters
        initial_text = initial_text - (extra * letter_spacing)

    if len(desc) < letters:
        subtract = len(desc) - letters
        initial_text = initial_text - (subtract * letter_spacing)

    draw.text(initial_text, 1950, desc)
    draw.text(50, 1950, code)
    draw(img)
    draw.clear()
    img.save(filename='./img_details/' + code + '.jpg')
    img.close()

    print("\n========" + code + "========")

print("\n====== Imagenes procesadas ========")
print(len(df))
print("======== Tiempo de ejecución ========")
fin = time.time()
print(round(fin-inicio, 2))
print("Finished...")
