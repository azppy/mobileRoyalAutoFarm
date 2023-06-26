import pyautogui
import time
import csv
from lib import clicktenkey
TIME = 0.8

path = "csv/kuromimifarming.csv"

x = []
y = []
dur = []

with open(path, 'r') as f:  # CSVファイルからデータを読み込みながら処理
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        x.append(int(row[2]))
        y.append(int(row[3]))
        dur.append(int(row[4])) 
target_times = []  # 目標時刻を保持するリスト

def farming():
    for i in range(len(dur)):
        pyautogui.click(1280, 130)  # 指定した座標にあるウィンドウをアクティブにする
        pyautogui.click(635, 255)  # 虫眼鏡をクリック
        time.sleep(TIME)  # TIME秒待つ
        pyautogui.click(735, 475)  # X入力をクリック
        time.sleep(TIME)  # TIME秒待つ

        num = int(x[i])  # i回目のxを抽出
        clicktenkey.function(num)
        pyautogui.click(1160, 625)  # X入力チェック
        time.sleep(TIME)

        pyautogui.click(880, 475)  # Y入力をクリック
        time.sleep(TIME)  # TIME秒待つ
        num = int(y[i])  # i回目のyを抽出
        clicktenkey.function(num)
        pyautogui.click(1160, 625)  # Y入力チェック
        time.sleep(TIME)

        pyautogui.click(720, 605)  # 座標スタート
        time.sleep(TIME)
        pyautogui.click(720, 480)  # 攻撃/中央選択
        time.sleep(TIME)
        pyautogui.click(960, 755)  # 攻撃選択
        time.sleep(TIME)
        pyautogui.click(730, 285)  # ヒーロー選択
        time.sleep(TIME)
        pyautogui.click(610, 582)  # 騎兵選択
        time.sleep(TIME)
        pyautogui.click(1040, 730)  # OK
        time.sleep(TIME)

        target_time = time.time() + dur[i]   # 現在時刻に所要時間を加算して目標時刻を計算
        target_times.append(target_time)  # 目標時刻をリストに追加

        while len(target_times) >= 8:
            if target_times and target_times[0] <= time.time():
                target_times.pop(0)
                time.sleep(1)
        else:
            time.sleep(1)

if __name__ == "__main__": 
    farming()
