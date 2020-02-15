import pybithumb

btc = pybithumb.get_ohlcv("BTC")
close = btc['close']

ma5 = close.rolling(5).mean()
ma10 = close.rolling(10).mean()

print(ma5)
print(ma10)