import pyautogui
import time
import webbrowser

def pesquisar_no_youtube(termo_de_pesquisa):
    webbrowser.open("https://www.youtube.com")
    time.sleep(3)

    pyautogui.click(1150, 218)
    time.sleep(2)
    pyautogui.write(termo_de_pesquisa, interval=0.2)
    pyautogui.press("enter")

termo=input("digite o termo de pesquisa: ")
print(termo)