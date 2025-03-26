from enum import IntEnum

import Console
import OkeyMath

class OkeyValue(IntEnum):
    TFalseOkey=0
    T1=1
    T2=2
    T3=3
    T4=4
    T5=5
    T6=6
    T7=7
    T8=8
    T9=9
    T10=10
    T11=11
    T12=12
    T13=13
    def to_int(self):
        return self.value

class OkeyColor(IntEnum):
    RED=0
    YELLOW=1
    BLACK=2
    BLUE=3
    def to_int(self):
        return self.value

class OkeyTile():
    Value:OkeyValue
    Color:OkeyColor
    
    def __init__(self,*args):
        if len(args)==0:
            self.Value=OkeyValue(OkeyMath.random_int(14))
            self.Color=OkeyColor(OkeyMath.random_int(4))
        else:
            val=args[0]
            self.Value=OkeyValue(val % 14)
            self.Color=OkeyColor(val//14)
        
    def print(self):
        colorvec=["r","y","k","b"]
        color=colorvec[self.Color.to_int()]
        if self.Value is OkeyValue.TFalseOkey:
            Console.print_color("FalseOkey",color)
        else:
            Console.print_color(f"{self.Value}",color)

for i in range(14*4):
    OkeyTile(i).print()
