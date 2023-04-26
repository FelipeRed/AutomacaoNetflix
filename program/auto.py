import pyautogui
import os
import time

while True:
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))  # Obtem o diretório atual do script

        # Para construir o caminho do arquivo PNG: file_path = os.path.join(script_dir, 'nome_do_arquivo.png')

        # Tenta encontrar a imagem na tela
        imagem = os.path.join(script_dir, 'btn_PularAbertura.png')  # Construindo o caminho do arquivo
        botao = pyautogui.locateOnScreen(imagem)
        botaoClicado = "pular abertura"
        if botao is None:  # Caso não tenha encontrado o botão "Pular Abertura" irá buscar o botão "Pular Resumo"
            imagem = os.path.join(script_dir, 'btn_PularResumo.png')
            botao = pyautogui.locateOnScreen(imagem)
            botaoClicado = "pular resumo"
        if botao is None:
            time.sleep(2)
            continue
        else:  # Caso encontre algum dos botões irá clicar e depois esperar 18 minutos
            time.sleep(0.5)
            botaoPoint = pyautogui.center(botao)
            buttonX, buttonY = botaoPoint
            pyautogui.click(buttonX, buttonY)
            if botaoClicado == "pular abertura":
                time.sleep(1080)

    except pyautogui.ImageNotFoundException:
        print("ERRO: Imagem não encontrada na tela.")
        continue
