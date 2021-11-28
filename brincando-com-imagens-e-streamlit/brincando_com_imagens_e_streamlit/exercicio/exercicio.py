import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
from PIL import Image

R = 0
G = 1 
B = 2

st.write('## testando as imagems')

st.sidebar.write('### configuração')

uploaded_file = st.sidebar.file_uploader("selecione uma imagem", 
    type=['png','jpg']
)

if upload_arquivos is not None:
    image_link = Image.open(uploaded_file)

    img = np.asarray(image_link)
    

    coluna, coluna1 = st.columns(2)

    with coluna:
       
        st.write('### Imagem original')

        st.image(img)
     

    with col2:
        pesos = [0.2126, 0.7152, 0.0722]
        image_ciza_correcao = np.copy(image)   
        image_cinza_correcao = np.array(image_gray_corr * pesos, dtype=np.uint8)
        image_cinza_correcao = np.array(np.sum(image_gray_corr, axis=2), dtype=np.uint8)

        st.write('### tons de cinza')
        # st.latex(r'''
        #     Y_{linear} = 0.2126R_{linear} 
        #         + 0.7152G_{linear}
        #         + 0.0722B_{linear}
        # ''')
        st.image(image_cinza_correcao)

    opt = st.sidebar.selectbox(
        'Qual é a transformação?',
        (None, 'negativo', 'log', 'power-law (gamma)'),
    )

    img_temp = np.copy(image_cinza_correcao)

    st.write(f'## {opt}'.upper())

    if opt == 'negativo':
        img_temp = 255 - imag_temp
    elif opt == 'log':
        st.sidebar.latex(r'''
            s = c \times log(1 + r)
        ''')

        c = st.sidebar.slider(
            'c',
            0, 100, 25
        )

        st.write('c:', c)

        img_temp_array = c * (np.log(image_aux + 1))
        image_temp = Image.fromarray(img_temp_array.astype(np.uint8)).convert('L')

        fig, ax = plt.subplots()
        ax.hist(img_temp_array.astype(np.uint8).flatten(), bins=20)
        st.sidebar.pyplot(fig)

    elif option == 'power-law (gamma)':
        st.sidebar.latex(r'''
            s = c \times r^\gamma
        ''')

        c = st.sidebar.slider(
            'c',
            0, 255, 25
        )

        gamma = st.sidebar.slider(
            'gamma',
            0.0, 25.0, 1.0, 0.02
        )

        st.write(f"c: {c}, gamma: {gamma}")

        img_temp_array = c * ((image_aux/255) ** gamma)
        image_temp = Image.fromarray(img_temp_array.astype(np.uint8)).convert('L')

        fig, ax = plt.subplots()
        ax.hist(img_temp_array.astype(np.uint8).flatten(), bins=5)
        st.sidebar.pyplot(fig)
    # img_temp_array.astype(int)
    # st.write(img_temp_array.astype)
    st.image(image_temp)


    # elif(option == 'Transformação em (log)'):
        
    #     c = st.sidebar.slider('c', 0, 130, 25)
    #     if color == 'tons de cinza':
    #         log_image_arr = c * (np.log(gray_arr + 1))
    #         image = Image.fromarray(log_image_arr).convert('L')
    #         # image = Image.fromarray(255 - gray_arr).convert('L') 
    #     else:
    #         image[:,:,0] = c * (np.log(image[:,:,0] + 1))
    #         image[:,:,1] = c * (np.log(image[:,:,1] + 1))
    #         image[:,:,2] = c * (np.log(image[:,:,2] + 1))
    #         image = Image.fromarray(image).convert('L')

    image_temp
    opt = st.sidebar.selectbox(
        'Qual o nível de cores?',
        (2, 4, 8, 16, 32, 64, 128, 192, 256),
    )

    image_temp = np.copy(image_cinza_correcao)
    # if opt == 2:
    #     image_temp[image_temp > 127] = 255
    #     image_aux[image_temp < 127] = 0
    # elif opt == 4:
    #     image_temp[image_temp > 191] = 192
    #     image_temp[(image_temp > 127) & (image_temp < 192)] = 128
    #     image_temp[(image_temp > 63) & (image_temp < 128)] = 64
    #     image_temp[image_temp < 64] = 0
    # elif opt == 8:
    #     image_temp[image_temp > 223] = 255
    #     image_temp[(image_temp > 191) & (image_temp < 224)] = 192
    #     image_temp[(image_temp > 159) & (image_temp < 192)] = 160
    #     image_temp[(image_temp > 127) & (image_temp < 160)] = 128
    #     image_temp[(image_temp > 95) & (image_temp < 128)] = 96
    #     image_temp[(image_temp > 63) & (image_temp < 96)] = 64
    #     image_temp[(image_temp > 31) & (image_temp < 64)] = 32
    #     image_temp[image_temp < 32] = 0

    def canalCores(canal, imagem_valor):
        valor = (256 / canal)
        print(valor)
        print(f'color: {canal}')
        for i in range(canal):
            if i == 0:
                imag_valor[imagem_valor <= valor] = 0
            elif i == canal - 1:
                imagem_valor[imagem_valor >= (valor * i)] = 255
            else:
                imagem_valor[(imagem_valor > ((i * valor) - 1)) & (imagem_valor < ((i + 1) * valor))] = valor* i

    canalCores(option, image_temp)

    # st.image(image_aux)