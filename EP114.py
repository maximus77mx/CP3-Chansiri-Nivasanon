from forex_python.bitcoin import *
import datetime,decimal


def getBTCprice():
    sum = 0
    b = BtcConverter()
    for i in range(1,31):
        date_obj = datetime.datetime(2021, 1, i)
        sum += b.get_previous_price('THB', date_obj)
        avg_bitcoin = sum
        print("Avg. Price : ", round(avg_bitcoin), "THB")
        result = b.get_latest_price('THB')
        print("Current Price: ", round(result), "BTH")
        increse = (result - avg_bitcoin)/avg_bitcoin * 100
        print("increase: ", round(increse), "%")

getBTCprice()