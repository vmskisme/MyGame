# 幻灵
# version 0.1
# By 覃向荣
# 2018-4-30

import pygame
import sys
from pygame.locals import *
from settings import *
from image_load import *
from role import role1,role2
from skills import *


pygame.init()
DISPLAYSURF = pygame.display.set_mode((width,height))#创建一个长width,宽height的窗口
pygame.display.set_caption("幻灵")#标题
FPSCLOCK=pygame.time.Clock()


#主循环
while True:

    #处理游戏结果
    if role1.HP<=0 or role2.HP<=0:
        if role1.HP <= 0:
            DISPLAYSURF.fill((0,0,0))
            DISPLAYSURF.blit(vctory, (width / 2 - 80, height - 800))
        elif role2.HP <= 0:
            DISPLAYSURF.fill((0, 0, 0))
            DISPLAYSURF.blit(defeat, (width / 2 - 80, height - 800))
    else:
        # 绘制背景
        DISPLAYSURF.blit(background1, (0, 0))
        DISPLAYSURF.blit(background2, (0, 0))

        # 绘制状态栏
        for length in range(0, width, state_bar_width):
            DISPLAYSURF.blit(state_bar, (length, height - state_bar_height))
        # 显示状态
        drawPoint(DISPLAYSURF)

        # 角色站立动作
        if role1.state_standing:
            DISPLAYSURF.blit(role1.standing, (200, 460))
        if role2.state_standing:
            DISPLAYSURF.blit(role2.standing, (width - 200, 420))

        # 如果是玩家回合，绘制技能栏
        if round.Round('剑士'):
            drawSkill_bar(DISPLAYSURF)
            #剑士攻击
            if saber_skills.attack:
                saber_skills.CastSkill(DISPLAYSURF)

        #法师攻击
        if round.Round('法师'):
            caster_skills.CastSkill(DISPLAYSURF)

    for event in pygame.event.get():#获取事件
        if event.type==QUIT:#关闭游戏
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:#移动鼠标
            mouse_x,mouse_y=event.pos#只是记录鼠标位置，不做其他任何操作
        elif event.type == MOUSEBUTTONUP:#按下鼠标的时候
            mouse_x, mouse_y = event.pos#读取鼠标的位置
            if round.Round('剑士'):
                saber_skills.attack=True
                saber_skills.action = saber_skills.judge_skill(mouse_x,mouse_y)


    pygame.display.update()
    FPSCLOCK.tick(FPS)