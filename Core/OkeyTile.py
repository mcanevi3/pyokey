from enum import IntEnum
import copy

import Console
import OkeyMath

class OkeyValue(IntEnum):
    T1=0
    T2=1
    T3=2
    T4=3
    T5=4
    T6=5
    T7=6
    T8=7
    T9=8
    T10=9
    T11=10
    T12=11
    T13=12
    
    def to_int(self):
        return self.value+1

class OkeyColor(IntEnum):
    RED=0
    YELLOW=1
    BLACK=2
    BLUE=3
    def to_int(self):
        return self.value

class OkeyType(IntEnum):
    STANDART=0
    FALSE_OKEY=1
    OKEY=2
    def to_int(self):
        return self.value

class OkeyTile():
    Value:OkeyValue
    Color:OkeyColor
    Type=OkeyType.STANDART
    
    def __init__(self,*args):
        if len(args)==0:
            self.Value=OkeyValue(OkeyMath.random_int(13))
            self.Color=OkeyColor(OkeyMath.random_int(4))
        else:
            val=args[0]
            self.Value=OkeyValue(val % 13)
            self.Color=OkeyColor(val//13)
            
    def to_int(self):
        val=13*self.Color.to_int()+self.Value.to_int()
        return val
    
    def print(self):
        colorvec=["r","y","k","b"]
        color=colorvec[self.Color.to_int()]

        if self.Type is OkeyType.STANDART:
            Console.print_color(f"{self.Value.to_int()}",color)
        elif self.Type is OkeyType.FALSE_OKEY:
            Console.print_color(f"[{self.Value.to_int()} F]",color)
        else:
            Console.print_color(f"[{self.Value.to_int()}]",color)

class OkeyStack:
    Tiles=[]
    Okey:OkeyTile
    
    def __init__(self):
        vec=list(range(0,52))+list(range(0,52))
        self.Tiles=[OkeyTile(x) for x in vec]
        
        random_tile=OkeyTile()
        for tile in self.Tiles:
            if tile.to_int()==random_tile.to_int():
                tile.Type=OkeyType.OKEY

        random_tile.Type=OkeyType.FALSE_OKEY
        self.Tiles.append(copy.deepcopy(random_tile))
        random_tile.Type=OkeyType.FALSE_OKEY
        self.Tiles.append(copy.deepcopy(random_tile))

        random_tile.Type=OkeyType.OKEY
        self.Okey=random_tile

        self.Tiles=OkeyMath.shuffle(self.Tiles)

    def print(self):
        self.Okey.print()
        print("")
        for tile in self.Tiles:
            tile.print()
        print("")

    def draw_tile(self):
        return self.Tiles.pop()

class OkeyPlayer:
    Tiles=[]
    Id:int 
    Stack:OkeyStack

    def __init__(self,id:int,stack:OkeyStack):
        self.Id=id
        self.Stack=stack

    def get_tile(self,count=1):
        for _ in range(count):
            self.Tiles.append(self.Stack.draw_tile())
    
    def print(self):
        print(f"Player{self.Id}:",end=" ")
        [t.print() for t in self.Tiles]

    def sort_tiles(self):
        okey=stack.Okey
        vec=[t.Value.to_int() for t in self.Tiles]
        sorted_indices = sorted(range(len(vec)), key=lambda i: vec[i])
        tiles=[self.Tiles[i] for i in sorted_indices]

        for t in tiles:
            t.print()

    def get_color_pairs(self):
        pairs=[]
        for val in range(1,14):
            pair = [x for x in self.Tiles if x.Value.to_int() == val]
            pair_colors=[x.Color for x in pair]
            unique_color_indices = {val: i for i, val in enumerate(pair_colors)}.values()
            unique_color_indices=list(unique_color_indices)
            
            unique_pair=[pair[i] for i in unique_color_indices]
            if len(unique_pair)>2:
                pairs.append(unique_pair)
        return pairs

stack=OkeyStack()
# stack.print()

player1=OkeyPlayer(id=1,stack=stack)
player1.get_tile(14)
player1.print()
print("")

pairs=player1.get_color_pairs()
for pair in pairs:
    for t in pair:
        t.print()
    print(" ")

