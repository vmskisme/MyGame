import pygame
import os
from settings import *
import random
from font import *

#人物图片背景
role_path='image/role/'


#角色类
class character:
    def __init__(self,HP,MP,STR,DFE,WIS,path,x):
        self.HP=HP#生命值
        self.MP=MP#魔法值
        self.STR = STR  # 力量
        self.DFE = DFE  # 防御
        self.WIS = WIS  # 智力
        self.Rage = 0  # 怒气
        self.state_standing = True
        self.state_attck = False
        self.state_cast = False
        self.state_injured = False
        self.action = None
        self.frames = 0
        self.round = True
        self.standing = pygame.image.load(path + 'standing.png')
        self.injured = pygame.image.load(path + 'injured.png')
        self.position_x = x
        self.enemy = None


    #回合结束后恢复各属性
    def action_end(self,enemy,damage):
        self.state_standing = True
        self.state_attck = False
        self.state_cast = False
        self.state_injured = False
        self.action = None
        self.frames = 0
        self.round = False
        enemy.state_standing = True
        enemy.state_injured = False
        enemy.HP-=damage
        enemy.Rage+=int(damage/20)
        if enemy.Rage>100:
            enemy.Rage = 100

    #加载技能图片
    def magic(self,magic_name,path):
        i=1
        magic=[]
        while os.path.exists(path+magic_name+' ('+str(i)+').png'):
            magic.append(pygame.image.load(path+magic_name+' ('+str(i)+').png'))
            i+=1
        return magic

    #绘制此时的姿势
    def posture(self,surface):
        if self.state_standing:
            surface.blit(self.standing, (self.position_x, position_y(self.standing)))
        elif self.state_injured:
            surface.blit(self.injured, (self.position_x, position_y(self.injured)))

    def choose_enemy(self,enemy):
        self.enemy = enemy


#剑士类
class saber(character):
    def __init__(self,HP,MP,STR,DFE,WIS):
        character.__init__(self, HP, MP, STR, DFE, WIS, role_path + 'saber/', width - 200)
        #攻击动作
        self.attack = []
        for i in range(1,12):
            self.attack.append(pygame.image.load(role_path + 'saber/saber_thump' + str(i) + '.png'))
        #施法动作
        self.cast = pygame.image.load(role_path+'saber/saber_casting.png')
        #后退（前进）动作
        self.back = pygame.image.load(role_path+'saber/saber_back.png')
        #配合技能‘穿心’的动作
        self.puncture = pygame.image.load(role_path+'saber/saber_puncture.png')
        #关于技能的字典,键为技能名，值为技能图片的surface对象的列表
        self.magics = {'旋光':self.magic('旋光',role_path+'saber/magic/'),
                       '穿心':self.magic('穿心',role_path+'saber/magic/'),
                       '施法': self.magic('施法', role_path + 'saber/magic/')}


    #通过x,y判断按下的技能
    def judge_magic(self,x, y):
        if width/2+120<x<width/2+120+saber_attack.get_rect()[2] and height/2-270<y<height/2-270+saber_attack.get_rect()[3]:
            self.action = '攻击'
        elif width/2+120<x<width/2+120+saber_skill1.get_rect()[2] and height/2-240<y<height/2-240+saber_skill1.get_rect()[3]:
            self.action = '旋光'
        elif width/2+120<x<width/2+120+saber_skill2.get_rect()[2] and height/2-210<y<height/2-210+saber_skill2.get_rect()[3]:
            self.action = '穿心'
        elif width/2+120<x<width/2+120+saber_skill3.get_rect()[2] and height/2-180<y<height/2-180+saber_skill3.get_rect()[3]:
            self.action = '强化攻击'
        elif width/2+120<x<width/2+120+saber_skill4.get_rect()[2] and height/2-150<y<height/2-150+saber_skill4.get_rect()[3]:
            self.action = '强化防御'
        elif width/2+120<x<width/2+120+saber_skill5.get_rect()[2] and height/2-120<y<height/2-120+saber_skill5.get_rect()[3]:
            self.action = '强化技能'
        elif width/2+180<x<width/2+180+saber_skill6.get_rect()[2] and height/2-270<y<height/2-270+saber_skill4.get_rect()[3]:
            self.action = '回复'

    #动作
    def Action(self,surface):
        if self.action == None:
            return
        if self.action == '旋光':
            if self.MP<500:
                return
            if self.frames<len(self.magics['旋光']):
                surface.blit(self.cast, (self.position_x, position_y(self.cast)))
                surface.blit(self.magics['旋光'][self.frames], (120, 400))
                self.enemy.state_standing = False
                self.enemy.state_injured = True
                self.state_standing = False
                self.state_cast = True
                self.frames += 1
            else:
                self.MP-=500
                self.action_end(BOSS,self.WIS*6+random.randint(-10,10))

        elif self.action == '穿心':
            if self.Rage<100:
                return
            if self.frames<=10:
                surface.blit(self.back,(width-self.frames*80,position_y(self.back)))
                self.state_standing = False
                self.frames += 1
            elif self.frames<10+len(self.magics['穿心']):
                surface.blit(self.puncture, (150, position_y(self.puncture)))
                surface.blit(self.magics['穿心'][self.frames-10], (50, position_y(BOSS.injured)-60))
                self.enemy.state_standing = False
                self.enemy.state_injured = True
                self.state_cast = True
                self.frames += 1
            else:
                self.Rage-=100
                self.action_end(BOSS,300+self.WIS*6+self.STR*3+random.randint(-50,50))

        elif self.action == '攻击':
            if self.frames<len(self.attack):
                surface.blit(self.attack[self.frames],(width-200-self.frames*60,position_y(self.attack[self.frames])))
                self.state_standing = False
                self.frames += 1
                if self.frames>=len(self.attack)-1:
                    self.enemy.state_injured = True
                    self.enemy.state_standing = False
            else:
                self.action_end(BOSS,self.STR*4+random.randint(-10,10))

        elif self.action == '强化攻击' or self.action == '强化防御' or self.action == '强化技能' or self.action == '回复':
            if self.frames<10:
                self.state_standing = False
                surface.blit(self.cast, (self.position_x, position_y(self.cast)))
                surface.blit(self.magics['施法'][0], (width - 280, position_y(self.magics['施法'][0])+20))
                self.frames+=1
            else:
                if self.action == '强化攻击':
                    self.STR +=5
                    if self.STR>100:
                        self.STR = 100
                elif self.action == '强化防御':
                    self.DFE +=5
                    if self.DFE>100:
                        self.DFE = 100
                elif self.action == '强化技能':
                    self.WIS+=5
                    if self.WIS>100:
                        self.WIS = 100
                else:
                    self.MP-=1000
                    self.HP+=self.WIS*8
                    if self.HP>10000:
                        self.HP=10000
                self.action_end(BOSS,0)


#法师类
class caster(character):
    def __init__(self,HP,MP,STR,DFE,WIS):
        character.__init__(self, HP, MP, STR, DFE, WIS, role_path + 'caster/', 200)
        self.cast1 = pygame.image.load(role_path+'caster/caster_casting1.png')
        self.cast2 = pygame.image.load(role_path+'caster/caster_casting2.png')
        self.magics = {'火球术':self.magic('火球术',role_path+'caster/magic/'),
                       '雷弹':self.magic('雷弹',role_path+'caster/magic/'),
                        '流光星陨':self.magic('流光星陨',role_path+'caster/magic/'),
                       '掏心':self.magic('掏心',role_path+'caster/magic/'),}

    def judge_magic(self):
        num = random.randint(1,100)
        if self.HP>=8000:
            if 0<num<51:
                self.action = '火球术'
            else:
                self.action = '雷弹'
        elif 3000<=self.HP<8000:
            if 0<num<31:
                self.action = '火球术'
            elif 30<num<61:
                self.action = '雷弹'
            else:
                self.action = '流光星陨'
        elif 1000<=self.HP<3000:
            if 0<num<51:
                self.action = '流光星陨'
            else:
                self.action = '掏心'
        elif self.HP<1000:
            self.action = '掏心'

    def Action(self,surface):
        if self.action == None:
            return
        if self.action == '火球术':
            if self.frames < 10:
                if self.frames>5:
                    self.enemy.state_standing = False
                    self.enemy.state_injured = True
                surface.blit(self.magics['火球术'][0],(200+self.frames*80,position_y(self.magics['火球术'][0])+50))
                self.state_standing = False
                surface.blit(self.cast2,(200,position_y(self.cast2)))
                self.frames+=1
            else:
                self.action_end(player,int(200*(200-player.DFE)/100)+random.randint(-20,20))

        elif self.action == '雷弹':
            if self.frames < 10:
                if self.frames>5:
                    self.enemy.state_standing = False
                    self.enemy.state_injured = True
                surface.blit(self.magics['雷弹'][0],(200+self.frames*80,position_y(self.magics['雷弹'][0])))
                self.state_standing = False
                surface.blit(self.cast2,(200,position_y(self.cast2)))
                self.frames+=1
            else:
                self.action_end(player,int(300*(150-player.DFE)/100)+random.randint(-20,10))

        elif self.action == '流光星陨':
            if self.frames < len(self.magics['流光星陨']):
                surface.blit(self.cast1, (200, position_y(self.cast1)))
                surface.blit(self.magics['流光星陨'][self.frames], (width - 320, position_y(self.magics['流光星陨'][self.frames])+50))
                self.enemy.state_standing = False
                self.enemy.state_injured = True
                self.state_standing = False
                self.state_cast = True
                self.frames += 1
            else:
                self.action_end(player, int(500*(200-player.DFE)/100) + random.randint(-10, 10))

        elif self.action == '掏心':
            if self.frames < len(self.magics['掏心']):
                surface.blit(self.cast1, (200, position_y(self.cast1)))
                surface.blit(self.magics['掏心'][self.frames], (width - 200, position_y(self.magics['掏心'][self.frames])))
                self.enemy.state_standing = False
                self.enemy.state_injured = True
                self.state_standing = False
                self.state_cast = True
                self.frames += 1
            else:
                self.action_end(player, 1000-player.DFE + random.randint(-10, 10))


#玩家
player = saber(10000,10000,80,80,60)
#BOSS
BOSS = caster(15000,10000,0,0,0)
player.choose_enemy(BOSS)
BOSS.choose_enemy(player)

