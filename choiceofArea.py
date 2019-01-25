'''
Choice of Area
Consider a game, in which you have two types of powers, A and B and there are 3 types of Areas X, Y and Z. Every second you have to switch between these areas, each area has specific properties by which your power A and power B increase or decrease. We need to keep choosing areas in such a way that our survival time is maximized. Survival time ends when any of the powers, A or B reaches less than 0.
Examples:

Initial value of Power A = 20        
Initial value of Power B = 8

Area X (3, 2) : If you step into Area X, 
                A increases by 3, 
                B increases by 2

Area Y (-5, -10) : If you step into Area Y, 
                   A decreases by 5, 
                   B decreases by 10

Area Z (-20, 5) : If you step into Area Z, 
                  A decreases by 20, 
                  B increases by 5

It is possible to choose any area in our first step.
We can survive at max 5 unit of time by following 
these choice of areas :
X -> Z -> X -> Y -> X
'''

def solve(arr,a,b):
    x = arr[0]
    y = arr[1]
    z = arr[2]

    
    def recur(a,b,prev,dp):
        if a <= 0 or b <= 0: 
            return 0
        if (a,b) in dp: 
            return dp[(a,b)]
        if prev == 1: 
            temp = max(recur(a+y[0],b+y[1],2,dp),recur(a+z[0],b+z[1],3,dp))
        elif prev == 2:
            temp = max(recur(a+x[0],b+x[1],1,dp),recur(a+z[0],b+z[1],3,dp))
        elif prev == 3: 
            temp = max(recur(a+x[0],b+x[1],1,dp),recur(a+y[0],b+y[1],2,dp))
        dp[(a,b)] = temp + 1
        return temp +1 
    return max(recur(a+x[0],b+x[1],1,{}),recur(a+y[0],b+y[1],2,{}),recur(a+z[0],b+z[1],3,{}))
arr = [(3,2),(-5,-10),(-20,5)]
a = 20 
b = 8 
print(solve(arr,a,b))