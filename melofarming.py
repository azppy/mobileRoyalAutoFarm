import pyautogui
import time
import lib.clicktenkey as clicktenkey
TIME = 0.8

path = "csv/melofarming.csv"  # pathという変数で、input.csvのパスを保持
x = []
y = []
with open(path, "r") as f:  # open関数にて開いたファイルの内容をfに保持   
    for line in f:
        x.append(line.split(",")[2])
        y.append(line.split(",")[3]) 

wait_times = [150, 320, 430, 610, 1200,1970,1]#各ループ終了後の待機時間
r = [(1, 9), (9, 17), (17, 25),(25, 33),(33, 41),(41, 49),(49, 57)]#fリストのr0行目からr1行目

for i in range(len(r)):
    pyautogui.click(1280,130)# 指定した座標にあるウィンドウをアクティブにする  
    for j in range(r[i][0], r[i][1]):
        pyautogui.click(635, 255)# 虫眼鏡をクリック
        time.sleep(TIME)# TIME秒待つ
        pyautogui.click(735,475)# X入力をクリック
        time.sleep(TIME)# TIME秒待つ
        num=x[j]#j回目のxを抽出
        num=int(num)#整数へ変換
        clicktenkey.function(num)
        pyautogui.click (1160,625)#X入力チェック
        time.sleep(TIME)
    
        pyautogui.click(880,475)# Y入力をクリック
        time.sleep(TIME)# TIME秒待つ
        num=y[j]#i回目のyを抽出
        num=int(num)#整数へ変換
        clicktenkey.function(num)
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