import pygame
import os
from settings import *
from role import *
from image_load import *
import random


caster_skills_path = '技能\法师技能\\'
caster_path ='主角\女主角\\'
saber_skills_path='技能\剑士技能\\'
role2_path = '主角\男主角\\'



#剑士的技能类
class saber_skills():
    def __init__(self):
        self.attack = False
        self.count = 1
        self.x = 680
        self.y = 440
        self.action=' '

    #还原设置
    def revoer(self):
        caster_skills.skill_name = caster_skills.randomSkill()
        round.round=1
        self.count=1
        self.x=680
        self.attack=False
        role1.state_standing = True
        role2.state_standing=True

    #判断玩家点击的技能
    def judge_skill(self,x,y):
        if width/2+120<x<width/2+120+role2_normal_attack.get_rect()[2] and height/2-270<y<height/2-270+role2_normal_attack.get_rect()[3]:
            return '普通攻击'
        if width/2+120<x<width/2+120+role2_skill1.get_rect()[2] and height/2-240<y<height/2-240+role2_skill1.get_rect()[3]:
            return '剑气'
        if width/2+120<x<width/2+120+role2_skill2.get_rect()[2] and height/2-210<y<height/2-210+role2_skill2.get_rect()[3]:
            return '旋光'
        if width/2+120<x<width/2+120+role2_skill3.get_rect()[2] and height/2-180<y<height/2-180+role2_skill3.get_rect()[3]:
            return '穿心'
        if width/2+120<x<width/2+120+role2_skill4.get_rect()[2] and height/2-150<y<height/2-150+role2_skill4.get_rect()[3]:
            return '强化'

    #根据self.action施放技能
    def CastSkill(self,surface):
        if self.action=='普通攻击':
            if self.count==15:
                self.revoer()
                role1.HP -= role2.STR + random.randint(-10, 10)
            elif self.count<10:
                moblie = pygame.image.load(role2_path+'男剑士冲刺.png')
                surface.blit(moblie,(self.x,self.y))
                self.x-=60
                self.count+=1
                role2.state_standing=False
            else:
                normal_attack = pygame.image.load(role2_path + '男剑士攻击.png')
                surface.blit(role1.injured,(200,460))
                surface.blit(normal_attack, (self.x, self.y))
                role1.state_standing=False
                self.count+=1

        elif self.action == '剑气':
            if role2.MP<200:
                return
            if os.path.exists(saber_skills_path + self.action + ' (' + str(self.count) + ').png'):
                skill = pygame.image.load(saber_skills_path + self.action + ' (' + str(self.count) + ').png')
                surface.blit(skill, (self.x, self.y))
                surface.blit(role2.cast,(width-200,360))
                if self.count>5:
                    surface.blit(role1.injured,(200,460))
                    role1.state_standing=False
                role2.state_standing=False
                self.count+=1
                self.x-=80
            else:
                self.revoer()
                role2.MP-=200
                role1.HP -= 100+role2.STR + random.randint(-20, 20)

        elif self.action=='穿心':
            if role2.MP<1000:
                return
            if self.count<15:
                moblie = pygame.image.load(role2_path + '男剑士冲刺.png')
                surface.blit(moblie, (self.x, self.y))
                role2.state_standing = False
                self.x -= 50
                self.count+=1
            elif os.path.exists(saber_skills_path + self.action +' ('+str(self.count-14)+').png'):
                skill = pygame.image.load(saber_skills_path + self.action + ' (' + str(self.count-14) + ').png')
                surface.blit(role1.injured, (200, 460))
                surface.blit(skill, (30, 400))
                surface.blit(role2.attack,(self.x,self.y))
                role2.state_standing = False
                role1.state_standing = False
                self.count+=1
            else:
                self.revoer()
                role2.MP-=1000
                role1.HP -= 300+role2.STR*2 + random.randint(-30, 50)

        elif self.action == '旋光':
            if role2.MP<400:
                return
            if os.path.exists(saber_skills_path + self.action + ' (' + str(self.count) + ').png'):
                skill = pygame.image.load(saber_skills_path + self.action + ' (' + str(self.count) + ').png')
                surface.blit(role1.injured, (200, 460))
                surface.blit(skill, (120, 400))
                surface.blit(role2.cast, (width - 200, 360))
                role2.state_standing = False
                role1.state_standing = False
                self.count+=1
            else:
                self.revoer()
                role2.MP-=400
                role1.HP -= 100+int(role2.STR*1.5) + random.randint(-10, 10)

        elif self.action == '强化':
            if role2.MP<200:
                return
            if self.count<=15:
                skill = pygame.image.load(saber_skills_path +'施法.png')
                surface.blit(skill, (self.x+30, self.y-100))
                surface.blit(role2.cast, (width - 200, 360))
                role2.state_standing = False
                self.count+=1
            else:
                role2.MP-=200
                role2.STR+=50
                self.revoer()


#法师的技能类
class caster_skills():
    def __init__(self):
        self.x=200
        self.y=400
        self.count=1
        self.attack=False
        self.name=('火球术','光爆','雷弹','落雷','一闪','心裂')
        self.skill_name=''

    #还原设置
    def recover(self):
        round.round=2
        self.attack = False
        self.count = 1
        self.x = 200
        role1.state_standing = True
        role2.state_standing = True

    #随机返回某一技能
    def randomSkill(self):
        skill=random.randint(1,100)
        if 1<skill<26:
            return self.name[0]
        if 25<skill<45:
            return self.name[1]
        if 45<skill<61:
            return self.name[2]
        if 60<skill<76:
            return self.name[3]
        if 75<skill<91:
            return self.name[4]
        if 90<skill<101:
            return self.name[5]

    #根据随机返回的技能名施放技能
    def CastSkill(self,surface):
        if self.skill_name == self.name[0]:
            if self.count==15:
                role1.MP-=200
                self.recover()
                role2.HP -= 200 + random.randint(-5, 5)
            elif self.count<10:
                skill = pygame.image.load(caster_skills_path+self.skill_name+'.png')
                surface.blit(skill,(self.x,self.y-100))
                surface.blit(role1.cast,(200,460))
                self.x+=50
                self.count+=1
                role1.state_standing=False
            else:
                skill = pygame.image.load(caster_skills_path + self.skill_name + '.png')
                surface.blit(skill, (self.x, self.y-100))
                surface.blit(role1.cast, (200, 460))
                surface.blit(role2.injured,(width-200,420))
                self.x += 50
                self.count+=1
                role2.state_standing=False

        elif self.skill_name == self.name[1]:
            if not os.path.exists(caster_skills_path+self.skill_name+' ('+str(self.count)+').png'):
                self.recover()
                role1.MP -= 300
                role2.HP-=300+random.randint(-10,20)
            else:
                skill = pygame.image.load(caster_skills_path+self.skill_name+' ('+str(self.count)+').png')
                surface.blit(role2.injured, (width - 200, 420))
                surface.blit(skill,(width-250,420))
                surface.blit(role1.cast,(200,460))
                self.count+=1
                role1.state_standing=False
                role2.state_standing=False

        elif self.skill_name == self.name[2]:
            if self.count==15:
                self.recover()
                role1.MP -= 300
                role2.HP-=600+random.randint(-50,50)
            elif self.count < 10:
                skill = pygame.image.load(caster_skills_path + self.skill_name + '.png')
                surface.blit(skill, (self.x+50, self.y))
                surface.blit(role1.cast, (200, 460))
                self.x += 50
                self.count += 1
                role1.state_standing = False
            else:
                skill = pygame.image.load(caster_skills_path + self.skill_name + '.png')
                surface.blit(skill, (self.x+50, self.y))
                surface.blit(role1.cast, (200, 460))
                surface.blit(role2.injured, (width - 200, 420))
                self.x += 50
                self.count += 1
                role2.state_standing = False

        elif self.skill_name==self.name[3]:
            if not os.path.exists(caster_skills_path+self.skill_name+' ('+str(self.count)+').png'):
                self.recover()
                role1.MP -= 300
                role2.HP-=600+random.randint(-100,50)
            else:
                skill = pygame.image.load(caster_skills_path+self.skill_name+' ('+str(self.count)+').png')
                surface.blit(role2.injured, (width - 200, 420))
                surface.blit(skill,(width-350,200))
                surface.blit(role1.cast,(200,460))
                self.count+=1
                role1.state_standing=False
                role2.state_standing=False

        elif self.skill_name == self.name[4]:
            if not os.path.exists(caster_skills_path+self.skill_name+' ('+str(self.count)+').png'):
                if self.count<=15:
                    skill = pygame.image.load(caster_skills_path+self.skill_name+' (3).png')
                    surface.blit(role2.injured, (width - 200, 420))
                    surface.blit(skill,(self.x,self.y))
                    self.count+=1
                    self.x+=60
                if self.count <=10:
                    skill = pygame.image.load(caster_skills_path + self.skill_name + ' (3).png')
                    surface.blit(role2.injured, (width - 200, 420))
                    surface.blit(skill, (self.x, self.y))
                    self.count += 1
                    self.x += 60
                else:
                    role1.MP -= 200
                    self.recover()
                    role2.HP -= 600 + random.randint(0, 50)
            else:
                skill = pygame.image.load(caster_skills_path + self.skill_name + ' ('+str(self.count)+').png')
                surface.blit(skill, (self.x, self.y))
                self.x += 50
                self.count += 1

        elif self.skill_name == self.name[5]:
            if not os.path.exists(caster_skills_path + self.skill_name + ' (' + str(self.count) + ').png'):
                self.recover()
                role1.MP -= 500
                role2.HP -= 1000 + random.randint(-10, 10)
            else:
                skill = pygame.image.load(caster_skills_path + self.skill_name + ' (' + str(self.count) + ').png')
                surface.blit(role2.injured, (width - 200, 420))
                surface.blit(skill, (width - 240, 360))
                surface.blit(role1.cast, (200, 460))
                self.count += 1
                role1.state_standing = False
                role2.state_standing = False


#回合类
class round():
    def __init__(self):
        #剑士先手
        self.round=2

    #返回是否为name的回合
    def Round(self,name):
        if name=='法师':
            return self.round==1
        if name=='剑士':
            return self.round==2


saber_skills = saber_skills()#剑士技能类的对象
caster_skills =caster_skills()#法师技能类的对象
round=round()#回合对象