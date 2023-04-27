import pyautogui
import os
import time

# Ainda não descobri o porque, mas o código está com um problema onde a cada vez que eu fecho o Pycharm e abro de novo
# ele não encontra mais os botões na tela, a não ser que eu tire print novamente e sobrescreva os arquivos de imagem

os.chdir(os.path.dirname(os.path.abspath(__file__)))
minutos_Ep = input("Insira quantos minutos têm cada episódio da série que você vai assistir: ")
tempo_Pausa = (int(minutos_Ep) * 60) - 240  # Transforma os minutos do input em segundos e diminui 4 minutos desse tempo
while True:
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))  # Obtem o diretório atual do script

        # Para construir o caminho do arquivo PNG: file_path = os.path.join(script_dir, 'nome_do_arquivo.png')
        imagem = os.path.join(script_dir, "btn_PularAbertura.png")
        botao = pyautogui.locateOnScreen(imagem)  # Tenta encontrar a imagem na tela
        botaoClicado = "pular abertura"
        if botao is None:  # Caso não tenha encontrado o botão "Pular Abertura" irá buscar o botão "Pular Resumo"
            imagem = os.path.join(script_dir, "btn_PularResumo.png")
            botao = pyautogui.locateOnScreen(imagem)
            botaoClicado = "pular resumo"
        if botao is None:
            print("Buscando...")
            time.sleep(2)
            continue
        else:  # Caso encontre algum dos botões irá clicar e depois esperar tempo_Pausa segundos
            time.sleep(0.5)
            botaoPoint = pyautogui.center(botao)
            buttonX, buttonY = botaoPoint
            pyautogui.click(buttonX, buttonY)
            if botaoClicado == "pular abertura":
                print("Pausando o programa por " + str(int(minutos_Ep) - 4) + " minutos.\n")
                time.sleep(tempo_Pausa)  # Pausará o programa pela quantidade de minutos do episódio menos 4 minutos

    except pyautogui.ImageNotFoundException:
        print("ERRO: ImageNotFoundException.")
        continue
