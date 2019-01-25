class MyCalendarTwo:

    def __init__(self):
        self.arr =[]

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        count = 0 
        for booking in self.arr:
            if (start < booking[1] and start >= booking[0]) or (end < booking[1] and end > booking[0]): 
                count+=1
            if count >=2: 
                return False
        self.arr.append([start,end])
        return True
    def __repr__(self):
        return ",".join(map(str,self.arr))

val = [[10,20],[50,60],[10,40],[5,15],[5,10],[25,55]]
cal = MyCalendarTwo()
ret = []
for i in range(len(val)):
    ret.append(cal.book(val[i][0],val[i][1]))
print(ret)