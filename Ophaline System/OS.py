# Ophaline System Version 1.0
'''
# Notation List
# - : Ground
# = : Unbreakable Ground
# + : Fire Ground
# * : Unbreakable Fire Ground
# o : Hole
# f : Birthplace(Can also go to the upper level)
# x : Wall
# z : Unbreakable Wall

# b : Bun

# n : Trap
# p : Pickaxe
# s : Shovel
# c : Carrot

# / : LineBreak
'''

'''
# Connectedness Notations
# 0 : Unconnected
# 1 : Connected
# Order : WNES (West, North, East, South)(Left, Up, Right, Down)
'''

testmapstringsample = 'W1 b1n0p0s0c0/x0000 x0000 x0000 x0000 x0000 x0000 x0000 x0000 x0000 x0000 x0000 x0000 x0000 x0000 x0000 x0000 x0000 x0000 x0000 x0000 x0000 x0000 x0000 -0000 x0000 -0000 x0000 x0000 x0000 x0000 x0000 x0000 x0000 x0000 x0000 x0000 x0000 -0000 -0000 -0000 -0000 -0000 x0000 x0000 x0000 x0000 x0000 x0000 x0000 x0000 x0000 x0000 x0000 x0000 x0000 -0000 x0000 x0000 x0000 x0000 x0000 x0000 f0000 -0000 -0000 -0000 -0000 b0001 -0000 -0000 -0000 -0000 x0000 x0000 x0000 x0000 x0000 x0000 x0000 -0000 x0000 x0000 x0000 x0000 x0000 x0000 x0000 x0000 x0000 x0000 x0000 x0000 x0000 x0000 o0000 x0000 x0000 x0000 x0000 x0000 x0000 x0000 x0000 x0000 x0000 x0000 x0000 x0000 x0000 x0000 x0000 x0000 x0000 x0000 x0000 x0000 x0000 x0000 x0000 x0000 x0000 x0000 x0000 x0000 x0000 x0000 x0000 x0000 x0000 x0000 x0000 x0000 x0000 x0000 x0000'

'''
# A level is originally 9*15.
# MapList, PaqueretteCoordinate, BunList, UnusedTool
'''
class level_info:
    
    def __init__(self, instr):
        # Create the maplist
        # (Left, Up, Right, Down)
        self.map = [[['z', [False, False, False, False]] for y in range(15)] for x in range(9)]
        # Level info. e.g. for W-01, dir = 'W', height = 1
        self.dir = ''
        self.height = 0
        self.levelstr = ''
        # Paquerette Coordinate
        self.px = 0
        self.py = 0
        # list for bun class
        self.bunlist = []
        # list for unused npsc
        self.toollist = [0, 0, 0, 0]
        
        if instr[1] in '0123456789':
            self.dir = instr[:1]
            instr = instr[1:]
        else:
            self.dir = instr[:2]
            instr = instr[2:]
        if instr[1] in '0123456789':
            self.height = int(instr[:2])
            self.levelstr = self.dir + '-' + instr[:2]
            instr = instr[2:]
        else:
            self.height = int(instr[:1])
            self.levelstr = self.dir + '-0' + instr[:1]
            instr = instr[1:]
        buffer = ''
        while True:
            char = instr[0]
            instr = instr[1:]
            if char == '/':
                break
            if (buffer == '') and (char in 'npsc'):
                buffer = char
                continue
            if (buffer != '') and (char in '0123456789'):
                if buffer == 'n':
                    self.toollist[0] = int(char)
                if buffer == 'p':
                    self.toollist[1] = int(char)
                if buffer == 's':
                    self.toollist[2] = int(char)
                if buffer == 'c':
                    self.toollist[3] = int(char)
                buffer = ''
                continue
        x = 0
        y = -1
        buffer = ''
        while True:
            if instr == '':
                break
            else:
                char = instr[0]
                if (char in '-=+*ofxzbnc'):
                    if y == 14:
                        y = 0
                        x += 1
                    else:
                        y += 1
                    instr = instr[1:]
                    self.map[x][y][0] = char
                    buffer = char
                    continue
                else:
                    if (char in '01') and (buffer != ''):
                        self.map[x][y][1][0] = (instr[0] == '1')
                        self.map[x][y][1][1] = (instr[1] == '1')
                        self.map[x][y][1][2] = (instr[2] == '1')
                        self.map[x][y][1][3] = (instr[3] == '1')
                        instr = instr[4:]
                        buffer = ''
                        continue
                instr = instr[1:]
        bunnum = 0
        for x in range(9):
            for y in range(15):
                if self.map[x][y][0] == 'f':
                    self.px = x
                    self.py = y
                if self.map[x][y][0] == 'b':
                    bunnum += 1
                    self.bunlist.append(bun({self.levelstr + '-0' + str(bunnum)}, x, y))

class bun:
    # This class track information that if 
    def __init__(self, bunset, x, y):
        # bunset is a set that stores the name(string) of buns at (x, y)
        self.bunset = bunset
        self.x = x
        self.y = y
        self.single = (len(bunset) == 1)

def bunrun():
    # This method must be as fast as possible!
    # Also should be absolutely correct
    

def pcomponent(info):
    pass
