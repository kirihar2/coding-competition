class Solution(object):
    def invalidTransactions(self, transactions):
        """
        :type transactions: List[str]
        :rtype: List[str]
        """
        names = {}
        ret= set()
        
        for i in range(len(transactions)):
            transaction = transactions[i]
            name,time,amount,city = transaction.split(",")
            time = int(time)
            if int(amount) > 1000:
                ret.add(i)
            if name not in names:
                names[name]=[]
            else:
                for curr in names[name]:
                    ind,t,c = curr
                    t = int(t)
                    if abs(t-time) <=60 and c != city:
                        if ind not in ret:
                            ret.add(ind)
                        if i not in ret:
                            ret.add(i)
                        break
            names[name].append([i,time,city])
        d = []
        for i in ret:
            d.append(transactions[i])
        return d
t=["xnova,261,1949,chicago","bob,206,1284,chicago","xnova,420,996,bangkok","chalicefy,704,1269,chicago","iris,124,329,bangkok","xnova,791,700,amsterdam","chalicefy,572,697,budapest","chalicefy,231,310,chicago","chalicefy,763,857,chicago","maybe,837,198,amsterdam","lee,99,940,bangkok","bob,132,1219,barcelona","lee,69,857,barcelona","lee,607,275,budapest","chalicefy,709,1171,amsterdam"]
sol = Solution()
print(sol.invalidTransactions(t))