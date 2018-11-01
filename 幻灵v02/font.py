import pygame

pygame.font.init()
White = (255,255,255)
fontObj = pygame.font.Font('FZLTCXHJW.ttf',20)
fontHP = fontObj.render('血:',False,White,None)
fontMP = fontObj.render('魔:',False,White,None)
fontSTR = fontObj.render('力:',False,White,None)
fontDFE = fontObj.render('防:',False,White,None)
fontWIS = fontObj.render('技:',False,White,None)
fontRage = fontObj.render('怒:',False,White,None)

saber_attack = fontObj.render('攻击', False, White, None)
saber_skill1 = fontObj.render('旋光', False, White, None)
saber_skill2 = fontObj.render('穿心', False, White, None)
saber_skill3 = fontObj.render('强化攻击', False, White, None)
saber_skill4 = fontObj.render('强化防御', False, White, None)
saber_skill5 = fontObj.render('强化技能', False, White, None)
saber_skill6 = fontObj.render('回复', False, White, None)


