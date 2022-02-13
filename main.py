#main.py

import os
import pygame as pg
from face_game import FaceGame
#from Similarity import Similarity



os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d"%(30,0)

def main():
    # similarity = Similarity()

    pg.init() #游戏初始化
    display_width = 740
    display_height = 480

    clock = pg.time.Clock()#对时间
    gameDisplay = pg.display.set_mode([display_width,display_height])#游戏窗口大小
    
    #开始游戏回圈
    pg.display.set_caption('Face game') #文件标题；游戏名
    
    facegame = FaceGame(gameDisplay)
    facegame.run()
    pg.quit()

if  __name__ == '__main__':
    main()