from PIL import Image, ImageDraw,ImageFont
import numpy as np

#可以選字型
font_type="C:\\Windows\\Fonts\\mingliu.ttc"
font_size=100
font = ImageFont.truetype(font_type,font_size,encoding='utf-8')

width = 920
height = 100
color = (255,255,255)
fill = (255,0,0)
text = "高山一実我老婆"

def generate_Picture(width, height, color, text, fill):
    #color內可調背景框顏色
    frame = Image.new('RGB',(width,height), color = color)

    draw = ImageDraw.Draw(frame)
    #前面數字對為文字開始處 text內輸入字型 fill內填入顏色
    draw.text((100,0),text=text,font=font,fill=fill)

    #把一格一格截出來的影格放到marquee的資料夾
    box=[0,0,100,100]
    for i in range(int(width/10)):
        if 100+10*i < width:
            box=[0+10*i,0,100+10*i,100]
            region = frame.crop(box)
            region.save('marquee/'+str(i)+'.png')

generate_Picture(width,height,color,text,fill)

#range 裏頭為可行的圖片編號
imagelist=[]
for i in range(int(width/10)):
    if 100+10*i < width:
        imagelist.append(Image.open('marquee/'+str(i)+'.png'))

#合併影格成gif duration可以調影格停留的時間，單位為ms
imagelist[0].save('marquee/out.gif', format='GIF',save_all=True, append_images=imagelist[1:], duration=40,optimize=True, loop=0)