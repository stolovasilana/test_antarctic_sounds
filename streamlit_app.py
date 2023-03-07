import streamlit as st
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
from tempfile import NamedTemporaryFile
from streamlit_option_menu import option_menu

st.title('SERENA: Sensado, monitoreo y estudio de entorno sonoro para la evaluación del impacto \
         antropogenico en Antártida\n  _Emiliano Acevedo, Maria Noel Espinosa, Ilana Stolovas_')
with st.sidebar:
    selected = option_menu("Serena", ["Home", 'Subir','Escuchar'], 
        icons=['house', 'cloud-upload','soundwave'], menu_icon="cast", default_index=0)
if selected == "Home":
    st.write("Home")
elif selected == "Subir":
    st.write("Subir un archivo")
    audio = st.file_uploader("Upload an audio file", type=["wav"])
    if audio is not None:
        y, sr = librosa.load(audio.name, sr=None)
        st.write(audio.name)
        st.audio(y, format='audio/wav',sample_rate=sr)
        ## plot spectrogram
        fig, ax = plt.subplots(nrows=1, ncols=1, sharex=True)
        img = librosa.display.specshow(librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max), y_axis='log', x_axis='time',
                                    ax = ax)
        plt.colorbar(img, format='%+2.0f dB', ax = ax)
        plt.title(audio.name)
        ## show image in streamlit
        st.pyplot(fig)
elif selected == "Escuchar":
    st.write("Ejemplo: Escuchar un sonido y graficar su espectrograma. El audio corresponde a una grabación \
              de ruido de ambiente de la Antartida. El archivo se llama 'Only Background_soundscape_unimodal0.wav'")
    y, sr = librosa.load('Only Background_soundscape_unimodal0.wav', sr=None)
    st.audio(y, format='audio/wav',sample_rate=sr)
    ## plot spectrogram
    fig, ax = plt.subplots(nrows=1, ncols=1, sharex=True)
    img = librosa.display.specshow(librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max), y_axis='log', x_axis='time',
                                ax = ax)
    plt.colorbar(img, format='%+2.0f dB', ax = ax)
    plt.title('Power spectrogram')
    ## show image in streamlit
    st.pyplot(fig)

st.write("The end")


