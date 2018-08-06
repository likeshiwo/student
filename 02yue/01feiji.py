#导入可能导入的包
import pygame
import random
import time

#控制自己飞机
class Hero:
    def __init__(self,screen,image,x,y,w,h):
        self.screen=screen
        self.image=image
        self.x=x
        self.zou=5
        self.y=y
        self.jian=0
        self.w=w
        self.h=h
        self.index=0
        self.jia=0
        self.hero=pygame.image.load(self.image)
        self.rect=pygame.Rect(self.x,self.y,self.w,self.h)
        self.l=[]
        self.ll=[]
        self.baozhatu()

    #显示飞机
    def display(self):
        self.screen.blit(self.hero,self.rect)
        for i in self.l:
            if i.shanchu():
                self.l.remove(i)
            i.display()
            i.move()
    #发射子弹
    def kaipao(self):
        self.l.append(Herozidan(self.screen,'./images/bullet.png',self.rect.x,self.rect.y))
    #移动已机
    def move(self):
        keys_pressed=pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT]:
            if self.rect.x < 400-self.rect.w:
                self.rect.x += self.zou
        if keys_pressed[pygame.K_LEFT]:
            if self.rect.x > 0:
                self.rect.x -=self.zou
        if keys_pressed[pygame.K_UP]:
            if self.rect.y > 0:
                self.rect.y -= self.zou
        if keys_pressed[pygame.K_DOWN]:
            if self.rect.y <= 800-self.rect.h:
                self.rect.y += self.zou
        if keys_pressed[pygame.K_SPACE]:
            self.kaipao()
    #已机爆炸
    def baozhatu(self):
        self.ll.append(pygame.image.load('./images/zha1.png'))
        self.ll.append(pygame.image.load('./images/zha.png'))
        self.ll.append(pygame.image.load('./images/zha2.png'))
        self.ll.append(pygame.image.load('./images/zha3.png'))
    #执行爆炸图
    def zhatu(self):
        if self.jian==True:
            self.screen.blit(self.ll[self.index],self.rect)
            self.jia += 1
            if self.jia == 7:
                self.index += 1
                self.jia = 0
            if self.index > 3:
                time.sleep(1)
                print('很遗憾，你输了!')
                exit()
    def chongxi(self):
        self.jian=True
#制造P2飞机
class Hero2:
    def __init__(self,screen,image,x,y,w,h):
        self.screen=screen
        self.image=image
        self.x=x
        self.zou=5
        self.y=y
        self.jian=0
        self.w=w
        self.h=h
        self.index=0
        self.jia=0
        self.hero=pygame.image.load(self.image)
        self.rect=pygame.Rect(self.x,self.y,self.w,self.h)
        self.l=[]
        self.ll=[]
        self.baozhatu()

    #显示飞机
    def display(self):
        self.screen.blit(self.hero,self.rect)
        for i in self.l:
            if i.shanchu():
                self.l.remove(i)
            i.display()
            i.move()
    #发射子弹
    def kaipao(self):
        self.l.append(Youzidan(self.screen,'./images/bullet-2.gif',self.rect.x,self.rect.y))
    #移动友机
    def move(self):
        keys_pressed=pygame.key.get_pressed()
        if keys_pressed[pygame.K_d]:
            if self.rect.x < 400-self.rect.w:
                self.rect.x += self.zou
        if keys_pressed[pygame.K_a]:
            if self.rect.x > 0:
                self.rect.x -=self.zou
        if keys_pressed[pygame.K_w]:
            if self.rect.y > 0:
                self.rect.y -= self.zou
        if keys_pressed[pygame.K_s]:
            if self.rect.y <= 800-self.rect.h:
                self.rect.y += self.zou
        if keys_pressed[pygame.K_SPACE]:
            self.kaipao()
    #友机爆炸
    def baozhatu(self):
        self.ll.append(pygame.image.load('./images/zha1.png'))
        self.ll.append(pygame.image.load('./images/zha.png'))
        self.ll.append(pygame.image.load('./images/zha2.png'))
        self.ll.append(pygame.image.load('./images/zha3.png'))
    #执行爆炸图
    def zhatu(self):
        if self.jian==True:
            self.screen.blit(self.ll[self.index],self.rect)
            self.jia += 1
            if self.jia == 7:
                self.index += 1
                self.jia = 0
            if self.index > 3:
                time.sleep(1)
                print('很遗憾，你输了!')
                exit()
    def chongxi(self):
        self.jian=True


 #制造敌机
class Diren:
    def __init__(self,screen,image,x,y,w,h):
        self.screen=screen
        self.image=image
        self.x=x
        self.y=y
        self.index=0
        self.jia=0
        self.f='no'
        self.w=w
        self.h=h
        self.zhixing=0
        self.diren=pygame.image.load(self.image)
        self.rect=pygame.Rect(self.x,self.y,self.w,self.h)
        self.l2=[]
        self.ll=[]
        self.baozha()
    #显示敌机
    def display(self):
        self.screen.blit(self.diren,self.rect)
        for i in self.l2:
            if i.shanchu():
                self.l2.remove(i)
            i.display()
            i.move()
    #显示敌机子弹
    def gongji(self):
        self.l2.append(Direnzidan(self.screen,'./images/bullet1.png',self.rect.x,self.rect.y))
    #敌机的移动
    def move(self):
        if self.f=='no':
            self.rect.x += 2
        if self.rect.x >= 400-self.rect.w:
            self.f='yes'
        if self.f=='yes':
            self.rect.x-=2
        if self.rect.x<=0:
            self.f='no'
        q=random.randint(1,60)
        if q==5:
            self.gongji()
    #敌机爆炸图
    def baozha(self):
        self.ll.append(pygame.image.load('./images/huai.png'))
        self.ll.append(pygame.image.load('./images/huai1.png'))
        self.ll.append(pygame.image.load('./images/huai2.png'))
    #执行爆炸图
    def baotu(self):
        if self.zhixing==True:
            self.screen.blit(self.ll[self.index],self.rect)
            self.jia += 1
            if self.jia == 7:
                self.index += 1
                self.jia = 0
            if self.index > 2:
                time.sleep(1)
                print('游戏结束，你赢了！')
                exit()
    def zhi(self):
        self.zhixing=True

#创建敌机子弹
class Direnzidan:
    def __init__(self,screen,image,x,y):
        self.screen=screen
        self.image=image
        self.x=x+20
        self.y=y
        self.zidan=pygame.image.load(self.image)
    #显示敌机子弹
    def display(self):
        self.screen.blit(self.zidan,(self.x,self.y))
    #敌机子弹的移动
    def move(self):
        self.y+=2
        #敌机子弹的删除
    def shanchu(self):
        if self.y>=800:
            return True
        else:
            return False

#创建自己飞机的子弹
class Herozidan:
    def __init__(self,screen,image,x,y):
        self.screen=screen
        self.image=image
        self.x=x+40
        self.y=y
        self.zidan=pygame.image.load(self.image)
    #显示自己飞机的子弹
    def display(self):
        self.screen.blit(self.zidan,(self.x,self.y))
    #移动已机
    def move(self):
        self.y-=3
    #删除已机子弹
    def shanchu(self):
        if self.y<0:
            return True
        else:
            return False
#创建友飞机的另一种武器
class Youzidan:
    def __init__(self,screen,image,x,y):
        self.screen=screen
        self.image=image
        self.x=x+40
        self.y=y
        self.zidan=pygame.image.load(self.image)
    #显示自己飞机的子弹
    def display(self):
        self.screen.blit(self.zidan,(self.x,self.y))
    #移动已机
    def move(self):
        self.y-=3
    #删除已机子弹
    def shanchu(self):
        if self.y<0:
            return True
        else:
            return False

def panduan(a,b):
    for i in b.l2:
        if i.x > a.rect.x and i.x < a.rect.x+a.rect.w and i.y > a.rect.y and i.y < a.rect.y+a.rect.h:
            a.chongxi()

def panduan2(a,b):
    for i in b.l2:
        if i.x > a.rect.x and i.x < a.rect.x+a.rect.w and i.y > a.rect.y and i.y < a.rect.y+a.rect.h:
            a.chongxi()
#def dipanduan(a,b):
    for i in a.l:
        if i.x > b.rect.x and i.x < b.rect.x+b.rect.w and i.y > b.rect.y and i.y < b.rect.y+b.rect.h:
            b.zhi()

#游戏窗口
def main():
    background=pygame.image.load('./images/background.png')
    screen=pygame.display.set_mode((400,800),0,32)
    like=Hero(screen,'./images/hero.gif',100,650,100,100)
    #lizhe=Hero2(screen,'./images/hero.gif',200,750,100,100)
    q=random.randint(0,400)
    w=random.randint(0,100)
    diren=Diren(screen,'./images/enemy1.png',q,w,60,60)

    clock=pygame.time.Clock()
    while True:
        screen.blit(background,(0,0))
        like.zhatu()
        #lizhe.zhatu()
        diren.baotu()
        #lizhe.display()
        like.display()
        diren.display()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                print('游戏退出')
                pygame.quit()
                exit()
        like.move()
        diren.move()
        #lizhe.move()
        panduan(like,diren)
        panduan2(like,diren)
        #dipanduan(lizhe,diren)
        #刷新显示
        pygame.display.update()
        clock.tick(60)
while True:
    if __name__ == '__main__':
        main()



