import pyautogui

windows = pyautogui.getWindows()
current_windows = list(filter(lambda w: w.title == 'sunBrowser', windows))
