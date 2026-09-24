from PIL import Image, ImageDraw, ImageFont

# --- Agile vs tradicional summary ---
img = Image.new('RGB', (1200, 420), 'white')
d = ImageDraw.Draw(img)

try:
    title_font = ImageFont.truetype('DejaVuSans-Bold.ttf', 30)
    head_font = ImageFont.truetype('DejaVuSans-Bold.ttf', 22)
    body_font = ImageFont.truetype('DejaVuSans.ttf', 18)
except Exception:
    title_font = ImageFont.load_default()
    head_font = ImageFont.load_default()
    body_font = ImageFont.load_default()

# Colors
blue = (219, 234, 254)
green = (220, 252, 231)
text = (17, 24, 39)
edge = (30, 41, 59)

# Layout
left_x, right_x = 80, 620
width = 420
box_y = 90
box_h = 260

# Title
bbox = d.textbbox((0, 0), 'Modelo ágil frente a modelo tradicional', font=title_font)
text_x = (1200 - (bbox[2] - bbox[0])) / 2
d.text((text_x, 18), 'Modelo ágil frente a modelo tradicional', font=title_font, fill=text)

# Boxes
for x, fill, title, items in [
    (left_x, blue, 'Tradicional', ['Planificación previa', 'Requisitos casi fijos', 'Cambios difíciles', 'Control documental fuerte', 'Entrega al final']),
    (right_x, green, 'Ágil', ['Planificación flexible', 'Requisitos evolucionan', 'Cambios frecuentes', 'Colaboración continua', 'Entrega incremental'])
]:
    d.rounded_rectangle((x, box_y, x + width, box_y + box_h), radius=18, outline=edge, width=2, fill=fill)
    d.text((x + 20, box_y + 18), title, font=head_font, fill=text)
    y = box_y + 70
    for item in items:
        d.text((x + 26, y), '• ' + item, font=body_font, fill=text)
        y += 34

# Center arrow
mid = 520
arrow_y = 210
for y in [185, 210, 235]:
    d.line((520, y, 620, y), fill=edge, width=4)

d.polygon([(620, 210), (600, 200), (600, 220)], fill=edge)
# Smaller arrow line to indicate difference

d.text((520, 145), 'comparación', font=body_font, fill=text)

out = r"C:\Users\pacoa\OneDrive - Conselleria d'Educació\ceed2627\pi2\git\pi2_2627\UD2\images\agil-vs-tradicional.png"
img.save(out)
print(out)
