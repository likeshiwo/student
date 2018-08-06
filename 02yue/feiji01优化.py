import pygame
import random
#英雄
class Hero:
    def __init__(self,screen,image,x,y,w,h):
        self.screen=screen
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.image=image
        self.heros=pygame.image.load(self.image)
        self.rect=pygame.Rect(self.x,self.y,self.w,self.h)
        self.l=[]
        self.l2=[]
    def display(self):
        self.screen.blit(self.heros,self.rect)
        for i in self.l:
            if i.shanchu():
               self.l.remove(i)
            i.display()
            i.move()
    def display2(self):
        self.screen.blit(self.heros,self.rect)
        for i in self.l:
            if i.shanchu2():
                self.l.remove(i)
            i.display2()
            i.move2()
    def zhale(self):
        self.l2.append(Zha(self.screen,'./images/hero_blowup_n1.png',self.rect.x,self.rect.y))
        self.l2.append(Zha(self.screen,'./images/hero_blowup_n2.png',self.rect.x,self.rect.y))
        self.l2.append(Zha(self.screen,'./images/hero_blowup_n3.png',self.rect.x,self.rect.y))
        self.l2.append(Zha(self.screen,'./images/hero_blowup_n4.png',self.rect.x,self.rect.y))
        self.ci=0
        self.shu=0
        i=True
        if i==True:
            self.screen.blit(self.l2[self.ci],self.rect)
            self.shu+=1
            if shu==7:
                self.ci+=1
                self.shu=0
            if self.ci>=3:
                time.sleep(1)
                exit()
        else:
            self.screen.blit(self.image,self.rect)

    def gongji(self):
        self.l.append(Zidan(self.screen,'./images/bullet1.png',self.rect.x,self.rect.y))

    def kaipao(self):
        self.l.append(Zidan(self.screen,'./images/bullet.png',self.rect.x,self.rect.y))

class Zha:
    def __init__(self,screen,image,x,y):
        self.screen=screen
        self.image=image
        self.x=x
        self.y=y
        self.zha=pygame.image.load(self.image)
    def display(self):
        self.screen.blit(self.zha,self.rect)




#子弹
class Zidan(Hero):
    def __init__(self,screen,image,x,y):
        self.screen=screen
        self.image=image
        self.x=x+40
        self.y=y
        self.zidan1=pygame.image.load(self.image)

    def display2(self):
        self.screen.blit(self.zidan1,(self.x,self.y))

    def display(self):
        self.screen.blit(self.zidan1,(self.x,self.y))
    def move(self):
        self.y-=2
    def move2(self):
        self.y+=2
    def shanchu(self):
        if self.y<0:
            return True
        else:
            return False
    def shanchu2(self):
        if self.y>500:
            return True
        else:
            return False

def main():
    #游戏窗口
    background=pygame.image.load('./images/background.png')
    screen=pygame.display.set_mode((400,500),0,32)
    hero=Hero(screen,'./images/hero.gif',100,350,70,100)
    #吃饭！
    q=random.randint(0,400)
    w=random.randint(0,100)
    diren=Hero(screen,'./images/enemy1.png',q,w,70,100)
    clock=pygame.time.Clock()
    f='r'
    while True:
        screen.blit(background,(0,0))
        hero.display()
        diren.display2()
        zou=5
        #自己飞机
        if hero.rect.x==400:
            hero.rect.x=400
        elif hero.rect.x==0:
            hero.rect.x=0
        elif hero.rect.y==500:
            hero.rect.y=500
        elif hero.rect.y==0:
            hero.rect.y=0


        for event in pygame.event.get():
            print('操作= ', event.type)
            print('你在作 = ',event)
            if event.type==pygame.QUIT:
                print('游戏退出')
                pygame.quit()
                exit()#退出
        #敌机
        if f=='r':
            diren.rect.x+=1
        else:
            diren.rect.x-=1
        if diren.rect.x==400:
            f='l'
        elif diren.rect.x==0:
            f='r'
        q=random.randint(1,50)
        if q==5:
            diren.gongji()


        #移动
        a=0
        keys_pressed=pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]:
            if hero.rect.x < 400-hero.rect.w:
                hero.rect.x += zou

        if keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]:
            if hero.rect.x > 0:
                hero.rect.x -= zou
        if keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]:
            if hero.rect.y > 0:
                hero.rect.y-=zou
        if keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_s]:
            if hero.rect.y < 500:
                hero.rect.y+=zou
        if keys_pressed[pygame.K_SPACE]:
            hero.kaipao()

        hero.zhale()



     #刷新显示
        pygame.display.update()
        clock.tick(60)
main()
