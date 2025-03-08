import pygame,sys,time,math,unit,Map_editor,MV
from pygame.locals import*

def check_obj(obj):
    if(type(obj)==type(1)):
        return False
    else:
        return True
    
def search(cord):
    for x in range(0,8):
        obj_lst =[P1[x],P2[x]]
        for obj in obj_lst:
            if (type(obj)!=int):
                if (cord == obj.axis):
                    return obj
    return 0
    
def isvacant(cord):
    for x in range(0,8):
        obj_lst =[P1[x],P2[x]]
        for obj in obj_lst:
            if (type(obj)!=int):
                if (cord == obj.axis):
                    return False
    return True

def check(cord,test_obj):
    if (CMAP[cord[0]][cord[1]] == CMAP[i][j]) and (MAIN_RENDER[cord[0]][cord[1]] == test_obj):
        return False
    return True   
            

            
def Quit(event):
    global Loop
    if event.type == QUIT:
        return True
    elif event.type == KEYDOWN:
        if event.key == K_ESCAPE:
            Loop = 0
        return False
    else:
        return False

def Render_map(MAP):
    count = 0
    global MAPL
    temp = []
    MAPL = []
    for x in MAP.split():
        if x == 'e':
            MAPL +=[temp]
            temp = []
            continue
        temp += [x]
    RENDER = []
    for x in range(0,len(MAPL)):
        RENDER += [[]]
        for y in range(0,len(MAPL[0])):
            if MAPL[x][y] == '0':
                RENDER[x] += [SmlGrass]
            elif MAPL[x][y] == '1':
                RENDER[x] += [BigGrass]
            elif MAPL[x][y] == '2':
                RENDER[x] += [Rock]
            elif MAPL[x][y] == '3':
                RENDER[x] += [Bush]
            elif MAPL[x][y] == '4':
                RENDER[x] += [Tree]
            elif MAPL[x][y] == '9':
                RENDER[x] += [Clear]

    return RENDER

def rec_boxsml(x, y, ch, i, j, s1, s2):
    pygame.draw.rect(DISPLAYSURF,WHITE, (x, y, s1, s2),2,4)
    textSurfaceObj = smlfontObj.render(ch, True, WHITE)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (i, j)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
def rec_box(x, y, ch, i, j, s1, s2):
    pygame.draw.rect(DISPLAYSURF,WHITE, (x, y, s1, s2),2,4)
    textSurfaceObj = subfontObj.render(ch, True, WHITE)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (i, j)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
def rec_boxsub(x, y, ch, i, j, s1, s2):
    pygame.draw.rect(DISPLAYSURF,WHITE, (x, y, s1, s2),2,4)
    textSurfaceObj = subfontObj.render(ch, True, WHITE)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (i, j)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    
def display_weapon(i, x, y, z, w):
            if i[3]=='':
                textSurfaceObj = subfontObj.render(str(i[2]), True, WHITE)
                textRectObj = textSurfaceObj.get_rect()
                textRectObj.center = (x, y)
            else:
                textSurfaceObj = subfontObj.render(str(i[3]), True, WHITE)
                if (i[4][2]==3)and(i[3]=='SOILDER'):
                    weponSurfaceObj = smlfontObj.render('AK-47', True, WHITE)
                elif (i[4][2]==4)and(i[3]=='SOILDER'):
                    weponSurfaceObj = smlfontObj.render('M16', True, WHITE)
                elif (i[4][2]==5)and(i[3]=='TANK'):
                    weponSurfaceObj = smlfontObj.render('50.calMG', True, WHITE)
                elif (i[4][2]==5)and(i[3]=='SOILDER'):
                    weponSurfaceObj = smlfontObj.render('AWM', True, WHITE)
                elif (i[4][2]==6)and(i[3]=='TANK'):
                    weponSurfaceObj = smlfontObj.render('CANNON', True, WHITE)
                elif (i[4][2]==8)and(i[3]=='none'):
                    weponSurfaceObj = smlfontObj.render('none', True, WHITE)
                elif (i[4][2]==9 and (i[3]=='none')):
                    weponSurfaceObj = smlfontObj.render('none', True, WHITE)
                else:
                    weponSurfaceObj = smlfontObj.render('none', True, WHITE)
                    
                weponRectObj = weponSurfaceObj.get_rect()
                weponRectObj.center = (x, z)
                DISPLAYSURF.blit(weponSurfaceObj, weponRectObj)
                
                textRectObj = textSurfaceObj.get_rect()
                textRectObj.center = (x, w)
                DISPLAYSURF.blit(textSurfaceObj, textRectObj)
#-------------------------------------------------------variables--------------------------------
Map_editor.makemap()

BLUE = ( 0, 0, 255)
GREEN = ( 0, 128, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = ( 0, 0, 0)
BGCOLOR = WHITE

Empty = pygame.image.load('img\\empty.png')
Tile = pygame.image.load('img\\Tile.png')
Heart = pygame.image.load('img\\Heart.png')
SmlGrass = pygame.image.load('img\\SmlGrass.png')
BigGrass = pygame.image.load('img\\BigGrass.png')
Bush = pygame.image.load('img\\Bush.png')
Tree = pygame.image.load('img\\Tree.png')
Rock = pygame.image.load('img\\Rock.png')
Clear = pygame.image.load('img\\Clear.png')
Soilder = pygame.image.load('img\\Soilder.png')
Tank = pygame.image.load('img\\Tank.png')
Soilder2 = pygame.image.load('img\\Soilder2.png')
Tank2 = pygame.image.load('img\\Tank2.png')
Tstate = 0


END = False
TURN = 0
FPS = 30
WIDTH =1550
HEIGHT = 800
MPWIDTH = 1000
MPHEIGHT = 1100
LOWERMARGIN = 5
X_AXIS = 0
Y_AXIS = 0
CMAP = []
Loop = 0
player = 0
next_pos = [0,0]
select = [0,0]
mv_map = []
P1 =[1,2,3,4,5,6,7,8]
P2 =[9,10,11,12,13,14,15,16]
UMAP = [[[475,75,0,'',[0,0,0],0,P1[0]],[625,75,1,'',[0,0,0],0,P1[1]],[775,75,2,'',[0,0,0],0,P1[2]],[925,75,3,'',[0,0,0],0,P1[3]],[475,275,4,'',[0,0,0],0,P1[4]],[625,275,5,'',[0,0,0],0,P1[5]],[775,275,6,'',[0,0,0],0,P1[6]],[925,275,7,'',[0,0,0],0,P1[7]]],[[475,75,0,'',[0,0,0],0,P2[0]],[625,75,1,'',[0,0,0,0],0,P2[1]],[775,75,2,'',[0,0,0],0,P2[2]],[925,75,3,'',[0,0,0],0,P2[3]],[475,275,4,'',[0,0,0],0,P2[4]],[625,275,5,'',[0,0,0],0,P2[5]],[775,275,6,'',[0,0,0],0,P2[6]],[925,275,7,'',[0,0,0],0,P2[7]]]]
PMAP = [[50, 500,0,'SOILDER',0],[50, 575,1,'TANK',0],[50, 500,2,'AK-47',1],[50, 575,3,'M16',1],[50, 650,4,'AWM',1],[50, 500,5,'CANNON',2],[50, 575,6,'50.calMG',2]]
BMAP = [[1025,700,"NEXT TURN"]]#side bar
start_prom = 'PLEASE SELECT A UNIT AND SELECT ITS WEAPON IN USE.'
unit_renderx = 0
unit_rendery = 0
G_state = [[0,0],[0,0]]

Z = 25
A = int(Z*(0.750111069))
B = int(Z*(0.661311865))
X_GAP = 2*(Z+B)
Y_GAP = 2*A


Mfile = open("maps\\G_MAP.txt","r")
MAP = Mfile.read()
Mfile.close()
MAIN_RENDER = Render_map(MAP)
#----------------------------------------objects_pygame--------------------------------------------------------------
pygame.init()

MV.set_variables(P1,P2)
DISPLAYSURF = pygame.display.set_mode((WIDTH,HEIGHT))
FPSCLOCK = pygame.time.Clock()
fontObj = pygame.font.Font('freesansbold.ttf', 50)
subfontObj = pygame.font.Font('freesansbold.ttf', 25)
smlfontObj = pygame.font.Font('freesansbold.ttf', 16)
MV = MV.movement()
#------------------------------world map --------------------------------------------------------------------
while True:
    while Loop == 1:
        if END == True:
            break
        pygame.time.wait(100)
        DISPLAYSURF.fill(BLACK)
        CMAP = []
        count= 0
        #Movement
        
        #map rendering
        for y in range(0,MPHEIGHT,X_GAP):
            CMAP += [[]]
            for x in range(0,MPWIDTH,Y_GAP):
                CMAP[count] += [[x+X_AXIS,y+Y_AXIS]]
            count += 1
            CMAP += [[]]
            for i in range(0,MPWIDTH-Y_GAP,Y_GAP):
                CMAP[count] += [[i+A+X_AXIS,y+Z+B+Y_AXIS]]
            count += 1


        for x in range(0,((MPHEIGHT//X_GAP))*2):
            for y in range(0,(MPWIDTH//Y_GAP)):
                DISPLAYSURF.blit(MAIN_RENDER[x][y],CMAP[x][y])

                
        for x in mv_map:
            if((26>x[0]>-1)and(27>x[1]>-1)):
                DISPLAYSURF.blit(Clear,CMAP[x[0]][x[1]])
 
        for x in range(0,8):
            obj_lst =[P1[x],P2[x]]
            for obj in obj_lst:
                unit_renderx = X_AXIS
                unit_rendery = Y_AXIS
                if (check_obj(obj)and (obj.stat[0]>0)):
                    unit_renderx += obj.axis[0] 
                    unit_rendery += obj.axis[1]
                    DISPLAYSURF.blit(obj.self_obj,(unit_renderx,unit_rendery))
                else:
                    obj = 0
                    
        # draw side bar       
        pygame.draw.rect(DISPLAYSURF,WHITE, (1000, 25, 525, 750),2,12)
        
        place = 0
        temp = TURN%2
        for x in UMAP[temp]:
            obj =[P1[place],P2[place]]
            #print(obj[temp])
            if check_obj(obj[temp]):
                pygame.draw.rect(DISPLAYSURF,WHITE, (x[1]+1040, x[0]-400, 125, 130),2,4)

                rec_boxsml(x[1]+1040, x[0]-400, 'ATK', x[1]+1060, x[0]-330, 125, 130)

                rec_boxsml(x[1]+1040, x[0]-400, 'AP', x[1]+1060, x[0]-310, 125, 130)

                rec_boxsml(x[1]+1040, x[0]-400, 'HP', x[1]+1060, x[0]-290, 125, 130)
                        
                for d in range(obj[temp].wepon()[0]):#Dammage painter
                    pygame.draw.rect(DISPLAYSURF,WHITE, (x[1]+1090+(d*13), x[0]-335, 5, 10),0,0)
                            
                for a in range(obj[temp].stat[1]):#armour painter
                    pygame.draw.rect(DISPLAYSURF,WHITE, (x[1]+1090+(a*13), x[0]-315, 5, 10),0,0)

                for h in range(obj[temp].stat[0]):# heart painter
                    DISPLAYSURF.blit(Heart, (x[1]+1080+(h*17), x[0]-318))
                if((obj[temp].self_obj== Soilder)or(obj[temp].self_obj== Soilder2)):
                    rec_box(x[1]+1040, x[0]-400, 'SOILDER', x[1]+1100, x[0]-370, 125, 130)
                else:
                    rec_box(x[1]+1040, x[0]-400, 'TANK', x[1]+1100, x[0]-370, 125, 130)
                    
            place += 1
            
        for x in BMAP:# side bar text and boxes
            rec_box(x[0],x[1], x[2], x[0]+235, x[1]+25, 475, 50)
        textSurfaceObj = subfontObj.render(('TURN OF PLAYER '+str(TURN%2+1)+" Turn("+str(TURN)+")"), True, WHITE)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (1275, 50)
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)
            
        for event in pygame.event.get():# Event mannager for LOOP 1
                
            END = Quit(event) #SILPE CODE TO EXIT TO MAINMENU WHEN ESC IS PREESED OR CLOSE THE WONDOW
            
            if event.type == KEYDOWN:
                if (event.key == 119):#up
                    Y_AXIS += 40
                if (event.key == 115):#down
                    Y_AXIS -= 40
                '''if (event.key == 100):#left
                    X_AXIS += 40
                if (event.key == 97):#right
                    X_AXIS -= 40'''
            elif event.type == MOUSEBUTTONDOWN:
                pos = event.pos
                if(event.button == 1):
                    if (1025<pos[0]<1500)and(700<pos[1]<750):
                        for i in range(8):
                            try:
                                P1[i].setplaced(True)
                                P2[i].setplaced(True)
                            except:
                                pass
                        TURN += 1
                        mv_map = []
                        pygame.draw.rect(DISPLAYSURF,WHITE, (x[0], x[1], 475, 50),0,12)
                    X=pos[0]
                    Y=pos[1]
#------------------------------------------------------------------click and move-------------------------------------------------------------------------------------
                    for i in range(len(CMAP)):
                        for j in range(len(CMAP[i])):
                            if ((i!=0) and (j!=0)):
                                k=CMAP[i][j][0]
                                l=CMAP[i][j][1]
                                if((X>k-A)and(X<k+A)and((Y-l-(Z/2)-B) <= -((B/A)*(X-k)))and((Y-l+(Z/2)+B)>=(-(B/A)*(X-k)))and((Y-l+(Z/2)+B)>=((B/A)*(X-k)))and((Y-l-(Z/2)-B)<=((B/A)*(X-k)))):

                                    if(TURN%2 == 0):
                                        Pl_obj = P1[Tstate]
                                    else:
                                        Pl_obj = P2[Tstate]
#---------------------------------------------------------------------------------------------------------------------
                                    if troop_select == True:
                                        mv_map = MV.move_map(i,j,Pl_obj)

#-----------------------------------------------------------------------------------------------------------------------
                                    if(i%2!=0):    
                                        DISPLAYSURF.blit(Tile, CMAP[i-1][j])
                                        next_pos[0] = [CMAP[i-1][j][0]-X_AXIS,CMAP[i-1][j][1]-Y_AXIS]
                                        
                                        if TURN == 0 or TURN == 1:
                                            G_state[0][1] = (MAIN_RENDER [i-1][j] == Clear)
                                        else:
                                            G_state[0][1] = True
                                            G_state[0][0] = True
                                    else:
                                        DISPLAYSURF.blit(Tile, CMAP[i-1][j-1])
                                        next_pos[1] = [CMAP[i-1][j-1][0]-X_AXIS,CMAP[i-1][j-1][1]-Y_AXIS]
                                        
                                        if TURN == 0 or TURN == 1:
                                            G_state[0][0] = (MAIN_RENDER [i-1][j-1] == Clear)
                                        else:
                                            G_state[0][0] = True
                                            G_state[0][1] = True
#------------------------------------------------------------------------------------------------------------------------    
                                    if (i%2 == 1) and (G_state[0][1]):
                                        if not (isvacant (next_pos[0])):
                                            if (MV.isenemy(TURN,search(next_pos[0]))and (MV.is_in_mv_map(mv_map,[i-1,j],Pl_obj))and (Pl_obj.placed)):
                                                temp = MV.enemy(TURN,search(next_pos[0]))
                                                temp.damage(temp.wepon()[0])
                                                Pl_obj.setplaced(False)
                                            print(Pl_obj)
                                            Tstate = MV.search_tile(Tstate,next_pos[0])
                                            Pl_obj = search(next_pos[0])
                                            mv_map = MV.move_map(i,j,Pl_obj)
                                        if (isvacant (next_pos[0]))and (type(Pl_obj)!=int)and (MV.is_in_mv_map(mv_map,[i-1,j],Pl_obj)and (Pl_obj.placed)):
                                            if Pl_obj.axis != next_pos[0]:
                                                Pl_obj.setplaced(False)
                                            Pl_obj.setaxis(next_pos [0])
                                            mv_map = MV.move_map(i,j,Pl_obj)
                                            break
                                        
                                        
                                            
                                    elif (i%2 == 0)and (G_state[0][0]):
                                        if not (isvacant (next_pos[1])):
                                            if (MV.isenemy(TURN,search(next_pos[1]))and (MV.is_in_mv_map(mv_map,[i-1,j-1],Pl_obj))and (Pl_obj.placed)):
                                                temp = MV.enemy(TURN,search(next_pos[1]))
                                                temp.damage(temp.wepon()[0])
                                                Pl_obj.setplaced(False)
                                            print(Pl_obj)
                                            Tstate = MV.search_tile(Tstate,next_pos[1])
                                            Pl_obj = search(next_pos[1])
                                            mv_map = MV.move_map(i,j,Pl_obj)
                                        if (isvacant (next_pos [1]))and (type(Pl_obj)!=int)and (MV.is_in_mv_map(mv_map,[i-1,j-1],Pl_obj)and (Pl_obj.placed)):
                                            if Pl_obj.axis != next_pos[1]:
                                                Pl_obj.setplaced(False)
                                            Pl_obj.setaxis(next_pos [1])
                                            mv_map = MV.move_map(i,j,Pl_obj)
                                            break
                                        
                                        
                                            
                                    #clicked on center cord [k,l] or CMAP[i][j] tile name (i,j),gives at start pos [0,0]
                                            
                    for x in UMAP[TURN%2]:
                        if (x[1]+1040<pos[0]<x[1]+1165) and (x[0]-400< pos[1] <x[0]-270) :
                            pygame.draw.rect(DISPLAYSURF,WHITE, (x[1]+1040, x[0]-400, 125, 130),0,4)
                            Tstate = x[2]
                            troop_select = True
                            break
                        else:
                            troop_select = False
        pygame.display.update()
        FPSCLOCK.tick(FPS)

#------------------------------------------------main menu-------------------------------------------------------------        
    CMAP = [[600,250],[600,400],[600,550]]
    while Loop == 0:
        if END == True:
            break
        DISPLAYSURF.fill(BLACK)
        count = 0
        for x in CMAP:
            pygame.draw.rect(DISPLAYSURF,WHITE, (x[0], x[1], 300, 100),2,12)
            if count == 0:
                textSurfaceObj = fontObj.render('PLAYER 1', True, WHITE)
            elif count == 1:
                textSurfaceObj = fontObj.render('PLAYER 2', True, WHITE)
            else:
                textSurfaceObj = fontObj.render('PLAY', True, WHITE)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (x[0]+150, x[1]+50)
            DISPLAYSURF.blit(textSurfaceObj, textRectObj)
            count += 1

        for event in pygame.event.get(): #event mannager for LOOP 0

            END = Quit(event)
            
            if event.type == MOUSEBUTTONDOWN:
                if (event.button == 1)and(600<event.pos[0]<900)and((250<event.pos[1]<350)or(400<event.pos[1]<500)):
                    Loop = 2
                    if(250<event.pos[1]<350):
                        player = 0
                    elif(400<event.pos[1]<500):
                        player = 1
                if (event.button == 1)and(600<event.pos[0]<900)and(550<event.pos[1]<650):
                    Loop = 1
                    TURN = 0
        pygame.display.update()
        FPSCLOCK.tick(FPS)

#-----------------------------------player 1&2 unit selection-----------------------------------------------------
    mode = 0
    while Loop == 2:
        if END == True:
            break
        DISPLAYSURF.fill(BLACK)
        count = 0
        if mode == 0:
            rec_boxsub(25, 475, start_prom, 25+750, 475+150, 1500, 300)
        elif mode == 2:# soilder weapon
            pygame.draw.rect(DISPLAYSURF,WHITE, (25, 475, 1500, 300),2,4)
            for y in PMAP:
                if y[4]==1:
                    rec_boxsub(y[0], y[1], y[3], y[0]+335, y[1]+25, 675, 50)

        elif mode == 3:# tank weapon
            pygame.draw.rect(DISPLAYSURF,WHITE, (25, 475, 1500, 300),2,4)
            for y in PMAP:
                if y[4]==2:
                    rec_boxsub(y[0], y[1], y[3], y[0]+335, y[1]+25, 675, 50)
                        
            #  unit cards ----------->
        for x in UMAP[player]:# card stats print --->

            rec_boxsml(x[0], x[1], 'ATK', x[0]+20, x[1]+ 105, 125, 175)

            rec_boxsml(x[0], x[1], 'AP', x[0]+20, x[1]+ 130, 125, 175)

            rec_boxsml(x[0], x[1], 'HP', x[0]+20, x[1]+ 155, 125, 175)

            for d in range(x[4][2]):#Dammage painter
                pygame.draw.rect(DISPLAYSURF,WHITE, (x[0]+50+(d*13), x[1]+ 100, 5, 10),0,0)
            for a in range(x[4][1]):#armour painter
                pygame.draw.rect(DISPLAYSURF,WHITE, (x[0]+50+(a*13), x[1]+ 125, 5, 10),0,0)

            for h in range(x[4][0]):# heart painter
                DISPLAYSURF.blit(Heart, (x[0]+40+(h*17), x[1]+ 125))
                
            display_weapon(x, x[0]+65, x[1]+50, x[1]+60, x[1]+34) #wepon equiped teller <<--------------
            
            count += 1
#------------------------------------units----------------------------------------------
        if mode == 1:
            pygame.draw.rect(DISPLAYSURF,WHITE, (25, 475, 1500, 300),2,4)
            for y in PMAP:
                if(y[4]==0):
                    rec_boxsub(y[0], y[1], y[3], y[0]+337, y[1]+25, 675, 50) # soilder & tank
        
        for event in pygame.event.get():# event mannager for LOOP 2
            
            END = Quit(event)
            
            if event.type == MOUSEBUTTONDOWN:
                if (event.button == 1):
                    pos = event.pos
                    for x in UMAP[player]:#selection screen of unit type
                        if (x[0]<pos[0]<(x[0]+125))and(x[1]<pos[1]<(x[1]+175)):
                            pygame.draw.rect(DISPLAYSURF,WHITE, (x[0], x[1], 125, 175),0,4)
                            if player == 0:
                                P1[x[2]] = unit.Unit(x[2],Empty,[0,0,0],[0,0],[-40,-40],True)
                                select = [1,x[2]]
                            elif player == 1:
                                P2[x[2]] = unit.Unit(x[2],Empty,[0,0,0],[0,0],[-40,-40],True)
                                select = [2,x[2]]
                            mode = 1
                            
                    if (mode == 1):#set unit type
                        for x in PMAP:
                            if (x[4]==0):
                                if((x[0]<pos[0]<x[0]+675)and(x[1]<pos[1]<x[1]+50)):
                                    pygame.draw.rect(DISPLAYSURF,WHITE, (x[0], x[1], 675, 50),0,4)
                                    UMAP[player][select[1]][3]=x[3]
                                    if x[3] == 'SOILDER':
                                        UMAP[player][select[1]][4][0]=2
                                        UMAP[player][select[1]][4][1]=1
                                        UMAP[player][select[1]][4][2]=0
                                        if select[0] == 1:
                                            P1[select[1]].setstat([2,4,2])
                                            P1[select[1]].setself_obj(Soilder)
                                        elif select[0] == 2:
                                            P2[select[1]].setstat([2,4,2])# [health,armour,speed]
                                            P2[select[1]].setself_obj(Soilder2)
                                        mode = 2
                                    elif x[3] == 'TANK':
                                        UMAP[player][select[1]][4][0]=4
                                        UMAP[player][select[1]][4][1]=4
                                        UMAP[player][select[1]][4][2]=0
                                        if select[0] == 1:
                                            P1[select[1]].setstat([4,4,4])
                                            P1[select[1]].setself_obj(Tank)
                                        elif select[0] == 2:
                                            P2[select[1]].setstat([4,4,4])# [health,armour,speed]
                                            P2[select[1]].setself_obj(Tank2)
                                        mode = 3
                    elif (mode == 2):# weapon selection soilder
                        for x in PMAP:
                            if(x[4]==1):
                                if((x[0]<pos[0]<x[0]+675)and(x[1]<pos[1]<x[1]+50)):
                                    pygame.draw.rect(DISPLAYSURF,WHITE, (x[0], x[1], 675, 50),0,4)
                                    if (x[3] == 'AK-47'):
                                        UMAP[player][select[1]][4][2] = 3
                                        if select[0] == 1:
                                            P1[select[1]].setwepon([1,2])# [dmg,armour percering]
                                        elif select[0] == 2:
                                            P2[select[1]].setwepon([1,2])
                                        
                                    elif (x[3] == 'M16'):
                                        UMAP[player][select[1]][4][2] = 4
                                        if select[0] == 1:
                                            P1[select[1]].setwepon([1,2])
                                        elif select[0] == 2:
                                            P2[select[1]].setwepon([1,2])
                                        
                                    elif (x[3] == 'AWM'):
                                        UMAP[player][select[1]][4][2] = 5
                                        if select[0] == 1:
                                            P1[select[1]].setwepon([2,3])
                                        elif select[0] == 2:
                                            P2[select[1]].setwepon([2,3])
                                        
                    elif (mode == 3):# wepon selection for tank
                        for x in PMAP:
                            if(x[4]==2):
                                    if((x[0]<pos[0]<x[0]+675)and(x[1]<pos[1]<x[1]+50)):
                                        pygame.draw.rect(DISPLAYSURF,WHITE, (x[0], x[1], 675, 50),0,4)
                                        if (x[3] == 'CANNON'):
                                            UMAP[player][select[1]][4][2] = 6
                                            if select[0] == 1:
                                                P1[select[1]].setwepon([3,3])# [dmg,armour percering]
                                            elif select[0] == 2:
                                                P2[select[1]].setwepon([3,3])
                                            
                                        elif (x[3] == '50.calMG'):
                                            UMAP[player][select[1]][4][2] = 5
                                            if select[0] == 1:
                                                P1[select[1]].setwepon([2,5])
                                            elif select[0] == 2:
                                                P2[select[1]].setwepon([2,5])
                                               
        pygame.display.update()
        FPSCLOCK.tick(FPS)
    if END == True:
        pygame.quit()
        sys.exit()
    pygame.display.update()
    FPSCLOCK.tick(FPS)

            
                
