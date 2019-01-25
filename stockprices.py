def get_max_profit(stock_prices):
  ret = -100000000
  min_price = stock_prices[0]
  for i in range(1,len(stock_prices)):
    price =  stock_prices[i] - min_price
    ret = max(price,ret)
    min_price = min(min_price,stock_prices[i])
  return ret 




stock_prices = [10, 7, 5, 8, 11, 9]
#stock_prices = [10,7,6,3]
print(get_max_profit(stock_prices))