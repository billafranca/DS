import pyautogui
import time
import webbrowser


def pesquisar_no_chatgpt(termo_de_busca):
    webbrowser.open("https://chatgpt.com")
    time.sleep(5)

    pyautogui.click()
    pyautogui.moveTo(800, 218, duration=1)
    

    pyautogui.click(1150, 218)
    pyautogui.position()
    pyautogui.click()
    time.sleep(1)
    pyautogui.write(termo_de_busca, interval=0.1)
    pyautogui.press("enter")


termo_de_busca = input("Digite o termo de busca: ")
pesquisar_no_chatgpt(termo_de_busca)

