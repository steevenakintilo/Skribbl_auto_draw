from PIL import Image
from os import system
import pyautogui, sys
import time
import requests
import numpy as np
import keyboard
from typing import Dict, Callable
import math

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

Colour = tuple[int, int, int]

tuple_colours: dict[str, Colour] = {'white': (255, 255, 255), 'black': (0, 0, 0), 'grey': (193, 193, 193), 'dark_grey': (76, 76, 76), 'red': (239, 19, 11), 'dark_red': (116, 11, 7), 'orange': (255, 113, 0), 'dark_orange': (194, 56, 0), 'yellow': (255, 228, 0), 'dark_yellow': (232, 162, 0), 'green': (0, 204, 0), 'dark_green': (0, 85, 16), 'blue': (0, 178, 255), 'dark_blue': (0, 86, 158), 'big_blue': (35, 31, 211), 'dark_big_blue': (14, 8, 101), 'purple': (163, 0, 186), 'dark_purple': (85, 0, 105), 'pink': (211, 124, 170), 'dark_pink': (167, 85, 116), 'brown': (160, 82, 45), 'dark_brown': (99, 48, 13)}

def check_key_quit(key):
    if keyboard.is_pressed(key):
        sys.exit()

def print_file(path):
    f = open(path, 'r')
    content = f.read()
    return(content)
    f.close()

def write_into_file(path,x):
    f = open(path, "w")
    f.write(str(x))
    f.close

def closest(dict_colors, color):
    dict_colors = np.array(dict_colors)
    color = np.array(color)
    distances = np.array([math.dist(c, color) for c in dict_colors])  # Calculate distances using math.dist
    index_of_smallest = np.where(distances == np.amin(distances))
    smallest_distance = dict_colors[index_of_smallest]
    smallest_distance = smallest_distance[0]  # Get the first color if multiple smallest distances
    smallest_distance = smallest_distance[:3]  # Keep only the first 3 elements (R, G, B)
    s = sum(smallest_distance)
    return s

def closest(dict_colors, color):
    colors = np.array(list(dict_colors.values()))
    color = np.array(color)
    distances = np.array([math.dist(c, color) for c in colors])  # Calculate distances using math.dist
    index_of_smallest = np.where(distances == np.amin(distances))
    closest_color_key = list(dict_colors.keys())[index_of_smallest[0][0]]  # Get the key for the closest color
    closest_color = dict_colors[closest_color_key]
    closest_color = closest_color[:3]  # Keep only the first 3 elements (R, G, B)
    s = sum(closest_color)
    return s

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
    check_key_quit("x")
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
                    pyautogui.click(x=X+pic_x+20 ,y=Y+pic_y)
                
                    pyautogui.click(x=idx_x - 15, y=idx_y)
                elif klick == 2:
                    pyautogui.PAUSE = 0.005
                    pyautogui.click(x=idx_x+20, y=idx_y+30)
                    
                else:
                    pyautogui.PAUSE = 0.005
                    pyautogui.click(x=X+pic_x+20 ,y=Y+pic_y+30)
                
            else:
                idx_y = 915
                idx_x = 586 + (int(23/2) * (i))
                if klick == 1:
                    time.sleep(0.5)
                    pyautogui.click(x=X+pic_x+20 ,y=Y+pic_y)
                    pyautogui.click(x=idx_x - 15, y=idx_y)
                elif klick == 2:
                    pyautogui.PAUSE = 0.005      
                    pyautogui.click(x=idx_x+20, y=idx_y+30)
                
                else:
                    pyautogui.PAUSE = 0.005 
                    pyautogui.click(x=X+pic_x+20 ,y=Y+pic_y+30)
            
            break
    
def draw_pic(m):
    #pyautogui.click(x=1075 ,y=930)

    pic_pix = get_pixel()
    print("colour ")
    a_colour = print_colour_from_pic()
    a_unique_colour = list(dict.fromkeys(a_colour))

    # Sort the unique colors by the number of their occurrences
    sorted_colors = sorted(a_unique_colour, key=lambda x: a_colour.count(x), reverse=True)

    for col in sorted_colors:
        count = a_colour.count(col)
        print("col:", col, count)

    #print(a)
    idx_x = 0
    idx_y = 0
    
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

def better_closest(c: Colour) -> str:
    return min(tuple_colours, key=lambda k: math.dist(c, tuple_colours[k]))

def adjust_pixels(img: Image.Image) -> list[str]:
    pixels: list[Colour] = list(img.getdata())  # type: ignore
    print(list(img.getdata()))
    write_into_file("ok.txt",list(img.getdata()))
    return [better_closest(p) for p in pixels]

def get_pixel():
    
    with Image.open("picture.jpg") as img:
        new_pixel_names: list[str] = adjust_pixels(img)
    
    final_list = []
    for i in range(len(new_pixel_names)):
        final_list.append(sum(tuple_colours[new_pixel_names[i]]))

    return(final_list)



def print_colour_from_pic():
    with Image.open("picture.jpg") as img:
        new_pixel_names: list[str] = adjust_pixels(img)
    return (new_pixel_names)

m = mylist()
try:
    #pic = input("pic to draw: ")
    pic = "https://cdn.vox-cdn.com/thumbor/sW5h16et1R3au8ZLVjkcAbcXNi8=/0x0:3151x2048/2000x1333/filters:focal(1575x1024:1576x1025)/cdn.vox-cdn.com/uploads/chorus_asset/file/15844974/netflixlogo.0.0.1466448626.png"
    #pic = "https://static.wikia.nocookie.net/characters/images/e/e8/Majin_Buu.png/revision/latest?cb=20221227172116"
    #"pic = "https://skribbl.io/img/logo.gif"
    #pic = "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Facebook_logo_%28square%29.png/800px-Facebook_logo_%28square%29.png"
    download_and_resize_pic(pic,m)
    #get_pixel()
    print("prout")
    time.sleep(5)
    draw_pic(m)
except:
    pic = "https://files.structurae.net/files/covers/doa127.jpg"
    download_and_resize_pic(pic,m)
    #get_pixel()
    time.sleep(5)
    draw_pic(m)

