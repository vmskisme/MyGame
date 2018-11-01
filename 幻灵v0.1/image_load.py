import pygame
from role import role1,role2
from settings import *

#游戏图片文件夹路径
image_path = ''

#游戏背景
background1 = pygame.image.load(image_path+'背景\冈特古村1背景.png')
background2 = pygame.image.load(image_path+'背景\冈特古村1近景.png')
state_bar = pygame.image.load(image_path+'背景\状态栏.png')
state_bar_width = state_bar.get_width()
state_bar_height = state_bar.get_height()
skill_bar = pygame.image.load(image_path+'背景\技能栏.png')
vctory = pygame.image.load(image_path+'背景\胜利.png')
defeat = pygame.image.load(image_path+'背景\失败.png')

pygame.font.init()
White = (255,255,255)
fontObj = pygame.font.Font('FZLTCXHJW.ttf',20)
fontHP = fontObj.render('HP:',False,White,None)
fontMP = fontObj.render('MP:',False,White,None)
role2_normal_attack = fontObj.render('普通攻击', False, White, None)
role2_skill1 = fontObj.render('剑气', False, White, None)
role2_skill2 = fontObj.render('旋光', False, White, None)
role2_skill3 = fontObj.render('穿心', False, White, None)
role2_skill4 = fontObj.render('强化', False, White, None)


def drawPoint(surface):
    surface.blit(fontHP, (220, 610))
    surface.blit(fontObj.render(str(role1.HP),False,White,None),(260,610))
    surface.blit(fontMP, (220, 630))
    surface.blit(fontObj.render(str(role1.MP),False,White,None),(260,630))
    surface.blit(fontHP, (800, 610))
    surface.blit(fontObj.render(str(role2.HP), False, White, None), (840, 610))
    surface.blit(fontMP, (800, 630))
    surface.blit(fontObj.render(str(role2.MP), False, White, None), (840, 630))


def drawSkill_bar(surface):
    surface.blit(skill_bar,(width/2+100,height/2-300))
    surface.blit(role2_normal_attack, (width/2+120,height/2-270))
    surface.blit(role2_skill1,(width/2+120,height/2-240))
    surface.blit(role2_skill2, (width/2+120,height/2-210))
    surface.blit(role2_skill3, (width/2+120,height/2-180))
    surface.blit(role2_skill4, (width / 2 + 120, height / 2 - 150))


