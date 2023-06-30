import pyautogui
import time

i = 0
while i < 5000:
        
  pyautogui.click(1280, 130)  # 指定した座標にあるウィンドウをアクティブにする
  pyautogui.click(1120, 680)  # ヘルプをクリック
  time.sleep(1)  # TIME秒待つ

  i += 1