import time
import lib.tenkey as tenkey

def function(num):
    '''座標を検索しクリック　　座標３桁の数をnumに渡すとテンキーをクリックする.numへの入力は直接またはCSVデータを使う。　　X,Yの指定はないのでそれぞれにimportすること。'''

    TIME = 0.8
    num=int(num)#整数へ変換
    place100 = num // 100  # 100の位
    place10 = (num - place100 * 100) // 10  # 10の位
    place1 = num - place100 * 100 - place10 * 10  # 1の位

    num = place100
    tenkey.number(num)#100の位tenkeyから呼び出す
    time.sleep(TIME)# TIME秒待つ
    num = place10
    tenkey.number(num)#10の位tenkeyから呼び出す
    time.sleep(TIME)# TIME秒待つ
    num = place1
    tenkey.number(num)#1の位tenkeyから呼び出す
    time.sleep(TIME)# TIME秒待つ
