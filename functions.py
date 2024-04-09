import math

class Operate():
    def __init__(self):
        self.num1 = None
        self.num2 = None
        self.result = None
        self.operator = None
        self.clean = None
        self.eq = None
        self.val = None

    def get_clean(self):
        return self.clean

    def get_operator(self):
        return self.operator

    def set_clean(self, pc):
        self.clean = pc

    def reset(self):
        self.num1 = None
        self.num2 = None
        self.result = 0
        self.operator = None

    def calc(self, op, tb_val):
        num1= None
        num2 = None
        
        if op == "√":
            self.result = math.sqrt(self.result)
            self.clean = 0
            self.num2 = None
            self.operator = None
            self.num1 = self.result
            return str(self.result)
        
        if self.operator is None:
            self.operator = op
            self.num1 = tb_val
            self.clean = 0
            return str(tb_val)
        else:
            self.num2 = tb_val
            # else:
            #     self.num1 = tb_val
            #     self.clean = 0
            #     return tb_val 
        if "." in (self.num1):
            num1= float(self.num1)
        else:
            num1= int(self.num1)
        
        if "." in (self.num2):
            num2 = float(self.num2)
        else:
            num2 = int(self.num2)              
        
        if self.operator == "+":
            self.result = (num1 + num2)
        elif self.operator == "-":
            self.result = (num1 - num2)
        elif self.operator == "*":
            self.result = (num1 * num2)
        elif self.operator == "/":
            self.result = (num1 / num2)
        elif self.operator == "√":
            self.result = math.sqrt(self.result)

        self.clean = 0
        self.num2 = None
        self.operator = None
        self.num1 = self.result
        return str(self.result)

    
    