import pyautogui
import time

# pyautogui.locateCenterOnScreen tenta localizar a imagem na tela (capturando o seu centro)
# Confidence é um parâmetro que determina quão igual a imagem encontrada deve ser (nesse caso 70%)
def pular_aberturas(n_vezes):  # n_vezes é o número de aberturas que o código irá pular
    imagens = ["btn_PularAbertura.png", "btn_PularResumo.png"]
    for i in range(n_vezes):
        abertura_pulada = False
        while not abertura_pulada:
            for img in imagens:
                botao = pyautogui.locateCenterOnScreen(img, confidence=0.7)
                if botao is not None:
                    pyautogui.click(botao.x, botao.y)
                    if img == "btn_PularAbertura.png":
                        abertura_pulada = True
                print("Buscando...")
                time.sleep(1)
        print("Botão de Pular Abertura encontrado.")
        print("Sleep de 10 minutos.")
        time.sleep(600)

# "Main"
pular_aberturas(5)
