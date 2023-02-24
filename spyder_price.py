# 量化投资第一部分，爬虫取价格
import requests
from time import sleep
import tushare
import talib as ta
# mytoken='19daf5d0248695483d961699537e768560bf359f240a0d4c084b08c1'
ts.set_token
def getTick():
    '''
    go to Tencent to get the last price
    :return:
    '''
    page = requests.get('https://qt.gtimg.cn/q=sh600036')
    stock_info = page.text
    mt_info = stock_info.split("~")
    close = mt_info[3]
    last = float(mt_info[1])
    trade_datetime = mt_info[30] + ' ' + mt_info[31]

    tick = (last, trade_datetime)
    return tick


v_sh600036 = "1~招商银行~600036~37.46~38.27~38.17~533690~244937~288753~37.46~1469~37.45~1576~37.44~974~37.43~547~37.42~448~37.47~158~37.48~117~37.49~104~37.50~698~37.51~6~~20230224150003~-0.81~-2.12~38.25~37.40~37.46/533690/2011474600~533690~201147~0.26~6.85~~38.25~37.40~2.22~7727.60~9447.35~1.14~42.10~34.44~0.91~3931~37.69~6.85~6.85~~~1.34~201147.4600~0.0000~0~ ~GP-A~0.54~2.04~4.06~14.49~1.39~48.98~26.30~-1.83~-8.75~16.26~20628944429~25219845601~64.47~-1.85~20628944429~~~-22.76~-0.21~~CNY";
while True:
    last_tick = getTick()
    print(last_tick)
    sleep(3)
