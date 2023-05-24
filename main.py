import pyautogui
import time
import tenkey
TIME=0.8

path = "input.csv"  # pathという変数で、input.csvのパスを保持
x = []
y = []
with open(path, "r") as f:  # open関数にて開いたファイルの内容をfに保持   
    for line in f:
        x.append(line.split(",")[2])
        y.append(line.split(",")[3]) 

pyautogui.click(1280,130)# 指定した座標にあるウィンドウをアクティブにする  

wait_times = [5, 480, 720, 1350, 1860]#各ループ終了後の待機時間
r = [(1, 14), (14, 22), (22, 30),(30, 38),(38, 46),(46,54)]#fリストのr0行目からr1行目

for i in range(len(r)):
    for j in range(r[i][0], r[i][1]):
        num = x[j]

        pyautogui.click(635, 255)# 虫眼鏡をクリック
        time.sleep(TIME)# TIME秒待つ
        pyautogui.click(735,475)# X入力をクリック
        time.sleep(TIME)# TIME秒待つ

        num=x[j]#j回目のxを抽出
        num=int(num)#整数へ変換
        place100 = num/100#100の位
        place100=int(place100)#整数へ変換
        place10 = (num - place100*100)/10#10の位
        place10=int(place10)#整数へ変換
        place1 = (num - place100*100 - place10*10)#1の位
        place1=int(place1)#整数へ変換
    
        num = place100
        tenkey.number(num)#100の位tenkeyから呼び出す
        time.sleep(TIME)# TIME秒待つ
        num = place10
        tenkey.number(num)#10の位tenkeyから呼び出す
        time.sleep(TIME)# TIME秒待つ
        num = place1
        tenkey.number(num)#1の位tenkeyから呼び出す
        time.sleep(TIME)# TIME秒待つ
        pyautogui.click (1160,625)#X入力チェック
        time.sleep(TIME)
    
        pyautogui.click(880,475)# Y入力をクリック
        time.sleep(TIME)# TIME秒待つ
        num=y[j]#i回目のyを抽出
        num=int(num)#整数へ変換
        place100 = num/100#100の位
        place100=int(place100)#整数へ変換
        print(place100)
        place10 = (num - place100*100)/10#10の位
        place10=int(place10)#整数へ変換
        print(place10)
        place1 = (num - place100*100 - place10*10)#1の位
        place1=int(place1)#整数へ変換
        print(place1)
    
        num = place100
        print (num)
        tenkey.number(num)#100の位tenkeyから呼び出す
        time.sleep(TIME)# TIME秒待つ
        num = place10
        print (num)
        tenkey.number(num)#10の位tenkeyから呼び出す
        time.sleep(TIME)# TIME秒待つ
        num = place1
        print (num)
        tenkey.number(num)#1の位tenkeyから呼び出す
        time.sleep(TIME)# TIME秒待つ
        pyautogui.click (1160,625)#Y入力チェック
        time.sleep(TIME)

        pyautogui.click (720,605)#座標スタート
        time.sleep(TIME)

        pyautogui.click (720,480)#攻撃/中央選択
        time.sleep(TIME)

        pyautogui.click (960,755)#攻撃選択
        time.sleep(TIME)

        pyautogui.click (730,285)#ヒーロー選択
        time.sleep(TIME)

        pyautogui.click (610,582)#騎兵選択
        time.sleep(TIME)

        pyautogui.click (1040,730)#OK
        time.sleep(TIME)
    time.sleep(wait_times[i])#次のループ開始までの待機時間