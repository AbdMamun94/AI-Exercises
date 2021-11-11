import streamlit as st 

# working with media file and images 

from PIL import Image
img = Image.open("Documents/image_03.jpg")
st.image(img , use_column_width =  True)

# From URL 

st.image("https://assets.cdn.moviepilot.de/files/0fa78ec27e6b66178ce6056703f5fe3169dd8989289ac08773a3c54aa34e/fill/1200/576/Wolverine-Weg-des-Kriegers.jpg")
#copy image address 

#display video

video_file = open("Documents/secret_of_success.mp4","rb").read()
st.video(video_file)      # Chaile Start time add kore dewa jabe. =    ,Start_time=3

#display Audio 

audio_file= open("Documents/song.mp3","rb")
st.audio(audio_file.read())
#perticular kono format e chaileo possible =   ,format='audio/mp3'