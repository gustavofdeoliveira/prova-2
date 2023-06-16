import numpy as np
import cv2 as cv

# Abre o arquivo de video
input_video = cv.VideoCapture('./assets/arsene.mp4')

# Checa se foi possivel abrir o arquivo
if not input_video.isOpened():
    print("Error opening video file")
    exit(1)
    
# tamanho do video
width  = int(input_video.get(cv.CAP_PROP_FRAME_WIDTH))   # float `width`
height = int(input_video.get(cv.CAP_PROP_FRAME_HEIGHT))

# importa o arquivo xml com o modelo de detecção
haar_cascade = cv.CascadeClassifier('haar_cascade.xml')
# Define o tamanho do video de saida
size = (width, height)
# Define o codec e cria o arquivo de video de saida
output_video = cv.VideoWriter('./exemplos/saida/out.avi', 
                         cv.VideoWriter_fourcc(*'MJPG'),
                         10, size)

# Loop de leitura frame por frame
while True:
    # Le o frame de entrada
    ret, frame = input_video.read()
    # Se nao conseguiu ler o frame, para o laço
    if not ret:
        break
    # Transforma o frame em escala de cinza
    gray_img = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Detecta as faces no frame
    faces_rect = haar_cascade.detectMultiScale(gray_img, 1.1, 9)
    for (x, y, w, h) in faces_rect:
        cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Salva o frame no video de saida
    output_video.write(frame)
    # Exibe o frame
    cv.imshow('Video Playback', frame)
    
    # Checa se o usuario apertou a tecla 'q' e fecha
    if cv.waitKey(30) & 0xFF == ord('q'):
        break
    
# Fecha tudo
output_video.release()
input_video.release()
cv.destroyAllWindows()