#face game

import os
import pygame as pg
import numpy as np
import random
from OpenCamera import Camera
from imageUse import *

class FaceGame:
    def __init__(self, display):
        self.black = (0,0,0)#黑色
        self.white = (255,255,255)#白色
        self.display = display#显示
        self.camera = Camera(self.display)#摄像头
        self.emotion, self.buttons = Emotion()
        
    
    def cover(self):
        self.display.fill(self.black)#背景设成黑色
        location('cover.jpg',self.display,0,0,740,480)
        pg.display.update()#设置开头背景
        
        while True:  
            for event in pg.event.get():#取得输入
                if event.type == pg.QUIT:#检查事件类型：游戏是否关闭
                    pg.quit()   #关闭游戏   
            mouse = pg.mouse.get_pos()
            click = pg.mouse.get_pressed()
            if 310<=mouse[0]<=420 and 250<=mouse[1]<=310 and click[0]==1:
                break   
            #mouse[0]=x轴，mouse[1]=y轴，位置根据图片改
    
    def menu(self):
        self.display.fill(self.white)
        location('level1.png',self.display,168,72,404,337)
        location('level2.png',self.display,168,72,404,337)
        location('level3.png',self.display,168,72,404,337)
        pg.display.update()


        while True:  
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()                    
            mouse = pg.mouse.get_pos()
            click = pg.mouse.get_pressed()
            if 245<=mouse[0]<=495 and 64<=mouse[1]<=160 and click[0]==1:
                self.level = 1
                print("level 1 ...")
                break
            elif 245<=mouse[0]<=495 and 192<=mouse[1]<=288 and click[0]==1:
                self.level = 2
                print("level 2 ...")
                break
            elif 245<=mouse[0]<=495 and 320<=mouse[1]<=416 and click[0]==1:
                self.level = 3
                print("level 3 ...")
                break
    def countDown(self):
        imgs = CountDownImgs()
        countDownImg = [picture(str(index)+'.png',576,480) for index in range(4)]
        start = pg.time.get_ticks()
        
        while True:
            sec = (pg.time.get_ticks()-start)/1000  
            index = int(sec)
            if index > 3:
                break
            self.display.fill(self.white)
            #self.display.blit(pg.transform.flip(self.camera.capture(), True, False), (0,0))
            self.display.blit(countDownImg[index], (32,0))
            pg.display.update()

    def start(self):
        print("start")
        score = 0
        count = 0
       
                        

        
     def pause(self):
        buttons = loadPauseButtons()

        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()                    
            mouse = pg.mouse.get_pos()
            click = pg.mouse.get_pressed()
            #play
            if 100<=mouse[0]<=300 and 190<=mouse[1]<=310 and click[0]==1:
                return False
            #exit
            if 440<=mouse[0]<=640 and 190<=mouse[1]<=310 and click[0]==1:
                return True
            self.display.fill(self.black)
            self.display.blit(buttons[0], (100, 190))
            self.display.blit(buttons[1], (440, 190))
            pg.display.update()
    
    def exit(self):
        self.display.fill(self.black)
        loadNblit('bye_3.png',self.display,82,0,576,480) 
        pg.display.update()
        print("exitting ...")
        pg.time.wait(1000)
    
    def end(self, score):
        self.display.fill(self.black)
        buttons = loadEndButtons()

        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()                    
            mouse = pg.mouse.get_pos()
            click = pg.mouse.get_pressed()
            #replay
            if 100<=mouse[0]<=300 and 260<=mouse[1]<=460 and click[0]==1:
                return False
            #exit
            if 440<=mouse[0]<=640 and 260<=mouse[1]<=460 and click[0]==1:
                return True
            self.display.fill(self.black)
            show_text("Score: " + str(score), self.display, 100, 100, 80)
            self.display.blit(buttons[0], (100, 260))
            self.display.blit(buttons[1], (440, 260))
            pg.display.update()   
        
                
            

            
            


        



    def run(self):
        self.cover()
        running = True
        while running:
            self.menu()
            self.start()
            for event in pg.event.get():#取得输入
                if event.type == pg.QUIT:
                    running = False
            
        pg.quit()     
        print("success")
        self.camera.stop()
        
   