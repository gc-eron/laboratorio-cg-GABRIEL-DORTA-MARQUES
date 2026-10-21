import numpy as np
import streamlit as st

def ampliar(imagem, k=30):
    return imagem.repeat(k, axis=0).repeat(k, axis=1)

#a = np.array([10, 20, 30])
#v = np.array([10, 20, 30])
#m = np.array([[10, 20, 30],
#            [40, 50, 60]])
#c = np.array([[[1, 2], [3, 4]],
#            [[5, 6], [7, 8]]])
#st.title("Imagem como matriz")
#img3 = np.array([[1,2],[1,1]])
#img2 = np.zeros([8,8], dtype=np.uint8)

#img2[2][5] = 255

#img2[4:][:] = 128
#st.write(img3)
#st.image(ampliar(img3), width=255)
#st.write(img2)
#st.image(ampliar(img2), width=255)

#img = np.zeros((6, 9, 3), dtype=np.uint8)
#img[:2, :] = (110, 50, 150)
#img[2:4, :] = (240, 190, 40)
#img[4:, :] = (30, 160, 150)
#st.image(ampliar(img))

bandeira = np. zeros((11,14,3), dtype=np.uint8)
#Verde
bandeira[:, :] = (0, 180, 0)

#Amarelo
bandeira[1,5:9] = (180,180,0)
bandeira[2,4:10] = (180,180,0)
bandeira[3,3:11] = (180,180,0)
bandeira[4,2:12] = (180,180,0)
bandeira[5,1:13] = (180,180,0)
bandeira[6,2:12] = (180,180,0)
bandeira[7,3:11] = (180,180,0)
bandeira[8,4:10] = (180,180,0)
bandeira[9,5:9] = (180,180,0)

#Azul
bandeira[3,6:8] = (0,0,160)
bandeira[4,5:9] = (0,0,160)
bandeira[5,4:10] = (0,0,160)
bandeira[6,5:9] = (0,0,160)
bandeira[7,6:8] = (0,0,160)

#branco
bandeira[4,6] = (200,200,200)
bandeira[4,7] = (200,200,200)
bandeira[5,8] = (200,200,200)

st.image(ampliar(bandeira))



