from advent import *
import math

aoc = Session(2023,3)

with aoc.fp() as f:
    grid = [line.strip() for line in f.readlines()]

height = len(grid)
width = len(grid[0])

def adj_symbol(x,y,grid):
    for ex,ey in adj8(x,y,grid):
        if(grid[ey][ex] not in "0123456789."):
            return True
    return False

def adj_gears(x,y,grid):
    gears = set()
    for ex,ey in adj8(x,y,grid):
        if(grid[ey][ex] == "*"):
            gears.add((ex,ey))
    return gears


class State:
    def __init__(self):
        self._reset()
        
    def _reset(self):
        self.start_loc = None
        self.v = 0
        self.in_num = False
        self.is_part = False
        self.gears = set()
    
    def process(self,c,x,y,grid):
        if(state.in_num):
            state._extend(c)
        else:
            state._begin(x,y,c)
        state._check_adj(x,y,grid)
        
    def _extend(self,digit):
        self.v = self.v * 10 + int(digit)
    
    def _begin(self,x,y,digit):
        self.v = int(digit)
        self.in_num = True
        self.start_loc = (x,y)
        
    def _check_adj(self,x,y,grid):
        self.is_part |= adj_symbol(x,y,grid)
        self.gears |= adj_gears(x,y,grid)
        
    def flush(self,number_dict,gear_dict):
        if(self.in_num):
            number_dict[self.start_loc] = (self.v,self.is_part)
        for gear_loc in self.gears:
            gear_dict[gear_loc] = gear_dict.get(gear_loc,[]) + [(self.start_loc,self.v)]
        self._reset()
        
number_dict = {}
gear_dict = {}
            
for y in range(width):
    state = State()
    
    for x in range(width):
        c = grid[y][x]
        if(c in "0123456789"):
            state.process(c,x,y,grid)
        else:
            state.flush(number_dict,gear_dict)
    state.flush(number_dict,gear_dict)
 
silver = sum(v for (v,is_part) in number_dict.values() if is_part)
gold = sum(math.prod(v for (_,v) in A) for A in gear_dict.values() if len(A) == 2)

aoc.solution(1,silver)
aoc.solution(2,gold)
