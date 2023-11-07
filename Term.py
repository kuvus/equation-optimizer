from enum import Enum

class Type(Enum):
    START = 0
    PAR = 1
    MUL = 2
    DIV = 3
    ADD = 4
    SUB = 5
    SIN = 6
    COS = 7
    VAR = 8
    NUM = 9

    def __str__(self) -> str:
        match (self):
            case Type.START:
                return "START"
            case Type.PAR:
                return "PAR"
            case Type.MUL:
                return "MUL"
            case Type.DIV:
                return "DIV"
            case Type.ADD:
                return "ADD"
            case Type.SUB:
                return "SUB"
            case Type.SIN:
                return "SIN"
            case Type.COS:
                return "COS"
            case Type.VAR:
                return "VAR"
            case Type.NUM:
                return "NUM"
            case _:
                return "UNKNOWN"
            
    def __repr__(self) -> str:
        match (self):
            case Type.START:
                return "START"
            case Type.PAR:
                return "PAR"
            case Type.MUL:
                return "MUL"
            case Type.DIV:
                return "DIV"
            case Type.ADD:
                return "ADD"
            case Type.SUB:
                return "SUB"
            case Type.SIN:
                return "SIN"
            case Type.COS:
                return "COS"
            case Type.VAR:
                return "VAR"
            case Type.NUM:
                return "NUM"
            case _:
                return "UNKNOWN"
    

class Expression:
    children = []
    dtype: Type = None

    def __init__(self, children, dtype):
        self.children = children
        self.dtype = dtype

    def out(self):
        match (self.dtype):
            case Type.START:
                # print(self)
                return "{}".format(self.children[0])
            case Type.PAR:
                if self.children[0].dtype == Type.NUM:
                    return "{}".format(self.children[0])
                return "({})".format(self.children[0])
            case Type.MUL:
                return "{} * {}".format(self.children[0], self.children[1])
            case Type.DIV:
                return "{} / {}".format(self.children[0], self.children[1])
            case Type.ADD:
                return "{} + {}".format(self.children[0], self.children[1])
            case Type.SUB:
                return "{} - {}".format(self.children[0], self.children[1])
            case Type.SIN:
                return "sin({})".format(self.children[0])
            case Type.COS:
                return "cos({})".format(self.children[0])
            case Type.VAR:
                return "{}".format(self.children[0])
            case Type.NUM:
                return "{}".format(self.children[0])
            

    def __str__(self):
        # return f"{self.dtype} > {self.children}"
        return self.out()
            

    def __repr__(self):
        # return f"{self.dtype} > {self.children}"
        return self.out()