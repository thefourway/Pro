from PIL import Image,ImageDraw,ImageFont
#get an image

Q000 = Image.open('E:\\0.jpg')

#Q000.show()

draw = ImageDraw.Draw(Q000)

myfont = ImageFont.truetype('C:/windows/fonts/Arial.ttf', size=500)

width, height = Q000.size

draw = ImageDraw.Draw(Q000)

draw.text((width-500,0),'0000',fill='#ff0000',font =myfont)


Q000.show()
#Q000.save('result.jpg','jpeg')





























'''
from PIL import Image, ImageDraw, ImageFont
# get an image
base = Image.open('Pillow/Tests/images/lena.png').convert('RGBA')

# make a blank image for the text, initialized to transparent text color
txt = Image.new('RGBA', base.size, (255,255,255,0))

# get a font
fnt = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 40)
# get a drawing context
d = ImageDraw.Draw(txt)

# draw text, half opacity
d.text((10,10), "Hello", font=fnt, fill=(255,255,255,128))
# draw text, full opacity
d.text((10,60), "World", font=fnt, fill=(255,255,255,255))

out = Image.alpha_composite(base, txt)

out.show()
'''
