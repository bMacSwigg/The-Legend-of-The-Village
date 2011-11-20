import pygame, sys, os, random, math
from pygame.locals import *

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', name
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

class Player:
    def __init__(self):
            self.health = 10
            
class Enemy:
    def __init__(self, health, num):
            self.health = health
            self.image = load_image("Enemy" + str(num) + ".png", -1)[0]
            self.rect = self.image.get_rect()

def background():
    background = load_image("backgroundmap.png")[0]
    screen.blit(background, (0, 0))
    pygame.display.update()

def enterArea():
    global n
    global imagefight
    imagefight = load_image("back" + str(n) + ".png")[0]
    screen.blit(imagefight, (0, 0))
    pygame.display.update()

def highlightgen():
    global n
    screen.fill((0, 0, 0))
    background = load_image("backgroundmap" + str(n) + ".png")[0]
    screen.blit(background, (0, 0))
    hundreds = math.floor(kills/100)
    tens = math.floor((kills-100*hundreds)/10)
    ones = (kills-100*hundreds)-10*tens
    hundredsImage = load_image(str(int(hundreds)) + ".png", -1)[0]
    tensImage = load_image(str(int(tens)) + ".png", -1)[0]
    onesImage = load_image(str(int(ones)) + ".png", -1)[0]
    levelImage = load_image(str(level) + ".png", -1)[0]
    screen.blit(hundredsImage, (470, 490))
    screen.blit(tensImage, (480, 490))
    screen.blit(onesImage, (490, 490))
    screen.blit(levelImage, (490, 475))
    pygame.display.update()

def equateHealth(bg=None):
    global EnemyHealth
    global PlayerHealth
    global n
    global half
    if END == False:
        background = load_image("back" + str(n) + ".png")[0]
    else:
        background = load_image(bg)[0]
    half = load_image("half.png", -1)[0] 
    PHImage = load_image(str(int(math.floor(PlayerHealth))) + ".png", -1)[0]
    EHImage = load_image(str(int(math.floor(EnemyHealth))) + ".png", -1)[0]
    PHRect = PHImage.get_rect()
    EHRect = EHImage.get_rect()
    screen.blit(background, (0, 0))
    screen.blit(PHImage, (118, 22))
    screen.blit(EHImage, (450, 22))
    if level >= 2:
        Fire = load_image("FireSpell.png", -1)[0]
        screen.blit(Fire, (32, 138))
    if level >= 3:
        Storm = load_image("StormSpell.png", -1)[0]
        screen.blit(Storm, (45, 138))
    if level >= 4:
        Earth = load_image("EarthSpell.png", -1)[0]
        screen.blit(Earth, (59, 138))
    if level >= 5:
        Water = load_image("WaterSpell.png", -1)[0]
        screen.blit(Water, (73, 138))
    if EnemyHealth != math.floor(EnemyHealth):
        screen.blit(half, (460, 22))
    if PlayerHealth != math.floor(PlayerHealth):
        screen.blit(half, (138, 22))
    pygame.display.update()

def StartCutScene():
    global cutscene
    checked = 0
    background = load_image("ElderCutScene.png")[0]
    screen.blit(background, (0, 0))
    pygame.display.update()
    cutscene = 1
    while checked == 0:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_q:
                    highlightgen()
                    checked = 1

def checkCutScene():
    global fight
    global n
    global cutscene
    goBack = False
    if n != 2 and cutscene == 0:
        print("There seems to be carnage everywhere, and you are reluctant to enter. The village a little ways away looks like it might be a bit more exciting, though.")
    elif n == 2 and cutscene == 0:
        StartCutScene()
    elif n == 1 and level1 == True:
        Cleared1 = load_image("Cleared1.png")[0]
        screen.blit(Cleared1, (0, 0))
        pygame.display.update()
        while goBack == False:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_q:
                        goBack = True
    elif n == 2 and level2 == True:
        Cleared2 = load_image("Cleared2.png")[0]
        screen.blit(Cleared2, (0, 0))
        pygame.display.update()
        while goBack == False:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_q:
                        goBack = True
    elif n == 3 and level3 == True:
        Cleared3 = load_image("Cleared3.png")[0]
        screen.blit(Cleared3, (0, 0))
        pygame.display.update()
        while goBack == False:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_q:
                        goBack = True
    elif n == 4 and level4 == True:
        Cleared4 = load_image("Cleared4.png")[0]
        screen.blit(Cleared4, (0, 0))
        pygame.display.update()
        while goBack == False:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_q:
                        goBack = True
    else:
        enterArea()
        fight = True

def levelClear():
    global n
    global level1
    global level2
    global level3
    global level4
    if n == 1:
        level1 = True
    elif n == 2:
        level2 = True
    elif n == 3:
        level3 = True
    elif n == 4:
        level4 = True

def show_Basic():
    basicNotice = load_image("Minion.png")[0]
    screen.blit(basicNotice, (357, 130))
    pygame.display.update()

def show_Boss():
    BossNotice = load_image("BOSS.png")[0]
    screen.blit(BossNotice, (357, 130))
    pygame.display.update()

def intro():
    MFG = load_image("MFG.png")[0]
    screen.blit(MFG, (0, 0))
    pygame.display.update()
    pygame.time.wait(5000)
    Presents = load_image("Presents.png")[0]
    screen.blit(Presents, (0, 0))
    pygame.display.update()
    pygame.time.wait(2000)
    LotV = load_image("Legendofthevillage.png")[0]
    screen.blit(LotV, (0, 0))
    pygame.display.update()
    pygame.time.wait(5000)
    

def start():
    global PC
    global background
    global screen
    global fight
    global n
    global level
    global kills
    global cutscene
    global level1
    global level2
    global level3
    global level4
    global END
    global waiting
    global continued
    global damage
    global PlayerHealth
    global EnemyHealth
    global toCredits
    startAgain = False
    toCredits = False
    continued = False
    waiting = False
    END = False
    level1 = False
    level2 = False
    level3 = False
    level4 = False
    cutscene = 0
    kills = 0
    level = 1
    screen = pygame.display.set_mode((500, 500))
    PC = Player()
    fight = False
    n = 1
    intro()
    background()
    while END == False:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
        if level1 == True and level2 == True and level3 == True and level4 == True:
            print("You won!")
        if fight == False:
            highlightgen()
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_w:
                        n += 1
                        if n > 4:
                            n = 1
                    if event.key == K_s:
                        n -= 1
                        if n < 1:
                            n = 4
                    if event.key == K_e:
                        checkCutScene()
                    if event.key == K_h:
                        helped = False
                        Instructions = load_image("Instructions.png")[0]
                        screen.blit(Instructions, (0, 0))
                        pygame.display.update()
                        while helped == False:
                            for event in pygame.event.get():
                                if event.type == KEYDOWN:
                                    if event.key == K_q:
                                        highlightgen()
                                        helped = True
        elif fight == True:
            battle(n)
    CutScene2 = load_image("ElderCutScene2.png")[0]
    screen.blit(CutScene2, (0, 0))
    pygame.display.update()
    while waiting == False:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_q:
                    Abyss = load_image("backgroundmapAbyss.png")[0]
                    screen.blit(Abyss, (0, 0))
                    pygame.display.update()
                    waiting = True
    while continued == False:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_e:
                    BattleBackground = load_image("FinalBattle.png")[0]
                    screen.blit(BattleBackground, (0, 0))
                    pygame.display.update()
                    eturn = 0
                    damage = 0
                    PlayerHealth = 22
                    EnemyHealth = 20
                    equateHealth("FinalBattle.png")
                    while EnemyHealth > 0 and PlayerHealth > 0:
                        while eturn == 0:
                            for event in pygame.event.get():
                                if event.type == KEYDOWN:
                                    if event.key == K_1:
                                        damage = 1
                                        eturn = 1
                                    elif event.key == K_2:
                                        if level > 1:
                                            damage = random.choice((1, 1.5, 2, 2.5))
                                            eturn = 1
                                    elif event.key == K_3:
                                        if level > 2:
                                            damage = random.choice((2, 2.5, 3, 3.5))
                                            eturn = 1
                                    elif event.key == K_4:
                                        if level > 3:
                                            damage = random.choice((3, 3.5, 4))
                                            eturn = 1
                                    elif event.key == K_5:
                                        if level > 4:
                                            damage = random.choice((3.5, 4, 4.5, 5))
                                            eturn = 1
                        EnemyHealth -= damage
                        a = 2
                        b = 5
                        Pdamage = random.randint(a, b)
                        PlayerHealth -= Pdamage
                        eturn = 0
                        if PlayerHealth < 0:
                            PlayerHealth = 0
                        elif EnemyHealth < 0:
                            EnemyHealth = 0
                        equateHealth("FinalBattle.png")
                    if EnemyHealth <= 0:
                        GameVictory = load_image("GameVictory.png")[0]
                        screen.blit(GameVictory, (0, 0))
                        pygame.display.update()
                        while continued == False:
                            for event in pygame.event.get():
                                if event.type == KEYDOWN:
                                    if event.key == K_q:
                                        continued = True
                    elif PlayerHealth <= 0:
                        Loss = load_image("Loss.png")[0]
                        screen.blit(Loss, (0, 0))
                        pygame.display.update()
                        while startAgain == False:
                            for event in pygame.event.get():
                                if event.type == KEYDOWN:
                                    if event.key == K_q:
                                        Abyss = load_image("backgroundmapAbyss.qpng")[0]
                                        screen.blit(CutScene2, (0, 0))
                                        pygame.display.update
                                        startAgain = True
    ECS = load_image("EndCutScene.png")[0]
    screen.blit(ECS, (0, 0))
    pygame.display.update()
    while toCredits == False:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_q:
                    toCredits = True
    Credits = load_image("Credits.png")[0]
    screen.blit(Credits, (0, 0))
    pygame.display.update()

def battle(num):
    global level
    global damage
    global fight
    global EnemyHealth
    global PlayerHealth
    global kills
    global END
    backToMap = False
    damage = 0
    t = 0
    OppChance = random.choice(("basic", "basic", "basic", "basic", "basic", "basic", "basic", "basic", "boss", "boss",))
    if OppChance == "boss":
        EnemyHealth = 10 + (4*n-4) - (n-1)
        PlayerHealth = 10 + 3*(level-1) + int(math.ceil((1/2)*(level-1)))
        equateHealth()
        show_Boss()
        while EnemyHealth > 0 and PlayerHealth > 0:
            while t == 0:
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if event.key == K_1:
                            damage = 1
                            t = 1
                        elif event.key == K_2:
                            if level > 1:
                                damage = random.choice((1, 1.5, 2, 2.5))
                                t = 1
                        elif event.key == K_3:
                            if level > 2:
                                damage = random.choice((2, 2.5, 3, 3.5))
                                t = 1
                        elif event.key == K_4:
                            if level > 3:
                                damage = random.choice((3, 3.5, 4))
                                t = 1
                        elif event.key == K_5:
                            if level > 4:
                                damage = random.choice((3.5, 4, 4.5, 5))
                                t = 1
                        EnemyHealth -= damage
            a = 0 + (n-1)
            b = 2 + (n-1)
            Pdamage = random.randint(a, b)
            PlayerHealth -= Pdamage
            t = 0
            if PlayerHealth < 0:
                PlayerHealth = 0
            if EnemyHealth < 0:
                EnemyHealth = 0
            equateHealth()
            show_Boss()
        if EnemyHealth <= 0:
            BossVictory = load_image("BossVictory.png")[0]
            screen.blit(BossVictory, (0, 0))
            pygame.display.update()
            level += 1
            if level == 5:
                END = True
            levelClear()
        elif PlayerHealth <= 0:
            Loss = load_image("Loss.png")[0]
            screen.blit(Loss, (0, 0))
            pygame.display.update()
        while backToMap == False:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_q:
                        backToMap = True

    elif OppChance == "basic":
        EnemyHealth = 10 + 2*n-2
        PlayerHealth = 10 + 3*(level-1)
        equateHealth()
        show_Basic()
        while EnemyHealth > 0 and PlayerHealth > 0:
            while t == 0:
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if event.key == K_1:
                            damage = 1
                            t = 1
                        elif event.key == K_2:
                            if level > 1:
                                damage = random.choice((1, 1.5, 2, 2.5))
                                t = 1
                        elif event.key == K_3:
                            if level > 2:
                                damage = random.choice((2, 2.5, 3, 3.5))
                                t = 1
                        elif event.key == K_4:
                            if level > 3:
                                damage = random.choice((3, 3.5, 4))
                                t = 1
                        elif event.key == K_5:
                            if level > 4:
                                damage = random.choice((3.5, 4, 4.5, 5))
                                t = 1
                        EnemyHealth -= damage
            a = 0
            b = 2
            Pdamage = random.randint(a, b)
            PlayerHealth -= Pdamage
            t = 0
            if PlayerHealth < 0:
                PlayerHealth = 0
            if EnemyHealth < 0:
                EnemyHealth = 0
            equateHealth()
            show_Basic()
        if EnemyHealth <= 0:
            MinionVictory = load_image("MinionVictory.png")[0]
            screen.blit(MinionVictory, (0, 0))
            pygame.display.update()
            kills += 1
            if kills > 999:
                kills = 999
        elif PlayerHealth <= 0:
            Loss = load_image("Loss.png")[0]
            screen.blit(Loss, (0, 0))
            pygame.display.update()
        while backToMap == False:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_q:
                        backToMap = True
    highlightgen()
    fight = False

start()
