width = 960#游戏窗口的长
height = 720#游戏窗口的宽
FPS = 30#帧数

horizon = 150#地平线

def position_y(image):#返回匹配地平线的y值
    return height-horizon-image.get_rect()[3]