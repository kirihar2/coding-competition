from balancedparens import balanced
class Calculator():
    def __init__(self): 
        self.parens = []
        self.nums = []
        pass
    def calculate(self,expr): 
        def isOperator(c):
            return c is '+' or c is '*' or c is '-' or c is '/'
        def isParens(c): 
            return c is '(' or c is ')'
        if not balanced(expr):
            return False 
        
        for c in expr: 
            pass