'''
Find Itinerary from a given list of tickets
Given a list of tickets, find itinerary in order using the given list.

Example:

Input:
"Chennai" -> "Banglore"
"Bombay" -> "Delhi"
"Goa"    -> "Chennai"
"Delhi"  -> "Goa"

Output: 
Bombay->Delhi, Delhi->Goa, Goa->Chennai, Chennai->Banglore,
'''
def solve(arr): 
    d = {}
    start = set()
    for pair in arr: 
        start.add(pair[1])
        d[pair[0]]=pair[1]

    start_city = ""
    for pair in arr: 
        if pair[0] not in start: 
            start_city = pair[0]
            break
    while start_city in d: 
        print(start_city)
        start_city = d[start_city]
    print(start_city)

arr = [
["Chennai", "Banglore"],
["Bombay" ,"Delhi"],
["Goa"    ,"Chennai"],
["Delhi"  ,"Goa"]
]
solve(arr)