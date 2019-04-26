import curses
from curses import wrapper # for easier debug, restoring echo etc..
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
import locale # for non-ASCII characters interpretation

class player(object):
	movedright = False
	movedleft = False
	movedup = False
	moveddown = False
	sprite = u'\u2639'.encode('utf-8')
	havepotion = False
	havefruit = False
	health = 100
	gold = 0


# hidden path
class path(object):
    isHidden = True
    sprite = u'\2592'.encode('utf-8')

# enemies
class enemy(object):
    def __init__(self, name):
        self.name = name
    Health = 30
    isdeath = False
    isHidden = True
    y9 = 0
    x9 = 0
    def move(self):
    	if (self.isdeath == False):
            if ((self.y9,self.x9 + 1) == (y,x)):
                player.health -= 2
            elif ((self.y9,self.x9 - 1) == (y,x)):
                player.health -= 2
            elif ((self.y9 + 1,self.x9) == (y,x)):
                player.health -= 2
            elif ((self.y9 - 1,self.x9) == (y,x)):
                player.health -= 2
            if abs(x - self.x9) < 8 and (x - self.x9) > 0 and abs(y - self.y9) < 4 and (self.y9,self.x9 + 1) != (y,x) and (self.y9,self.x9 + 1) != (enemy1.y9, enemy1.x9) and (self.y9,self.x9 + 1) != (enemy2.y9, enemy2.x9) and (self.y9,self.x9 + 1) != (enemy3.y9, enemy3.x9) and (self.y9,self.x9 + 1) != (enemy4.y9, enemy4.x9) and (self.y9,self.x9 + 1) != (enemy5.y9, enemy5.x9) and (self.y9,self.x9 + 1) != (enemy6.y9, enemy6.x9) and (self.y9,self.x9 + 1) != (enemy7.y9, enemy7.x9) and (self.y9,self.x9 + 1) != (enemy8.y9, enemy8.x9) and (self.y9,self.x9 + 1) != (enemy9.y9, enemy9.x9) and (self.y9,self.x9 + 1) != (enemy10.y9, enemy10.x9):
                self.x9 += 1
            if abs(x - self.x9) < 8 and (x - self.x9) < 0 and abs(y - self.y9) < 4 and (self.y9,self.x9 - 1) != (y,x) and (self.y9,self.x9 - 1) != (enemy1.y9, enemy1.x9) and (self.y9,self.x9 - 1) != (enemy2.y9, enemy2.x9) and (self.y9,self.x9 - 1) != (enemy3.y9, enemy3.x9) and (self.y9,self.x9 - 1) != (enemy4.y9, enemy4.x9) and (self.y9,self.x9 - 1) != (enemy5.y9, enemy5.x9) and (self.y9,self.x9 - 1) != (enemy6.y9, enemy6.x9) and (self.y9,self.x9 - 1) != (enemy7.y9, enemy7.x9) and (self.y9,self.x9 - 1) != (enemy8.y9, enemy8.x9) and (self.y9,self.x9 - 1) != (enemy9.y9, enemy9.x9) and (self.y9,self.x9 - 1) != (enemy10.y9, enemy10.x9):
            	self.x9 -= 1
            if abs(y - self.y9) < 4 and (y - self.y9) > 0 and abs(x - self.x9) < 8 and (self.y9 + 1,self.x9) != (y,x) and (self.y9 + 1,self.x9) != (enemy1.y9, enemy1.x9) and (self.y9 + 1,self.x9) != (enemy2.y9, enemy2.x9) and (self.y9 + 1,self.x9) != (enemy3.y9, enemy3.x9) and (self.y9 + 1,self.x9) != (enemy4.y9, enemy4.x9) and (self.y9 + 1,self.x9) != (enemy5.y9, enemy5.x9) and (self.y9 + 1,self.x9) != (enemy6.y9, enemy6.x9) and (self.y9 + 1,self.x9) != (enemy7.y9, enemy7.x9) and (self.y9 + 1,self.x9) != (enemy8.y9, enemy8.x9) and (self.y9 + 1,self.x9) != (enemy9.y9, enemy9.x9) and (self.y9 + 1,self.x9) != (enemy10.y9, enemy10.x9):
                self.y9 += 1
            if abs(y - self.y9) < 4 and (y - self.y9) < 0 and abs(x - self.x9) < 8 and (self.y9 - 1,self.x9) != (y,x) and (self.y9 - 1,self.x9) != (enemy1.y9, enemy1.x9) and (self.y9 - 1,self.x9) != (enemy2.y9, enemy2.x9) and (self.y9 - 1,self.x9) != (enemy3.y9, enemy3.x9) and (self.y9 - 1,self.x9) != (enemy4.y9, enemy4.x9) and (self.y9 - 1,self.x9) != (enemy5.y9, enemy5.x9) and (self.y9 - 1,self.x9) != (enemy6.y9, enemy6.x9) and (self.y9 - 1,self.x9) != (enemy7.y9, enemy7.x9) and (self.y9 - 1,self.x9) != (enemy8.y9, enemy8.x9) and (self.y9 - 1,self.x9) != (enemy9.y9, enemy9.x9) and (self.y9 - 1,self.x9) != (enemy10.y9, enemy10.x9):
            	self.y9 -= 1


class gold(object):
    def __init__(self, name):
        self.name = name
    isHidden = True
    takken = 0
    sprite = '€'
    x = 0
    y = 0


# initializing variables
rows = 50
col  = 150
y,x  = 18,10
winstate = -1
exit = False



#  Room
class Room(object):
	def __init__(self, name):
		self.name = name
	isHidden = True
	spriteHorizontal = u'\u2550'.encode('utf-8')
	spriteVertical = u'\u2551'.encode('utf-8')
	spriteTopRight = u'\u2557'.encode('utf-8')
	spriteTopLeft = u'\u2554'.encode('utf-8')
	spriteBottomRight = u'\u255d'.encode('utf-8')
	spriteBottomLeft = u'\u255a'.encode('utf-8')
	spriteDoor = '#' #u'\u256c'.encode('utf-8')
	def putrooms(self, ylocation, xlocation, ysize, xsize, upexit, downexit,leftexit, rightexit):
		if (self.isHidden == False):
			i = xlocation + 1
			j = ylocation + 1

			while (j < ylocation + ysize):
				stdscr.addstr(j, xlocation, Room.spriteVertical)
				stdscr.addstr(j, xlocation + xsize, Room.spriteVertical)
				k = 1
				while (k < xsize):
					 if (chr(stdscr.inch(j, k + xlocation)) == ' '):
					 	stdscr.addstr(j , k + xlocation, '.')
					 k += 1
				j += 1

			while (i < xlocation + xsize):
				stdscr.addstr(ylocation, i,Room.spriteHorizontal)
				stdscr.addstr(ylocation + ysize, i,Room.spriteHorizontal)
				i += 1
			stdscr.addstr(ylocation, xlocation, Room.spriteTopLeft)
			stdscr.addstr(ylocation + ysize, xlocation + xsize, Room.spriteBottomRight)
			stdscr.addstr(ylocation, xlocation + xsize, Room.spriteTopRight)
			stdscr.addstr(ylocation + ysize, xlocation, Room.spriteBottomLeft)

			if (upexit != -1):
				stdscr.addstr(ylocation , xlocation + upexit ,Room.spriteDoor)
			
			if (downexit != -1):
				stdscr.addstr(ylocation + ysize, xlocation + downexit,Room.spriteDoor)
			
			if (rightexit != -1 ):
				stdscr.addstr(ylocation + rightexit, xlocation + xsize,Room.spriteDoor)
			
			if (leftexit != -1):
				stdscr.addstr(ylocation + leftexit , xlocation ,Room.spriteDoor)

def borders(stdscr, y, x):
	i = 1
	while (i < y):
		stdscr.addstr(i,0, u'\u2502'.encode('utf-8'))
		stdscr.addstr(i,x, u'\u2502'.encode('utf-8'))
		i += 1
	i = 1
	while (i < x):
		stdscr.addstr(0,i, u'\u2500'.encode('utf-8'))
		stdscr.addstr(y,i, u'\u2500'.encode('utf-8'))
		i += 1


class Path(object):
	def __init__(self, name):
		self.name = name
	isHidden = True
	spritepath = '#'
	def putpaths(self, ylocation1, xlocation1, size, horizontal):
		if (self.isHidden == False):
			if (horizontal == True):
				i = 1
				while(i < size):
					if (chr(stdscr.inch(ylocation1, xlocation1 + i)) == ' '):
						stdscr.addstr(ylocation1, xlocation1 + i, self.spritepath)
					i += 1
			else:
				i = 1
				while(i < size):
					if (chr(stdscr.inch(ylocation1 + i, xlocation1)) == ' '):
						stdscr.addstr(ylocation1 + i, xlocation1, self.spritepath)
					i += 1

locale.setlocale(locale.LC_ALL, '')
stdscr = curses.initscr() # initialize screen
curses.start_color() 
stdscr.keypad(True) # to take events  from keyboard 
curses.noecho() # dont echo pressed keys
curses.curs_set(0) # make curser invisible
stdscr.resize(rows, col)
dims = stdscr.getmaxyx() # get yx dimensions
curses.cbreak() # take input without requiring ENTER from user

Room1 = Room('Room1')
Room2 = Room('Room2')
Room3 = Room('Room3')
Room4 = Room('Room4')
Room5 = Room('Room5')
Room6 = Room('Room6')
Room7 = Room('Room7')
Room8 = Room('Room8')
Path1 = Path('Path1')
Path2 = Path('Path2')
Path3 = Path('Path3')
Path4 = Path('Path4')
Path5 = Path('Path5')
Path6 = Path('Path6')
Path7 = Path('Path7')
Path8 = Path('Path8')

gold1 = gold('gold1')
gold2 = gold('gold2')
gold3 = gold('gold3')
gold4 = gold('gold4')
gold5 = gold('gold5')

enemy1 = enemy('K')
enemy1.y9 = 8
enemy1.x9 = 6
enemy2 = enemy('L')
enemy2.y9 = 4
enemy2.x9 = 45
enemy3 = enemy('B')
enemy3.y9 = 31
enemy3.x9 = 12
enemy4 = enemy('F')
enemy4.y9 = 8
enemy4.x9 = 120
enemy5 = enemy('K')
enemy5.y9 = 8
enemy5.x9 = 127
enemy6 = enemy('U')
enemy6.y9 = 2
enemy6.x9 = 113
enemy7 = enemy('Q')
enemy7.y9 = 41
enemy7.x9 = 137
enemy8 = enemy('I')
enemy8.y9 = 24
enemy8.x9 = 35
enemy9 = enemy('T')
enemy9.y9 = 42
enemy9.x9 = 9
enemy10 = enemy('R')
enemy10.y9 = 44
enemy10.x9 = 15

gold1.y = 6
gold1.x = 53
gold2.y = 2
gold2.x = 136
gold3.y = 44
gold3.x = 92
gold4.y = 41
gold4.x = 97
gold5.y = 24
gold5.x = 32

while input != ord('0'):
    stdscr.clear()


    # player print
    stdscr.addstr(y,x, player.sprite)

    if ((y == 44 and x == 10) or (y == 43 and x == 9)):
    	winstate = 1
    	break
    elif (player.health <= 0):
    	winstate = 0
    	break

    # move enemies
    enemy1.move()
    enemy2.move()
    enemy3.move()
    enemy4.move()
    enemy5.move()
    enemy6.move()
    enemy7.move()
    enemy8.move()
    enemy9.move()
    enemy10.move()


    if (gold1.y == y and gold1.x == x and gold1.takken == 0):
        gold1.takken = 1
        player.gold += 15
    if (gold2.y == y and gold2.x == x and gold2.takken == 0):
        gold2.takken = 1
        player.gold += 15
    if (gold3.y == y and gold3.x == x and gold3.takken == 0):
        gold3.takken = 1
        player.gold += 15
    if (gold4.y == y and gold4.x == x and gold4.takken == 0):
        gold4.takken = 1
        player.gold += 15
    if (gold5.y == y and gold5.x == x and gold5.takken == 0):
        gold5.takken = 1
        player.gold += 15

    # gold
    

    if (gold1.isHidden == False and gold1.takken == 0):
        stdscr.addstr(gold1.y, gold1.x, gold1.sprite)

    if (gold2.isHidden == False and gold2.takken == 0):
        stdscr.addstr(gold2.y, gold2.x, gold2.sprite)

    if (gold3.isHidden == False and gold3.takken == 0):
        stdscr.addstr(gold3.y, gold3.x, gold3.sprite)

    if (gold4.isHidden == False and gold4.takken == 0):
        stdscr.addstr(gold4.y, gold4.x, gold4.sprite)

    if (gold5.isHidden == False and gold5.takken == 0):
        stdscr.addstr(gold5.y, gold5.x, gold5.sprite)


    # enemy print 
    if (enemy1.isdeath == False):
        stdscr.addstr(enemy1.y9, enemy1.x9, enemy1.name)
    if (y == 8 and x == 39):
    	enemy2.isHidden = False
    	gold1.isHidden = False
    if (enemy2.isHidden == False and enemy2.isdeath == False):
        stdscr.addstr(enemy2.y9, enemy2.x9, enemy2.name)
    if (y == 33 and x == 29):
    	enemy3.isHidden = False
    if (enemy3.isHidden == False and enemy3.isdeath == False):
        stdscr.addstr(enemy3.y9, enemy3.x9, enemy3.name)
    if (y == 4 and x == 89):
    	enemy4.isHidden = False
    if (enemy4.isHidden == False and enemy4.isdeath == False):
        stdscr.addstr(enemy4.y9, enemy4.x9, enemy4.name)
    if (y == 4 and x == 89):
    	enemy5.isHidden = False
    if (enemy5.isHidden == False and enemy5.isdeath == False):
        stdscr.addstr(enemy5.y9, enemy5.x9, enemy5.name)
    if (y == 4 and x == 89):
    	enemy6.isHidden = False
    	gold2.isHidden = False
    if (enemy6.isHidden == False and enemy6.isdeath == False):
        stdscr.addstr(enemy6.y9, enemy6.x9, enemy6.name)
    if (y == 39 and x == 125):
    	enemy7.isHidden = False
    	gold3.isHidden = False
    	gold4.isHidden = False
    if (enemy7.isHidden == False and enemy7.isdeath == False):
        stdscr.addstr(enemy7.y9, enemy7.x9, enemy7.name)
    if (y == 21 and x == 61):
    	enemy8.isHidden = False
    	gold5.isHidden = False
    if (enemy8.isHidden == False and enemy8.isdeath == False):
        stdscr.addstr(enemy8.y9, enemy8.x9, enemy8.name)
    if (y == 33 and x == 29):
    	enemy9.isHidden = False
    if (enemy9.isHidden == False and enemy9.isdeath == False):
        stdscr.addstr(enemy9.y9, enemy9.x9, enemy9.name)
    if (y == 33 and x == 29):
    	exit = True
    	enemy10.isHidden = False
    if (enemy10.isHidden == False and enemy10.isdeath == False):
        stdscr.addstr(enemy10.y9, enemy10.x9, enemy10.name)
    if (exit == True):
       stdscr.addstr(44,9, u'\u2592'.encode('utf-8'))

    
    stdscr.addstr(1,2, "Health = {}".format(player.health))
    stdscr.addstr(2,2, "Money € = {}".format(player.gold))

    # print the area
    borders(stdscr, dims[0] - 2, dims[1] - 2)
    Room1.isHidden = False
    Room1.putrooms(5, 5, 15, 20, -1, -1, -1, 3)
    if (y == 8 and x == 39):
         Room2.isHidden = False
    Room2.putrooms(3, 40, 6, 15, -1, -1, 5, 1)
    if (y == 4 and x == 89):
         Room3.isHidden = False
    Room3.putrooms(1, 90, 8, 50, -1, 35, 3, -1)
    if (y == 20 and x == 116):
         Room4.isHidden = False
    Room4.putrooms(12, 90, 10, 25, -1, -1, 9, 8)
    if (y == 39 and x == 125):
        Room5.isHidden = False
    Room5.putrooms(40, 90, 5, 50, 35, -1, -1, -1)
    if (y == 21 and x == 61):
        Room6.isHidden = False
    Room6.putrooms(20, 30, 5, 30, -1, -1, -1, 1)
    if (y == 29 and x == 65):
        Room7.isHidden = False
    Room7.putrooms(30, 60, 5, 10, 5, -1, 3, -1)
    if (y == 33 and x == 29):
        Room8.isHidden = False
    Room8.putrooms(30, 8, 15, 20, -1, -1, -1, 3)
    if (y == 8 and x == 25):
    	Path1.isHidden = False
    Path1.putpaths(8,25,15,True)
    if (y == 4 and x == 55):
    	Path2.isHidden = False
    Path2.putpaths(4,55,35,True)
    if (y == 9 and x == 125):
    	Path3.isHidden = False
    Path3.putpaths(9,125,31,False)
    if (y == 20 and x == 115):
    	Path4.isHidden = False
    Path4.putpaths(20,115,11,True)
    if (y == 20 and x == 125):
    	Path5.isHidden = False
    Path5.putpaths(20,115,11,True)
    if (y == 21 and x == 91):
    	Path6.isHidden = False
    Path6.putpaths(21,60,30,True)
    if (y == 33 and x == 61):
    	Path7.isHidden = False
    Path7.putpaths(33,28,32,True)
    if (y == 21 and x == 65):
    	Path8.isHidden = False
    Path8.putpaths(21,65,10,False)

    

    stdscr.refresh()
    input = stdscr.getch()
    if (input == KEY_UP and y > 1 and chr(stdscr.inch(y - 1, x)) == '.') or (input == KEY_UP and y > 1 and (chr(stdscr.inch(y - 1, x)) == '#')) or (input == KEY_UP and y > 1 and (chr(stdscr.inch(y - 1, x)) == '€')):
        y -= 1
        player.movedup = True
    elif (input == KEY_DOWN and y < dims[0] - 3 and chr(stdscr.inch(y + 1, x)) == '.') or (input == KEY_DOWN and y < dims[0] - 3 and chr(stdscr.inch(y + 1, x))== '#') or (input == KEY_DOWN and y < dims[0] - 3 and chr(stdscr.inch(y + 1, x))== '€'):
        y += 1
        player.moveddown = True
    elif (input == KEY_RIGHT and x < dims[1] - 3 and chr(stdscr.inch(y, x + 1)) == '.') or (input == KEY_RIGHT and x < dims[1] - 3 and chr(stdscr.inch(y, x + 1)) == '#') or (input == KEY_RIGHT and x < dims[1] - 3 and chr(stdscr.inch(y, x + 1)) == '€'):
        x += 1
        player.movedright = True
    elif (input == KEY_LEFT and x > 1 and chr(stdscr.inch(y, x - 1)) == '.') or (input == KEY_LEFT and x > 1 and chr(stdscr.inch(y, x - 1)) == '#') or (input == KEY_LEFT and x > 1 and chr(stdscr.inch(y, x - 1)) == '€'):
        x -= 1
        player.movedleft = True
    else:
    	player.moved = False

    if (((y - 1, x) == (enemy1.y9,enemy1.x9))):
        enemy1.Health -= 5
        player.movedup == False
    elif (((y + 1, x) == (enemy1.y9,enemy1.x9))):
        enemy1.Health -= 5
        player.moveddown == False
    elif (((y, x - 1) == (enemy1.y9,enemy1.x9))):
        enemy1.Health -= 5
        player.movedleft == False
    elif (((y, x + 1) == (enemy1.y9,enemy1.x9))):
        enemy1.Health -= 5
        player.movedright == False

    if ((y - 1, x) == (enemy2.y9,enemy2.x9)):
        enemy2.Health -= 5
    elif ((y + 1, x) == (enemy2.y9,enemy2.x9)):
        enemy2.Health -= 5
    elif ((y, x - 1) == (enemy2.y9,enemy2.x9)):
        enemy2.Health -= 5
    elif ((y, x + 1) == (enemy2.y9,enemy2.x9)):
        enemy2.Health -= 5

    if ((y - 1, x) == (enemy3.y9,enemy3.x9)):
        enemy3.Health -= 5
    elif ((y + 1, x) == (enemy3.y9,enemy3.x9)):
        enemy3.Health -= 5
    elif ((y, x - 1) == (enemy3.y9,enemy3.x9)):
        enemy3.Health -= 5
    elif ((y, x + 1) == (enemy3.y9,enemy3.x9)):
        enemy3.Health -= 5

    if ((y - 1, x) == (enemy4.y9,enemy4.x9)):
        enemy4.Health -= 5
    elif ((y + 1, x) == (enemy4.y9,enemy4.x9)):
        enemy4.Health -= 5
    elif ((y, x - 1) == (enemy4.y9,enemy4.x9)):
        enemy4.Health -= 5
    elif ((y, x + 1) == (enemy4.y9,enemy4.x9)):
        enemy4.Health -= 5

    if ((y - 1, x) == (enemy5.y9,enemy5.x9)):
        enemy5.Health -= 5
    elif ((y + 1, x) == (enemy5.y9,enemy5.x9)):
        enemy5.Health -= 5
    elif ((y, x - 1) == (enemy5.y9,enemy5.x9)):
        enemy5.Health -= 5
    elif ((y, x + 1) == (enemy5.y9,enemy5.x9)):
        enemy5.Health -= 5

    if ((y - 1, x) == (enemy6.y9,enemy6.x9)):
        enemy6.Health -= 5
    elif ((y + 1, x) == (enemy6.y9,enemy6.x9)):
        enemy6.Health -= 5
    elif ((y, x - 1) == (enemy6.y9,enemy6.x9)):
        enemy6.Health -= 5
    elif ((y, x + 1) == (enemy6.y9,enemy6.x9)):
        enemy6.Health -= 5

    if ((y - 1, x) == (enemy7.y9,enemy7.x9)):
        enemy7.Health -= 5
    elif ((y + 1, x) == (enemy7.y9,enemy7.x9)):
        enemy7.Health -= 5
    elif ((y, x - 1) == (enemy7.y9,enemy7.x9)):
        enemy7.Health -= 5
    elif ((y, x + 1) == (enemy7.y9,enemy7.x9)):
        enemy7.Health -= 5

    if ((y - 1, x) == (enemy8.y9,enemy8.x9)):
        enemy8.Health -= 5
    elif ((y + 1, x) == (enemy8.y9,enemy8.x9)):
        enemy8.Health -= 5
    elif ((y, x - 1) == (enemy8.y9,enemy8.x9)):
        enemy8.Health -= 5
    elif ((y, x + 1) == (enemy8.y9,enemy8.x9)):
        enemy8.Health -= 5

    if ((y - 1, x) == (enemy9.y9,enemy9.x9)):
        enemy9.Health -= 5
    elif ((y + 1, x) == (enemy9.y9,enemy9.x9)):
        enemy9.Health -= 5
    elif ((y, x - 1) == (enemy9.y9,enemy9.x9)):
        enemy9.Health -= 5
    elif ((y, x + 1) == (enemy9.y9,enemy9.x9)):
        enemy9.Health -= 5

    if ((y - 1, x) == (enemy10.y9,enemy10.x9)):
        enemy10.Health -= 5
    elif ((y + 1, x) == (enemy10.y9,enemy10.x9)):
        enemy10.Health -= 5
    elif ((y, x - 1) == (enemy10.y9,enemy10.x9)):
        enemy10.Health -= 5
    elif ((y, x + 1) == (enemy10.y9,enemy10.x9)):
        enemy10.Health -= 5

    if (enemy1.Health < 0):
        enemy1.isdeath = True
    if (enemy2.Health < 0):
        enemy2.isdeath = True
    if (enemy3.Health < 0):
        enemy3.isdeath = True
    if (enemy4.Health < 0):
        enemy4.isdeath = True
    if (enemy5.Health < 0):
        enemy5.isdeath = True
    if (enemy6.Health < 0):
        enemy6.isdeath = True
    if (enemy7.Health < 0):
        enemy7.isdeath = True
    if (enemy8.Health < 0):
        enemy8.isdeath = True
    if (enemy9.Health < 0):
        enemy9.isdeath = True
    if (enemy10.Health < 0):
        enemy10.isdeath = True

while input != ord('0'):
	stdscr.clear()
	if (winstate == 1):
		stdscr.addstr(25, 70, 'Player Win!')
	if (winstate == 0):
		stdscr.addstr(25, 70, 'Game Over!')
	stdscr.refresh()
	input = stdscr.getch()
stdscr.getch()
curses.endwin()


# q = potion
# move with u,j,k,h like original rogue
# w = wear armor if u have one
# e = eat fruits if u have one
# display skull when character dies > stdscr.addstr(y,x, u'\u2620'.encode('utf-8')









'''
# move character function

def move()


# draw map function

def draw_map()
'''




# to end curses program
'''
curses.nocbreak()
stdscr.keypad(False)
curses.echo()
'''