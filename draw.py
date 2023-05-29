from PIL import Image
from os import system
import pyautogui, sys
import time
import requests
import numpy as np
import keyboard
from typing import Dict, Callable
import math
from colormath.color_diff import delta_e_cie1976 as cie76

SIZE = 150

class mylist:
    before = []
    idx = 0
    size = 0

    
Colour = tuple[int, int, int]


tuple_colours: dict[str, Colour] = {'white': (255, 255, 255), 'black': (0, 0, 0), 'grey': (193, 193, 193), 'dark_grey': (76, 76, 76), 'red': (239, 19, 11), 'dark_red': (116, 11, 7), 'orange': (255, 113, 0), 'dark_orange': (194, 56, 0), 'yellow': (255, 228, 0), 'dark_yellow': (232, 162, 0), 'green': (0, 204, 0), 'dark_green': (0, 85, 16), 'light_green': (255,145,255) , 'light_dark_green': (70,25,255), 'blue': (0, 178, 255), 'dark_blue': (0, 86, 158), 'big_blue': (35, 31, 211), 'dark_big_blue': (14, 8, 101), 'purple': (163, 0, 186), 'dark_purple': (85, 0, 105), 'pink': (211, 124, 170), 'dark_pink': (167, 85, 116), 'brown': (160, 82, 45), 'dark_brown': (99, 48, 13)}

Pos = tuple[int,int]

colours_pos: dict[str,Pos] = {'white': (575, 918), 
                              'black': (575, 942), 
                              'grey': (600, 918), 
                              'dark_grey': (600, 942), 
                              'red': (625,918), 
                              'dark_red': (625,942), 
                              'orange': (650,918), 
                              'dark_orange': (650,942), 
                              'yellow': (675,918), 
                              'dark_yellow': (675,942), 
                              'green': (700,918), 
                              'dark_green': (700,942), 
                              'light_green': (725,918), 
                              'light_dark_green': (725,942), 
                              'blue': (750, 918), 
                              'dark_blue': (750,942), 
                              'big_blue': (775, 918), 
                              'dark_big_blue': (775,942), 
                              'purple': (800, 918), 
                              'dark_purple': (800,942), 
                              'pink': (825,918), 
                              'dark_pink': (825,942), 
                              'brown': (850,918), 
                              'dark_brown': (850,942)}

def check_key_quit(key):
    if keyboard.is_pressed(key):
        sys.exit()

def download_and_resize_pic(pic,m):
    img_data = requests.get(pic).content
    with open('image_name.jpg', 'wb') as handler:
        handler.write(img_data)
    image = Image.open('image_name.jpg')
    x , y = image.size
    SIZE_X = 150
    SIZE_Y = 150
    res_x = 0
    res_y = 0
    factor = 0
    short_pic = False
    if x > SIZE_X or y > SIZE_Y:
        if x > y:
            factor = x / SIZE_X
        else:
            factor = y / SIZE_Y
        res_x = int(x / factor)
        res_y = int(y / factor)
        
    else:
        short_pic = True
    
    if short_pic == True:
        if x > y:
            factor = SIZE_X / x
        else:
            factor = SIZE_Y / y
        res_x = int(x * factor)
        res_y = int(y * factor)
        
    m.size = int(res_x)
    print("X: " , x , " Y: " , y , " LIGNE: " , m.size, " X FINAL: " , res_x , " Y FINAL: " , res_y)
    new_image = image.resize((res_x,res_y))
    new_image.convert('RGB').save('picture.jpg')

def click_on_colour(color,pos,pic_x,pic_y,klick):
    check_key_quit("x")
    X = 477
    Y = 274
    idx_x = 0
    idx_y = 0
    if klick == 1:
        time.sleep(0.5)
        pyautogui.click(x=pos[0] , y=pos[1])
        pyautogui.click(x=idx_x+20, y=idx_y+30)
    elif klick == 2:
        pyautogui.PAUSE = 0.00000001     
        pyautogui.click(x=idx_x+20, y=idx_y+30)
    
    else:
        pyautogui.PAUSE = 0.00000001
        pyautogui.click(x=X+pic_x+20 ,y=Y+pic_y+30)
        

def draw_pic(m):
    pic_pix = get_pixel()
    a_colour = print_colour_from_pic()
    a_unique_colour = list(dict.fromkeys(a_colour))
    sorted_colors = sorted(a_unique_colour, key=lambda x: a_colour.count(x))
    
    for col in sorted_colors:
       count = a_colour.count(col)
       print("col:", col, count)
    
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
    pixel_size = 5
    for j in range(len(sorted_colors)):
        for i in range(len(pic_pix)):
            color = sorted_colors[j]
            pos = colours_pos[sorted_colors[j]]
            if once == 0:
                click_on_colour(color,pos,idx_x,idx_y,1)
                once = 1 
            if i % m.size == 0:
                idx_y = idx_y + pixel_size
                idx_x = 0
            idx_x = idx_x + pixel_size
            if pic_pix[i] != 765:
                if pic_pix[i] == one_pic[change_c] and color != "white":
                    click_on_colour(color,pos,idx_x,idx_y,0)
        idx_x = 0
        idx_y = 0
        once = 0
        change_c = change_c + 1


def better_closest(c: Colour) -> str:
    return min(tuple_colours, key=lambda k: math.dist(c, tuple_colours[k]))

def adjust_pixels(img: Image.Image) -> list[str]:
    pixels: list[Colour] = list(img.getdata())  # type: ignore
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
    pic = input("pic to draw: ")
    download_and_resize_pic(pic,m)
    print("prout")
    time.sleep(5)
    draw_pic(m)
except:
    pic = "https://files.structurae.net/files/covers/doa127.jpg"
    download_and_resize_pic(pic,m)
    time.sleep(5)
    draw_pic(m)
