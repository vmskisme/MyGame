import pygame
from settings import *
from character import BOSS,player
from font import *


#游戏图片文件夹路径
image_path = 'image/background/'

#游戏背景
background1 = pygame.image.load(image_path+'学校大厅_远景.png')
background2 = pygame.image.load(image_path+'学校大厅_近景.png')
background3 = pygame.image.load(image_path+'学校大厅_前景.png')
notstart_background = pygame.image.load(image_path+'开始前背景.jpg')
state_bar = pygame.image.load(image_path+'状态栏.png')
state_bar_width = state_bar.get_width()
state_bar_height = state_bar.get_height()
magic_bar = pygame.image.load(image_path+'技能栏.png')
vctory = pygame.image.load(image_path+'胜利.png')
defeat = pygame.image.load(image_path+'失败.png')

#绘制开始前背景
def draw_notstartBackground(surface):
    surface.blit(notstart_background, (0, 0))
    surface.blit(fontObj.render('按任意键开始', False, White, None), (width / 2 - 90, height / 2))

#游戏中背景
def drawBackground(surface):
    surface.blit(background1,(-800,0))
    surface.blit(background2, (-800, 0))
    surface.blit(background3, (-800, 0))

#结果界面
def resulting_screen(surface):
    if player.HP<=0:
        surface.blit(defeat,(width/2-80,height-800))
    elif BOSS.HP<=0:
        surface.blit(vctory,(width/2-80,height-800))


def drawPoint(surface,BOSS,player):
    # 绘制状态栏
    for length in range(0, width, state_bar_width):
        surface.blit(state_bar, (length, height - state_bar_height))
    #绘制状态
    surface.blit(fontHP, (220, 610))
    surface.blit(fontObj.render(str(BOSS.HP), False, White, None), (260, 610))
    # surface.blit(fontMP, (220, 630))
    # surface.blit(fontObj.render(str(BOSS.MP), False, White, None), (260, 630))
    surface.blit(fontHP, (800, 610))
    surface.blit(fontObj.render(str(player.HP), False, White, None), (840, 610))
    surface.blit(fontMP, (800, 630))
    surface.blit(fontObj.render(str(player.MP), False, White, None), (840, 630))
    surface.blit(fontSTR, (800, 650))
    surface.blit(fontObj.render(str(player.STR), False, White, None), (840, 650))
    surface.blit(fontDFE, (800, 670))
    surface.blit(fontObj.render(str(player.DFE), False, White, None), (840, 670))
    surface.blit(fontWIS, (800, 690))
    surface.blit(fontObj.render(str(player.WIS), False, White, None), (840, 690))
    surface.blit(fontRage, (700, 610))
    surface.blit(fontObj.render(str(player.Rage), False, White, None), (750, 610))


#技能栏
def draw_magicbar(surface):
    surface.blit(magic_bar,(width/2+100,height/2-300))
    surface.blit(saber_attack, (width/2+120,height/2-270))
    surface.blit(saber_skill1,(width/2+120,height/2-240))
    surface.blit(saber_skill2, (width/2+120,height/2-210))
    surface.blit(saber_skill3, (width/2+120,height/2-180))
    surface.blit(saber_skill4, (width / 2 + 120, height / 2 - 150))
    surface.blit(saber_skill5, (width / 2 + 120, height / 2 - 120))
    surface.blit(saber_skill6, (width / 2 + 180, height / 2 - 270))