import cv2
import numpy as np
import streamlit as st
from PIL import Image

st.title("Trabalho de Computação Gráfica")

foto = Image.open("imagens/foto2.jpg")
img = np.array(foto)

st.header("2. Brilho")

col1, col2 = st.columns(2)
fator = col1.slider("Brilho", 0.0, 2.55, 1.5)
hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
v = hsv[:, :, 2].astype(float) * fator
hsv2 = hsv.copy()
hsv2[:, :, 2] = np.clip(v, 0, 255)
col1.image(img, caption="Normal")
col2.image(cv2.cvtColor(hsv2, cv2.COLOR_HSV2RGB), caption="Brilho")

st.header("8. Negativo")

col1, col2 = st.columns(2)
negativo = 255 - img
col1.image(img, caption="Normal")
col2.image(negativo, caption="Negativo")

st.header("9. Recorte")

col1, col2 = st.columns(2)
x = col2.slider("X posição", 0, img.shape[1] - 200, 59)
y = col2.slider("Y posição", 0, img.shape[0] - 200, 163)
recorte = img[y:y + 200, x:x + 200]
col1.image(img, caption="Normal")
col2.image(recorte, caption="Recorte")

st.header("12. Simetria")

col1, col2 = st.columns(2)
simetrica = img.copy()
meio = img.shape[1] // 2
esquerda = simetrica[:, :meio]
simetrica[:, meio:] = esquerda[:, ::-1]
col1.image(img, caption="Normal")
col2.image(simetrica, caption="Simétrica")

st.header("20. Pixel art")

col1, col2 = st.columns(2)
tamanho = col1.slider("Tamanho", 2, 15, 5)
pequena = img[::tamanho, ::tamanho]
pixelada = pequena.repeat(tamanho, axis=0).repeat(tamanho, axis=1)
pixelada = pixelada[:img.shape[0], :img.shape[1]]
col1.image(img, caption="Normal")
col2.image(pixelada, caption="Pixel art")