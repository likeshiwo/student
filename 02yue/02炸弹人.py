#先到入可能要用到的包
import pygame
import random
import time
#定义主角
class People:
    def __init__(self,screen,image,x,y):
        self.screen=screen
        self.image=image
        self.zou=10
        self.x=x
        self.y=y
        self.w=70
        self.h=50
        self.hero=pygame.image.load(self.image)
        self.rect=pygame.Rect(self.x,self.y,self.w,self.h)
        self.l=[]
    # 显示主角
    def display(self):
        self.screen.blit(self.hero,self.rect)
        for i in self.l:
            if i.shanchu():
                self.l.remove(i)
            i.display()
            i.time()
    def display2(self):
        for y in self.l:
            if y.shanchu():
                self.l.remove(y)
            y.display()
            y.time()
    #显示炮弹及炸完之后....
    def kaipao(self):
        print('kaipao')
        self.l.append(Zhadan(self.screen,'/home/like/图片/zhadan.png',self.rect.x,self.rect.y))
    def jieshu(self):
        print('jieshu')
        self.l.append(Zhawan(self.screen,'/home/like/图片/zhawan.png',self.rect.x,self.rect.y))
    # 移动
    def move(self):
        '''
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.kaipao()
                    self.jieshu()
                    '''

        keys_pressed=pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT]:
            self.rect.x += self.zou
        if keys_pressed[pygame.K_LEFT]:
            self.rect.x -= self.zou
        if keys_pressed[pygame.K_UP]:
            self.rect.y -= self.zou
        if keys_pressed[pygame.K_DOWN]:
            self.rect.y += self.zou
        if keys_pressed[pygame.K_SPACE]:
            self.kaipao()
            self.jieshu()

class Zhadan:
    def __init__(self,screen,image,x,y):
        self.screen=screen
        self.image=image
        self.x=x
        self.a='S'
        self.y=y
        self.zha=pygame.image.load(self.image)
    def display(self):
        self.screen.blit(self.zha,(self.x,self.y))
        print(self.x)
        print(self.y)
    def time(self):
        time.sleep(1.5)
        self.a='TU'
    def shanchu(self):
        if self.a=='TU':
            return True
        else:
            return False
class Zhawan:
    def __init__(self,screen,image,x,y):
        self.screen=screen
        self.image=image
        self.x=x
        self.y=y
        self.a='b'
        self.wan=pygame.image.load(self.image)
    def display(self):
        self.screen.blit(self.wan,(self.x,self.y))
    def time(self):
        time.sleep(0.5)
        self.a='ok'
    def shanchu(self):
        if self.a=='ok':
            return True
        else:
            return False
#游戏窗口及调用函数
def main():
    background=pygame.image.load('/home/like/图片/beijing.png')
    screen=pygame.display.set_mode((1000,800),0,32)
    #xzhou=random.randint(100,900)
    #yzhou=random.randint(100,700)
    like=People(screen,'/home/like/图片/ren.png',500,500)
    clock=pygame.time.Clock()
    while True:
        #游戏的显示开始
        screen.blit(background,(0,0))
        like.display()
        like.display2()
        #监听？....
        for event in pygame.event.get():
           # print('操作:',event.type)
           # print('操作:',event)
            if event.type==pygame.QUIT:
                print('游戏退出')
                pygame.quit()
                exit()#退出
        like.move()
        #刷新显示...
        pygame.display.update()
        clock.tick(60)
while True:
    if __name__=='__main__':
        main()


