import pybithumb
import time

while True:
    try:
        price = [pybithumb.get_current_price("BTC"), pybithumb.get_current_price("ETH"), pybithumb.get_current_price("XRP")]

        print("BTC : %.0f" % price[0])
        print("ETH : %.0f" % price[1])
        print("XRP : %.1f" % price[2])

        time.sleep(1)
    except:
        print("error occurs")