import pygame

class role():
    def __init__(self,HP,MP,standing,attack,cast,injured):
        self.standing = standing
        self.attack = attack
        self.cast = cast
        self.injured =  injured
        self.state_standing = True
        self.state_attck = False
        self.state_cast = False
        self.state_injured = False
        self.HP=HP
        self.MP=MP
        self.STR=100


image_path = 'E:\Games\幻灵素材/'

#创建法师类的对象并导入图像
role1=role(8000,10000,
           pygame.image.load(image_path+'主角\女主角\女法师站立.png'),
           pygame.image.load(image_path + '主角\女主角\女法师攻击.png'),
           pygame.image.load(image_path + '主角\女主角\女法师施法.png'),
           pygame.image.load(image_path + '主角\女主角\女法师受伤.png'))

#创建剑士类的对象并导入图像
role2=role(10000,6000,
           pygame.image.load(image_path+'主角\男主角\男剑士站立.png'),
           pygame.image.load(image_path + '主角\男主角\男剑士攻击.png'),
           pygame.image.load(image_path + '主角\男主角\男剑士施法.png'),
           pygame.image.load(image_path + '主角\男主角\男剑士受伤.png'))


