board = []
for i in range(8):
    board.append([]) 
    for j in range(8):
        board[i].append("  ")
def show():
    print('-----------------------------------------')
    for i in range (8):
        print('|', end='')
        for j in range (8):
            print(' '+board[i][j]+' |', end = '')
        row = str(i)
        if len(row) == 1:
            row = "0"+row
        print('', row)
        print('-----------------------------------------')
    print("  A    B    C    D    E    F    G    H ")
board[7][0] = 'wr'
board[7][1] = 'wh'
board[7][2] = 'wb'
board[7][3] = 'wq'
board[7][4] = 'wk'
board[7][5] = 'wb'
board[7][6] = 'wh'
board[7][7] = 'wr'
for i in range(8):
    board[6][i] = 'wp'
board[0][0] = 'br'
board[0][1] = 'bh'
board[0][2] = 'bb'
board[0][3] = 'bq'
board[0][4] = 'bk'
board[0][5] = 'bb'
board[0][6] = 'bh'
board[0][7] = 'br'
for i in range(8):
    board[1][i] = 'bp'
#show()
from itertools import groupby
import math
import random
import pygame
import sys
timer = pygame.time.Clock()
fps = 60
# Initialize pygame
pygame.init()
font = pygame.font.SysFont('Arial', 30)
font1 = pygame.font.SysFont('Arial', 25)
# Define constants
WIDTH, HEIGHT = 1000,800
SQUARE_SIZE = 800 // 8
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (80, 200, 120)
# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chessboard")
piecew = []
pieceb = []
s = []
bq = pygame.image.load('C:\\Users\\thest\\Downloads\\bq.png') #make sure to change all the file direction for all of the images 
bq = pygame.transform.scale(bq, (80, 80))
bk = pygame.image.load('C:\\Users\\thest\\Downloads\\bk.png')
bk = pygame.transform.scale(bk, (80, 80))
br = pygame.image.load('C:\\Users\\thest\\Downloads\\br.png')
br = pygame.transform.scale(br, (80, 80))
bb = pygame.image.load('C:\\Users\\thest\\Downloads\\bb.png')
bb = pygame.transform.scale(bb, (80, 80))
bh = pygame.image.load('C:\\Users\\thest\\Downloads\\bh.png')
bh = pygame.transform.scale(bh, (80, 80))
bp = pygame.image.load('C:\\Users\\thest\\Downloads\\bp.png')
bp = pygame.transform.scale(bp, (80, 80))
wq = pygame.image.load('C:\\Users\\thest\\Downloads\\wq.png')
wq = pygame.transform.scale(wq, (80, 80))
wk = pygame.image.load('C:\\Users\\thest\\Downloads\\wk.png')
wk = pygame.transform.scale(wk, (80, 80))
wr = pygame.image.load('C:\\Users\\thest\\Downloads\\wr.png')
wr = pygame.transform.scale(wr, (80, 80))
wb = pygame.image.load('C:\\Users\\thest\\Downloads\\wb.png')
wb = pygame.transform.scale(wb, (80, 80))
wh = pygame.image.load('C:\\Users\\thest\\Downloads\\wh.png')
wh = pygame.transform.scale(wh, (80, 80))
wp = pygame.image.load('C:\\Users\\thest\\Downloads\\wp.png')
wp = pygame.transform.scale(wp, (80, 80))
s1 = pygame.image.load('C:\\Users\\thest\\Downloads\\s1.png')
s1 = pygame.transform.scale(s1, (180, 120))
s1d = font1.render("The selected piece, other than queen and king, is invincible, ", True, 'Black')
s1d1 = font1.render("but you can't move it. (It will still be your turn after using this skill)", True, 'Black')
s2 = pygame.image.load('C:\\Users\\thest\\Downloads\\s2.png')
s2 = pygame.transform.scale(s2, (180, 120))
s2d = font1.render("All of your piece will randomly locate in different empty", True, 'Black')
s2d1 = font1.render("spots (this skill is consirder as a round)", True, 'Black')
s3 = pygame.image.load('C:\\Users\\thest\\Downloads\\s3.png')
s3 = pygame.transform.scale(s3, (180, 120))
s3d = font1.render("You can teleport one of your piece to any empty spot; can't not eat a piece (this", True, 'Black')
s3d1 = font1.render("skill is consirder as a round)", True, 'Black')
s4 = pygame.image.load('C:\\Users\\thest\\Downloads\\s4.png')
s4 = pygame.transform.scale(s4, (234, 162))
s4d = font1.render("The selected piece explode itself and destory all pieces ", True, 'Black')
s4d1 = font1.render("within the surrounding 9 blocks (this skill is consirder as a round)", True, 'Black')
s5 = pygame.image.load('C:\\Users\\thest\\Downloads\\s5.png')
s5 = pygame.transform.scale(s5, (180, 120))
s5d = font1.render("Add a round", True, 'Black')
s5d1 = font1.render("", True, 'Black')
s6 = pygame.image.load('C:\\Users\\thest\\Downloads\\s6.png')
s6 = pygame.transform.scale(s6, (180, 120))
s6d = font1.render("Change your queen to king (only available if queen still exit)", True, 'Black')
s6d1 = font1.render("(this skill is consirder as a round)", True, 'Black')
gcm = pygame.image.load('C:\\Users\\thest\\Downloads\\gcm.png')
gcm = pygame.transform.scale(gcm, (180, 120))
for i in (br, bh, bb, bq, bk, bb, bh, br, bp):
    pieceb.append(i)
for i in (wr, wh, wb, wq, wk, wb, wh, wr, wp):
    piecew.append(i)
for i in (s1, s2, s3, s4, s5, s6):
    s.append(i)
sob = [[], [], [], [], [], []]
sobs = [[], [], [], [], [], []]
sobn =[]
sobl = [[800, 0], [800, 100], [800, 200], [800,500], [800, 600], [800,700]]
sl = [[0.5, 0], [0.5, 1.5], [0.5, 3], [0.23, 4], [0.5, 5.5], [0.5,7]]
sd = [s1d, s2d, s3d, s4d, s5d, s6d]
sd1 = [s1d1, s2d1, s3d1, s4d1, s5d1, s6d1]
sdl = [[200, 50], [200, 200], [200, 350], [200, 475], [200, 600], [200,700]]
nos = [1, 1, 1, 1, 1, 1]
wl = [[0, 7], [1, 7], [2, 7], [3, 7], [4, 7], [5, 7], [6, 7], [7, 7], [0, 6], [1, 6], [2, 6], [3, 6], [4, 6], [5, 6], [6, 6], [7, 6]]
bl = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [0, 1], [1,1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1]]
# Main loop
def showboard():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Draw the chessboard
    for row in range(8):
        for col in range(8):
            color = WHITE if (row + col) % 2 == 0 else GREEN
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    pygame.draw.rect(screen, 'light gray', (HEIGHT, HEIGHT-WIDTH, WIDTH, HEIGHT+(WIDTH-HEIGHT)))
    if len(sc) == 6:
        #print(len(sob))
        for i in range (len(sob)):
            #print(i)
            sob[i] = list(set(sob[i]))
            #print(sob)
            try:
                #print(sob[0])
                sob[i][0] = pygame.transform.scale(sob[i][0], (120, 90))
                screen.blit(sob[i][0],  (sobl[i][0], sobl[i][1]))
                img = font.render(str(nos[i]), True, 'Black')
                screen.blit(img,  (sobl[i][0]+100, sobl[i][1]+25))
            except:
                pass
def decision():
    pygame.draw.rect(screen, 'white', [150, 200, 600, 400])
    pygame.draw.rect(screen, 'red', [200, 425, 200, 100])
    pygame.draw.rect(screen, 'green', [500, 425, 200, 100])
    img = font.render('Which game mode would you like!', True, 'Black')
    (img,  (210, 300))
    img = font.render('power chess', True, 'Black')
    screen.blit(img,  (210, 450))
    img = font.render('Click and select 3 skills', True, 'Black')
    screen.blit(img,  (120, 530))
    img = font.render('for each player', True, 'Black')
    screen.blit(img,  (120, 560))
    img = font.render('nomral chess', True, 'Black')
    screen.blit(img,  (510, 450))
def skill(sc):
    sc1 = math.floor((len(sc)-1)/3)*3
    #sc1 = len(sc)-1
    #print(len(sc1)-len(sob))
    for i in range (len(sl)):
        screen.blit(s[i],  (sl[i][0]*100, sl[i][1]*100))
        screen.blit(sd[i],  (sdl[i][0], sdl[i][1]-15))
        screen.blit(sd1[i],  (sdl[i][0], sdl[i][1]+15))
        if 4>len(sc)>0:
                for j in range(len(sc)):
                    if sc[j] < 135:
                        screen.blit(gcm,  (sl[0][0]*100, sl[0][1]*100))
                        sob[sc1+j].append(s1)
                        sobs[sc1+j].append(1)
                    elif sc[j] < 286:
                        screen.blit(gcm,  (sl[1][0]*100, sl[1][1]*100))
                        sob[sc1+j].append(s2)
                        sobs[sc1+j].append(2)
                    elif sc[j] < 417:
                        screen.blit(gcm,  (sl[2][0]*100, sl[2][1]*100))
                        sob[sc1+j].append(s3)
                        sobs[sc1+j].append(3)
                    elif sc[j] < 551:
                        screen.blit(gcm,  (sl[3][0]*100, sl[3][1]*100))
                        sob[sc1+j].append(s4)
                        sobs[sc1+j].append(4)
                    elif sc[j] < 667:
                        screen.blit(gcm,  (sl[4][0]*110, sl[4][1]*110-50))
                        sob[sc1+j].append(s5)
                        sobs[sc1+j].append(5)
                    elif sc[j] >= 667:
                        screen.blit(gcm,  (sl[5][0]*100, sl[5][1]*100))
                        sob[sc1+j].append(s6)
                        sobs[sc1+j].append(6)
                    
        else:
            sc = sc[3:]
def piece(round):
    #screen.blit(s1, (100, 200))
    imgr = font.render('Round ' + str(round), True, 'Black')
    if round % 2 == 0:
        imgc = font.render("White's turn", True, 'Black')
    else:
        imgc = font.render("Black's turn", True, 'Black')
    screen.blit(imgr,  (850, 350))
    screen.blit(imgc,  (820, 400))
    for i in range(len(bl)):
        try:
            if i < 8:
                screen.blit(pieceb[i], (bl[i][0]*100+25/2, bl[i][1]*100+25/2))
            else:
                screen.blit(pieceb[-1], (bl[i][0]*100+25/2, bl[i][1]*100+25/2))
        except:
            continue
    for i in range(len(wl)):
        try:
            if i < 8:
                screen.blit(piecew[i], (wl[i][0]*100+25/2, wl[i][1]*100+25/2))
            else:
                screen.blit(piecew[-1], (wl[i][0]*100+25/2, wl[i][1]*100+25/2))
        except:
            continue
def wbe(x, y, x1, y1, w, b):
    if round % 2 == 0:
        aa, bb, cc = w, wl, bl
    else:
        aa, bb, cc= b, bl, wl
    #print(board[y1][x1], board[y][x])
    board[y1][x1] =aa
    board[y][x] = '  '
    #show()
    for i in range(len(bb)):
        if board[y1][x1] != '  ':
            for b in range(len(cc)):
                if cc[b] == [x1, y1]:
                    cc[b] = []
        if bb[i] == [x, y]:
            bb[i] = [x1, y1]
            
def sk(sk):
    if round % 2 == 0:
        aa, bb, cc, dd = bl, piecew, wq, wk
    else:
        aa, bb, cc, dd  = wl, pieceb, bq, bk
    if sk == 1:
        for i in ('bk', 'wk', 'bq', 'wq'):
            if board[a[-2][1]][a[-2][-2]] != i:
                board[a[-2][1]][a[-2][-2]] = 'iv'
    elif sk == 2:
        sk2l = []
        ne = 0
        for i in aa:
            if i != []:
                ne += 1
        while len(sk2l) != ne:
            rnx = random.randint(0, 7)
            rny = random.randint(0, 7)
            print(rnx, rny)
            if board[rny][rnx] == '  ':
                sk2l.append([rnx, rny])
            sk2l = [next(group) for key, group in groupby(sorted(sk2l))]
            print(len(sk2l))
        #print(sk2l)
        b = 0
        while b < ne:
            print(ne)
            if aa[b] != []:
                board[sk2l[b][1]][sk2l[b][0]] = board[aa[b][1]][aa[b][0]]
                board[aa[b][1]][aa[b][0]] = '  '
                b += 1
            else:
                b += 1
            show()
        for i in range(ne):
            aa[i] = sk2l[i]
    elif sk == 4:
        x = a[-2][0]
        y = a[-2][1]
        for dx, dy in ([-1, 1], [-1, -1], [1, 1], [1, -1], [1, 0], [0, 1], [-1, 0], [0, -1], [0, 0]):
            print(y+dy, x+dx)
            if y+dy < 8 and x+dx < 8:
                board[y+dy][x+dx] = '  '
                for i in range(len(wl)):
                    if wl[i] == [x+dx, y+dy]:
                        wl[i] = []
                    if bl[i] == [x+dx, y+dy]:
                        bl[i] = []
    elif sk == 6:
        for i in range (len(bb)):
            if round % 2 == 0 and wl[3] != [] and bb[i] == cc:
                board[wl[3][1]][wl[3][0]] = 'wk'
                bb[i] = dd
            elif round % 2 == 1 and bl[3] != [] and bb[i] == cc:
                board[bl[3][1]][bl[3][0]] = 'bk'
                bb[i] = dd
mode = 'none'
sn = 99999
l1 = []
round = -1
a = []
ssp = 'pp'
sc = []
fdx, fdy = 0, 0
bf5, bf6, running = True, False, True
while running: # b == 0
    screen.fill((255, 255, 255)) 
    if round == -1: 
        screen.fill((255, 255, 255)) 
        decision()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                #print(x, y)
                if (200<x<400) and (425<y<525):
                    mode = 'pc'                 
                elif (500<x<700) and (425<y<525):
                    mode = 'nc'
                    round = 0
            pygame.display.flip()
    if mode == 'pc':
        round = 0
        screen.fill((255, 255, 255)) 
        skill(sc)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos 
                sc.append(y)
                print(sc)
                if len(sc) == 6:
                    skill(sc)
                    mode = 'npc'
    if mode == 'nc' or mode == "npc":
        screen.fill((255, 255, 255)) 
        showboard()
        #skill()
        piece(round)
        for event in pygame.event.get():
            c = round
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                x = x//SQUARE_SIZE
                y = y//SQUARE_SIZE
                a.append([x, y])
                print(a)
                try:
                    if len(a)> 1:
                        sp = board[a[-2][1]][a[-2][0]] #seclected piece
                    if x >= 8 and mode == 'npc' and (y == 5 or y == 6 or y == 7 or y == 0 or y == 1 or y == 2):
                        if round % 2 == 0 and (y == 5 or y == 6 or y == 7):
                            sn = 2
                        elif round % 2 == 1 and (y == 0 or y == 1 or y == 2):
                            sn = 0
                        print(y, sn, sobs[y-sn][0])
                        if sobs[y-sn][0] == 1 and nos[y-sn] == 1:
                            l1.append([board[a[-2][1]][a[-2][-2]], [a[-2][1], a[-2][-2]], round])   
                            nos[y-sn] = 0 
                        if sobs[y-sn][0] == 2 and nos[y-sn] == 1:
                            round += 1
                            nos[y-sn] = 0 
                        if sobs[y-sn][0] == 3 and board[a[-2][1]][a[-2][0]] == '  ' and nos[y-sn] == 1:
                            wbe(a[-3][0], a[-3][1], a[-2][0], a[-2][1], 'w'+sp[-1:], 'b'+sp[-1:]) # change to sp[.....
                            round += 1
                            nos[y-sn] = 0 
                        if sobs[y-sn][0] == 5 and nos[y-sn] == 1:
                            bf5 = False
                            nos[y-sn] = 0 
                        if (sobs[y-sn][0] == 4 or sobs[y-sn][0] == 6) and nos[y-sn] == 1:
                            nos[y-sn] = 0 
                            # power mode finished on 9/16/2023
                        sk(sobs[y-sn][0])
                        #show()
                    for i in l1:
                        if round-i[2] == 2:
                            i[1][1], i[1][0] = int(i[1][1]), int(i[1][0])
                            board[i[1][0]][i[1][1]] = i[0]
                            l1.remove(i)
                #try:
                    if len(a)>1:
                        if board[a[-2][1]][a[-2][-2]][0:1] != board[a[-1][1]][a[-1][-2]][0:1] and board[a[-1][1]][a[-1][-2]] != 'iv':
                            
                            ssp = board[a[-1][1]][a[-1][-2]]
                            #print(sp)
                            if sp == 'bp' or sp == 'wp':
                                if (a[-1][0]-a[-2][0] == 0 and board[a[-1][1]][a[-1][0]] == "  " and ((round % 2 == 1 and ((a[-2][-1] == 1 and a[-1][1]-a[-2][1] == 2) or a[-1][1]-a[-2][1] == 1)) or (round % 2 == 0 and ((a[-2][-1] == 6 and a[-1][1]-a[-2][1] == -2) or a[-1][1]-a[-2][1] == -1)))) or board[a[-1][1]][a[-1][0]] != "  " and abs(a[-2][0]-a[-1][0]) == 1 and ((round % 2 == 0 and a[-2][1]-a[-1][1]==1) or (round % 2 == 1 and a[-2][1]-a[-1][1]==-1)):
                                    wbe(a[-2][0], a[-2][1], a[-1][0], a[-1][1], 'wp', 'bp') 
                                    if bf5:
                                        round += 1
                                    a = []                             
                            elif sp == 'br' or sp == 'wr':
                                space = 0
                                if a[-2][0] == a[-1][0]:
                                    s, xr, yr, n1, n2 = a[-2][1]-a[-1][1], a[-2][0],  min(a[-2][1], a[-1][1]), 0, 1
                                elif a[-2][1] == a[-1][1]:
                                    s, xr, yr, n1, n2 = a[-2][0]- a[-1][0], min(a[-2][0], a[-1][0]),  a[-2][1], 1, 0
                                for j in range(1, abs(s)):
                                    if board[yr+j*n2][xr+j*n1] == '  ':
                                        space += 1
                                if space == abs(s)-1:
                                    wbe(a[-2][0], a[-2][1], a[-1][0], a[-1][1], 'wr', 'br')
                                    if bf5:
                                        round += 1
                                    a= []
                            elif sp == 'wh' or sp == 'bh':
                                for dx, dy in ([[-1, 2], [1, 2], [2, 1], [2, -1], [-2, 1], [-2, -1], [-1, -2], [1, -2]]):
                                    if (a[-2][0]+dx == a[-1][0]) and (a[-2][1]+dy == a[-1][1]):
                                        wbe(a[-2][0], a[-2][1], a[-1][0], a[-1][1], 'wh', 'bh')
                                        if bf5:
                                            round += 1
                                        a=[]
                            elif sp == 'wb' or sp == 'bb':
                                space = 0
                                bfb = False
                                if ((-a[-2][1]-(-a[-1][1]))/(a[-2][0]-a[-1][0])) == -1:
                                    xb, v = min(a[-2][1], a[-1][1]), 1
                                elif ((-a[-2][1]-(-a[-1][1]))/(a[-2][0]-a[-1][0])) == 1:
                                    xb, v = max(a[-2][1], a[-1][1]), -1
                                for i in range(1, abs(a[-2][0]-a[-1][0])):
                                    if board[xb+i*v][min(a[-2][0], a[-1][0])+i] == '  ':
                                        space += 1
                                if space == 0 and abs(a[-2][0]-a[-1][0]) == 1 and abs(a[-2][1]-a[-1][1]) == 1:
                                    bfb = True
                                if (space == abs(a[-2][0]-a[-1][0])-1 and space != 0) or bfb:
                                    wbe(a[-2][0], a[-2][1], a[-1][0], a[-1][1], 'wb', 'bb')
                                    if bf5:
                                        round += 1
                                    a=[]
                            elif sp == 'wk' or sp == 'bk':
                                for dx, dy in ([-1, 1], [-1, -1], [1, 1], [1, -1], [1, 0], [0, 1], [-1, 0], [0, -1]):
                                        if (a[-2][0]+dx == a[-1][0]) and (a[-2][1]+dy == a[-1][1]):
                                            wbe(a[-2][0], a[-2][1], a[-1][0], a[-1][1], 'wk', 'bk')
                                            if bf5:
                                                round += 1
                                            a=[]
                            elif sp == 'wq' or sp == 'bq':
                                space = 0
                                bfq = False
                                if a[-2][0]-a[-1][0] != 0:
                                    c = a[-2][0]-a[-1][0]
                                else:
                                    c = a[-2][1]-a[-1][1]
                                for dx, dy in ([-1, 1], [-1, -1], [1, 1], [1, -1], [1, 0], [0, 1], [-1, 0], [0, -1]):
                                    for i in range(abs(c)+1):                           
                                        if (a[-2][0]+dx*i == a[-1][0]) and (a[-2][1]+dy*i == a[-1][1]):
                                            bfq = True
                                            fdx, fdy = dx, dy
                                            break
                                for i in range(1, abs(c)):
                                    if board[a[-2][1]+fdy*i][a[-2][0]+fdx*i] == '  ':
                                        space += 1
                                    else:
                                        space = 0
                                if space == abs(c)-1 and bfq:
                                    wbe(a[-2][0], a[-2][1], a[-1][0], a[-1][1], 'wq', 'bq')
                                    if bf5:
                                        round += 1
                                    a=[]   
                            
                            
                except:
                    pass
                show()
        fw = any('wk' in x for x in board)
        fb = any('bk' in x for x in board)
        if not fw or not fb:
            pygame.draw.rect(screen, 'black', [150, 200, 400, 70])
            if fw and (not fb):
                img = font.render('White win the game!', True, 'white')
                screen.blit(img,  (210, 210))
            elif fb and (not fw):
                img = font.render('Black win the game!', True, 'white')
                screen.blit(img,  (210, 210))
            elif not fb and not fw:
                img = font.render('Tie!', True, 'white')
                screen.blit(img,  (210, 210))


    # noraml mode finish on 2023/9/2
    pygame.display.flip()
    timer.tick(500)
pygame.quit()