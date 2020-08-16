# text_to_marquee
## 如何使用 
1.下載python 3.8 </br>
2.把程式跟requirements.txt放到同一目的地 </br>
3.打開command line </br>
4.cd 到程式所在的資料夾，輸入 </br>
```
pip install -r requirements.txt 
```
5.用編輯器打開程式 </br>
</br>
</br>
## 調整參數
#### 字型部分可以調整，路徑為絕對路徑，選擇時盡量選擇支援utf-8的字型
```python
#可以選字型
font_type="C:\\Windows\\Fonts\\mingliu.ttc"
#字體大小
font_size=100
font = ImageFont.truetype(font_type,font_size,encoding='utf-8')
```
#### 其餘參數
width, height為背景box的寬、高 </br>
color為背景box的顏色，fill為字體的顏色，兩者皆為RGB編碼 </br>
text中可填入跑馬燈的文字
```python
width = 920
height = 100
color = (255,255,255)
fill = (255,0,0)
text = "高山一実我老婆"
```
## 使用
在放程式的資料夾新增一個叫做marquee的資料夾程式碼，運行程式 </br>
出來的結果會像這樣 </br>
![1](https://github.com/YYLIZH/text_to_marquee/blob/master/marquee.jpg "輸出範例")
會出現一堆圖片以及做好的gif檔 </br>
原理是用這堆圖片合出gif檔，可以檢查一下gif取值是否滿意，若不滿意可以在range裡改成想要的圖片編號
```python
#range 裏頭為可行的圖片編號
imagelist=[]
for i in range(int(width/10)):
    imagelist.append(Image.open('marquee/'+str(i)+'.png'))

#合併影格成gif duration可以調影格停留的時間，單位為ms
imagelist[0].save('marquee/out.gif', format='GIF',save_all=True, append_images=imagelist[1:], duration=40,optimize=True, loop=0)
```
Ex.range(81):第0到第80張 range(1,81)：第1到第80張 </br>
除此之外，save裡duration可以調整每個影格出線的秒數，單位是毫秒
## 結果
![gif](https://github.com/YYLIZH/text_to_marquee/blob/master/beauty.gif "輸出結果)
