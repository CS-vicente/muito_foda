#importa as bibliotecas

#cv2 é para as cores
import cv2 #type: ignore
#numeros das cores (rgb)
import numpy as np
#para salvar o nome das fotos e individualmente
from datetime import datetime
#para salvar em pasta diferente
import os

#para acessar a camera
webcam = cv2.VideoCapture(0)

#se não foi acessada da erro
if not webcam.isOpened():
    print("Erro: Não foi possível acessar a webcam.")
    exit()

print("Posicione o objeto no centro do retângulo e pressione 'S' para foto ou 'Q' para sair.")

#ve se tirou a foto
foto_capturada = None
#loop infinito para atualizar a imagem da câmera continuamente
while True:
#le o quadro (frame) atual da câmera
    sucesso, frame = webcam.read()
    if not sucesso:
        print("Erro ao capturar o vídeo.")
        break
#calcula o tamanho da tela (imagem)
    h_f, w_f, _ = frame.shape
#calcula o ponto central exato da tela.
    cx, cy = w_f // 2, h_f // 2
#tamanho do quadrado central
    r_size = 50
#desenha o quadrado verde
    cv2.rectangle(frame, (cx - r_size, cy - r_size), (cx + r_size, cy + r_size), (0, 255, 0), 2)
#exibe o frame atual na janela (camera)
    cv2.imshow("Webcam ao Vivo", frame)
#aguarda 1 milisegundo para digitar tecla
    tecla = cv2.waitKey(1) & 0xFF
#tira a foto com a tecla S, além de mover para outra pasta
    if tecla in (ord('s'), ord('S')):
        foto_capturada = frame.copy()
        pasta_destino = "capturas_fotos"
        os.makedirs(pasta_destino, exist_ok=True)
# gera um nome de arquivo usando a data e hora atual
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        nome_arquivo = f"foto_{timestamp}.jpg"
#salva pasta destino
        caminho_completo = os.path.join(pasta_destino, nome_arquivo)
        cv2.imwrite(caminho_completo, foto_capturada)
#mostra caminho da foto
        print(f"Foto salva com sucesso em: {caminho_completo}")
        break
#se apertar Q sai da camera
    elif tecla in (ord('q'), ord('Q')):
        print("Programa encerrado sem salvar foto.")
        break

#tira a aba da camera dps da foto
webcam.release()
#fecha todas as janelas opencv
cv2.destroyAllWindows()
#se apertar q encerra
if foto_capturada is None:
    print("Nenhuma imagem capturada.")
    exit()
#apenal a cor do quadrado central
roi = foto_capturada[cy - r_size:cy + r_size, cx - r_size:cx + r_size]
#cor predominante
media_bgr = cv2.mean(roi)[:3]
#converte em media de cor
b, g, r = int(media_bgr[0]), int(media_bgr[1]), int(media_bgr[2])

def obter_dados_hsv(b, g, r):
    pixel_bgr = np.uint8([[[b, g, r]]])
    pixel_hsv = cv2.cvtColor(pixel_bgr, cv2.COLOR_BGR2HSV)
    return pixel_hsv[0][0]  # h (matriz, cor em si), s(saturação), v(brilho, clara ou escura)
#nome da cor
def identificar_cor_nome(h, s, v):
#cores acromáticas e neutras escuras/claras
    if v < 40:
        return 'Preto'
    if s < 25 and v > 200:
        return 'Branco'
    
    if 10 <= h < 35 and 20 <= s < 80 and v > 160:
        return 'Bege'
        
    if (h < 22 or h >= 165) and 30 <= s < 220 and 40 <= v < 150:
        return 'Marrom'

    if s < 30:
        return 'Cinza'
    
    if h < 10 or h >= 165:
        return 'Vermelho'
    elif 10 <= h < 25:
        return 'Laranja'
    elif 25 <= h < 35:
        return 'Amarelo'
    elif 35 <= h < 85:
        return 'Verde'
    elif 85 <= h < 130:
        return 'Azul'
    elif 130 <= h < 165:
        return 'Roxo / Rosa'
    
    return 'Indefinido'
#circulo cromatico combinações
def obter_cor_complementar(h, s, v, nome_cor):
#se for cor neutra ou marrom retorna uma dica fixa
    """Sugere combinações com base na teoria das cores ou tons neutros."""
    if nome_cor in ['Preto', 'Branco', 'Cinza', 'Bege']:
        return 'Cores neutras (combinam bem com Marinho, Vinho ou Tons Terrosos)'
    if nome_cor == 'Marrom':
        return 'Azul Claro ou Verde Oliva'
#para cores cromáticas, calcula o tom oposto no círculo cromático somando 90 graus na escala do OpenCV (+ 90 % 180) e reutiliza a função de identificação para retornar a cor oposta/complementar.
    h_complementar = (int(h) + 90) % 180
    return identificar_cor_nome(h_complementar, s, v)
#roda os defs
h, s, v = obter_dados_hsv(b, g, r)
cor_detectada = identificar_cor_nome(h, s, v)
cor_combina = obter_cor_complementar(h, s, v, cor_detectada)

print(f'A cor detectada é: {cor_detectada}')
print(f'A cor complementar que combina mais é: {cor_combina}')


# fala a cor final na tela
cv2.rectangle(foto_capturada, (cx - r_size, cy - r_size), (cx + r_size, cy + r_size), (0, 255, 0), 2)
# fala a cor final na tela
cv2.putText(foto_capturada, f'Cor: {cor_detectada}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
cv2.imshow('Foto Processada', foto_capturada)
#exibe a imagem final processada até que qualquer tecla seja pressionada
cv2.waitKey(0)
cv2.destroyAllWindows()

