from PIL import Image
from os import system
import pyautogui, sys
import time
import requests
import numpy as np

SIZE = 150

class mylist:
    before = []
    idx = 0
    size = 0

class Color:
    white = [255,255,255]
    black = [0,0,0]
    grey = [193,193,193]
    dark_grey = [76,76,76]
    red = [239,19,11]
    dark_red = [116,11,7]
    orange = [255,113,0]
    dark_orange = [194,56,0]
    yellow = [255,228,0]
    dark_yellow = [232,162,0]
    green = [0,204,0]
    dark_green = [0,85,16]
    blue = [0,178,255]
    dark_blue = [0,86,158]
    big_blue = [35,31,211]
    dark_big_blue = [14,8,101]
    purple = [163,0,186]
    dark_purple = [85,0,105]
    pink = [211,124,170]
    dark_pink = [167,85,116]
    brown = [160,82,45]
    dark_brown = [99,48,13]
    color_list = [white,black,grey,dark_grey,red,dark_red,orange,dark_orange,yellow,dark_yellow,green,dark_green,blue,dark_blue,big_blue,dark_big_blue,purple,dark_purple,pink,dark_pink,brown,dark_brown]
    color_list_name = ["white","black","grey","dark_grey","red","dark_red","orange","dark_orange","yellow","dark_yellow","green","dark_green","blue","dark_blue","big_blue","dark_big_blue","purple","dark_purple","pink","dark_pink","brown","dark_brown"]


class Kolor:
    white = 765
    black = 0
    grey = 579
    dark_grey = 228
    red = 269
    dark_red = 134
    orange = 388
    dark_orange = 250
    yellow = 483
    dark_yellow = 394
    green = 204
    dark_green = 101
    blue = 433
    dark_blue = 244
    big_blue = 277
    dark_big_blue = 123
    purple = 349
    dark_purple = 190
    pink = 505
    dark_pink = 368
    brown = 287
    dark_brown = 160
    color_list = [white,black,grey,dark_grey,red,dark_red,orange,dark_orange,yellow,dark_yellow,green,dark_green,blue,dark_blue,big_blue,dark_big_blue,purple,dark_purple,pink,dark_pink,brown,dark_brown]
    color_list_name = ["white","black","grey","dark_grey","red","dark_red","orange","dark_orange","yellow","dark_yellow","green","dark_green","blue","dark_blue","big_blue","dark_big_blue","purple","dark_purple","pink","dark_pink","brown","dark_brown"]


def closest(colors,color):
    colors = np.array(colors)
    color = np.array(color)
    distances = np.sqrt(np.sum((colors-color)**2,axis=1))
    index_of_smallest = np.where(distances==np.amin(distances))
    smallest_distance = colors[index_of_smallest]
    s_color = str(smallest_distance).replace("[","").replace("]","").replace("  "," ")
    s_color = s_color.split(" ")
    s_list = []
    for i in range(len(s_color)):
        if s_color[i] != "":
            s_list.append(s_color[i])
    res = int(s_list[0]) + int(s_list[1]) + int(s_list[2])
    return res
    
def download_and_resize_pic(pic,m):
    img_data = requests.get(pic).content
    with open('image_name.jpg', 'wb') as handler:
        handler.write(img_data)
    image = Image.open('image_name.jpg')
    x , y = image.size
    if x > y:
        res = x /SIZE
    else:
        res = y/SIZE
    m.size = int(x/res)
    
    if int(y/res) < 145 and int(x/res) < 145 or int(x/res) < 145 and int(y/res) < 145:
        new_image = image.resize((int(x/res),int(y/res)))
    else:
        new_image = image.resize((int(int(x/res)*0.75),int(int(y/res)*0.75)))
        m.size = int(m.size*0.75)
    new_image.convert('RGB').save('picture.jpg')

def closest_number_from_list(num,l):
    list_of_num = l
    list_of_num.sort()
    n = num
    idx = 0
    num_list = []

    for i in range(len(list_of_num)):
        if n < l[i]:
            num_list.append(list_of_num[i])
            num_list.append(list_of_num[i-1])
            idx = idx + 1
            break
    if idx == 0:
        return(l[-1])
    else:
        if n - num_list[0] >= n - num_list[1]:
            return(num_list[0])
        else:
            return(num_list[1])

def click_on_colour(num,pic_x,pic_y,klick):
    X = 477
    Y = 274
    c = Kolor()
    idx_x = 0
    idx_y = 0
    
    for i in range(len(c.color_list)):
        if c.color_list[i] == num:
            if i % 2 != 0:
                idx_y = 944
                idx_x = 586 + int(23/2) * (i)
                if klick == 1:
                    time.sleep(0.5)
                    pyautogui.click(x=X+pic_x ,y=Y+pic_y)
                
                    pyautogui.click(x=idx_x, y=idx_y)
                elif klick == 2:
                    pyautogui.PAUSE = 0.005
                    pyautogui.click(x=idx_x, y=idx_y)
                    
                else:
                    pyautogui.PAUSE = 0.005
                    pyautogui.click(x=X+pic_x ,y=Y+pic_y)
                
            else:
                idx_y = 915
                idx_x = 586 + (int(23/2) * (i))
                if klick == 1:
                    time.sleep(0.5)
                    pyautogui.click(x=X+pic_x ,y=Y+pic_y)
                    pyautogui.click(x=idx_x, y=idx_y)
                elif klick == 2:
                    pyautogui.PAUSE = 0.005      
                    pyautogui.click(x=idx_x, y=idx_y)
                
                else:
                    pyautogui.PAUSE = 0.005 
                    pyautogui.click(x=X+pic_x ,y=Y+pic_y)
            
            break
    
def draw_pic(m):
    pyautogui.click(x=1075 ,y=930)
    pic_pix = get_pixel()
    idx_x = 0
    idx_y = 0
    
    pic_pix = get_pixel()
    one_pic = list(dict.fromkeys(pic_pix))
    count_l = []
    idx = 0
    change_c = 0
    for i in range(len(one_pic)):
        count_l.append(pic_pix.count(one_pic[i]))
    count_l, one_pic = zip(*sorted(zip(count_l, one_pic)))
    once = 0
    click_on_colour(one_pic[change_c],0,0,2)

    for j in range(len(one_pic)):
        for i in range(len(pic_pix)):
            if once == 0:
                click_on_colour(one_pic[change_c],idx_x,idx_y,1)
                once = 1 
            if i % m.size == 0:
                idx_y = idx_y + 5
                idx_x = 0
            idx_x = idx_x + 5
            if pic_pix[i] != 765:
                if pic_pix[i] == one_pic[change_c]:
                    click_on_colour(one_pic[change_c],idx_x,idx_y,0)
        idx_x = 0
        idx_y = 0
        once = 0
        change_c = change_c + 1
        

def get_pixel():
    color = Color()
    new_list = []
    final_list = []
    im = Image.open('picture.jpg', 'r')
    width, height = im.size
    pixel_values = list(im.getdata())
    
    for i in range(len(pixel_values)):
        final_list.append(int(closest(color.color_list,pixel_values[i])))
    return(final_list)

m = mylist()
try:
    pic = input("Le truc a dessiner: ")
    download_and_resize_pic(pic,m)
    get_pixel()
    time.sleep(5)
    draw_pic(m)
except:
    pic = "https://files.structurae.net/files/covers/doa127.jpg"
    download_and_resize_pic(pic,m)
    get_pixel()
    time.sleep(5)
    draw_pic(m)

