# 幻灵 
# version 0.2
# By 覃向荣
#2018-5-6

import sys
from pygame.locals import *
from background import *
from character import BOSS,player


pygame.init()
DISPLAYSURF = pygame.display.set_mode((width,height))#创建一个长width,宽height的窗口
pygame.display.set_caption("幻灵")#标题
FPSCLOCK=pygame.time.Clock()
game_start = False

#主循环
while True:
    #游戏开始前界面
    if not game_start:
        draw_notstartBackground(DISPLAYSURF)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN or event.type == MOUSEBUTTONUP:#按下任意键开始游戏
                game_start = True
                pygame.time.wait(500)

    #游戏开始
    elif BOSS.HP>0 and player.HP>0:
        drawBackground(DISPLAYSURF)

        # 绘制状态栏
        for length in range(0, width, state_bar_width):
            DISPLAYSURF.blit(state_bar, (length, height - state_bar_height))
        # 显示状态
        drawPoint(DISPLAYSURF,BOSS,player)

        #人物的姿态
        player.posture(DISPLAYSURF)
        BOSS.posture(DISPLAYSURF)

        #人物的攻击
        if player.round:#玩家回合
            draw_magicbar(DISPLAYSURF)
            player.Action(DISPLAYSURF)
        elif BOSS.round:#BOSS回合
            if BOSS.frames == 0:
                BOSS.judge_magic()
            BOSS.Action(DISPLAYSURF)
        else:#一回合结束后开始下一回合
            player.round, BOSS.round = True, True


        for event in pygame.event.get():  # 获取事件
            if event.type == QUIT:  # 关闭游戏
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONUP:  # 按下鼠标的时候
                mouse_x, mouse_y = event.pos  # 读取鼠标的位置
                player.judge_magic(mouse_x, mouse_y)#通过鼠标位置判断玩家按下的行动

    else:#当玩家或者BOSS的血量下降到0和0以下时，显示游戏结束界面
        DISPLAYSURF.fill((0,0,0))
        resulting_screen(DISPLAYSURF)
        for event in pygame.event.get():  # 获取事件
            if event.type == QUIT:  # 关闭游戏
                pygame.quit()
                sys.exit()

    pygame.display.update()#更新画面
    FPSCLOCK.tick(FPS)#限制帧数
