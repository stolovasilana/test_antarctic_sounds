import streamlit as st
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt

st.write("Serena is the best")
### streamlit load audio file
audio_file = st.file_uploader("Upload Audio", type=['wav'])
if audio_file is not None:
    ## if user upload audio file, make a button to play audio
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/wav')
    ## load audio file
    y, sr = librosa.load(audio_file)
    ## plot spectrogram
    plt.figure(figsize=(14, 5))
    librosa.display.specshow(librosa.amplitude_to_db(librosa.stft(y), ref=np.max), y_axis='log', x_axis='time')
    plt.colorbar(format='%+2.0f dB')
    plt.title('Power spectrogram')
else:
    st.write("Please upload audio file")


