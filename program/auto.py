import pyautogui
import time

def pular_aberturas(iteracoes):
    # Essa função pula a abertura de no máximo 5 episódios
    if iteracoes == 5:
        return

    acao_realizada = ""
    while acao_realizada != "Pular Abertura":
        # Tenta localizar a imagem na tela (capturando o seu centro)
        botao = pyautogui.locateCenterOnScreen("btn_PularAbertura.png", confidence = 0.7)
        if botao is not None:
            acao_realizada = "Pular Abertura"
            pyautogui.click(botao.x, botao.y)
            continue

        botao = pyautogui.locateCenterOnScreen("btn_PularResumo.png", confidence = 0.7)
        if botao is not None:
            pyautogui.click(botao.x, botao.y)
            print("Botão de Pular Resumo encontrado.")
            continue

        print("Buscando...")
        time.sleep(1)

    print("Botão de Pular Abertura encontrado.")
    print("Sleep de 10 minutos.")
    time.sleep(600)  # Espera 10 minutos até chamar a função recursivamente
    pular_aberturas(iteracoes + 1)

# "Main"
pular_aberturas(0)
