from tkinter import *
import random
 
class Ball: #定义球类
    def __init__(self, racket):
        self.racket = racket
        
        self.id = cv.create_oval(0, 0, 20, 20, fill="yellow") #绘制一个黄色的圆形作为球
        cv.move(self.id, WIDTH//2, HEIGHT//2) #使球初始位于窗口中央
        
        self.xspeed = random.choice([3, -3]) #设置球的x速度
        self.yspeed = -3 #设置球的y速度
 
    def run(self):
        cv.move(self.id, self.xspeed, self.yspeed) #将球移动self.xspeed, self.yspeed个像素
        
        pos = cv.coords(self.id) #获取球的位置，返回(x1, y1, x2, y2)
        
        if pos[0] <= 0: #如果球的位置越过屏幕左侧
            self.xspeed = 3 #根据坐标系，速度设置为正则向右移动
        elif pos[2] >= WIDTH: #如果球的位置越过屏幕右侧
            self.xspeed = -3 #向右移动
 
        if pos[1] <= 0: #如果球的位置越过屏幕上方
            self.yspeed = 3 #向下移动
        elif pos[3] >= HEIGHT: #如果球的位置越过屏幕下方
            print("你失败了！")
            root.destroy() #接球失败，游戏结束
 
        if self.id in cv.find_overlapping(*cv.coords(self.racket)): #如果球碰撞到球拍
            self.yspeed = -3 #球向上弹起
 
class Racket: #定义球拍类
    def __init__(self):        
        self.id = cv.create_rectangle(0, 0, 90, 15, fill="blue") #绘制一个蓝色的矩形作为球拍
        cv.move(self.id, WIDTH//2, 200) #设置球拍的初始位置
 
        self.xspeed = 0 #球拍默认不移动
        root.bind("<Left>", self.move_left) #按左键执行self.move_left
        root.bind("<Right>", self.move_right) #按右键执行self.move_right
 
    def run(self):
        pos = cv.coords(self.id) #获取球拍位置
        
        if (pos[0] <= 0 and self.xspeed < 0) or \
           (pos[2] >= WIDTH and self.xspeed > 0): #如果移动方式会导致球拍超出屏幕范围
            self.xspeed = 0
        else:
            cv.move(self.id, self.xspeed, 0) #移动球拍
        
    def move_left(self, event): #左移
        self.xspeed = -3
 
    def move_right(self, event): #右移
        self.xspeed = 3
 
 
root = Tk()
root.focus_force() #使窗口获取焦点
 
cv = Canvas(root, bg="white", highlightthickness=0)
cv.pack()
 
root.update()
WIDTH = root.winfo_width()
HEIGHT = root.winfo_height() #获取窗口宽高
 
racket = Racket()
ball = Ball(racket.id)
 
def run():
    racket.run()
    ball.run()
    root.after(20, run)
 
root.after(20, run) #20毫秒后执行run
root.mainloop()