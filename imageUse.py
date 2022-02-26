#image

import pygame as pg
import os
import numpy as np

def location(filename, display, x=0, y=0, a=96, b=96):
    image = pg.image.load(os.path.join('image', filename))
    image = pg.transform.scale(image,(a,b)) #调整到新的分辨率 
    display.blit(image,(x,y))   

def picture(filename, a=160, b=160):
    image = pg.image.load(os.path.join('image', filename))
    image = pg.transform.scale(image, (a,b))  
    return image
    
def word(text, display, x, y, size=30, color=(0,0,0)):
    font = pg.font.SysFont('comicsansms', size)
    render_txt = font.render(text, True, color)
    display.blit(render_txt, (x,y))


def CountDownImgs():
    imgs = []
    imgs.append(picture('LeftO.png',96,96))
    imgs.append(picture('momo.png',96,96))
    imgs.append(picture('surprised.png',96,96))
    imgs.append(picture('yushan.png',96,96))
    imgs.append(picture('grin.png',96,96))
    imgs = np.array(imgs)
    return imgs
        
def Emotion():
    imgs = []
    imgs.append(picture('pessistic.png',600,480))
    imgs.append(picture('surprised.png',600,480))
    imgs.append(picture('wink.png',600,480))
    imgs.append(picture('sad.png',600,480))
    imgs.append(picture('grin.png',600,480))
    imgs.append(picture('angry.png',600,480))
    imgs.append(picture('LeftO.png',600,480))
    imgs.append(picture('RightO.png',600,480))
    imgs.append(picture('toothache.png',600,480))
    imgs.append(picture('calm.png',600,480))
    imgs.append(picture('bling.png',600,480))
    imgs = np.array(imgs)

    buttons = []
    buttons.append(picture('pause.png',96,96))
    buttons.append(picture('exit.png',96,96))
    buttons = np.array(buttons)

    return imgs, buttons

def PauseButtons():
    buttons = []
    buttons.append(picture('play.png',200,200))
    buttons.append(picture('exit.png',200,200))
    return buttons
    
def EndButtons():
    buttons = []
    buttons.append(picture('replay.png',200,200))
    buttons.append(picture('exit.png',200,200))
    return buttons
