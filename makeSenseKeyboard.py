import pyautogui
from pynput import keyboard

x1, y1 = 2998, 1063  # 'd' tuşu için hedef koordinat
x2, y2 = 2766, 1060  # 'a' tuşu için hedef koordinat


def click_position(x, y):
    current_position = pyautogui.position()
    pyautogui.click(x, y)
    pyautogui.moveTo(current_position)  # Mouse'u eski pozisyona geri getir


def on_press(key):
    try:
        if key.char == "d":
            click_position(x1, y1)
            print(f"'d' tuşuna basıldı. ({x1}, {y1}) noktasına tıklandı.")

        elif key.char == "a":
            click_position(x2, y2)
            print(f"'a' tuşuna basıldı. ({x2}, {y2}) noktasına tıklandı.")

    except AttributeError:
        pass


with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
