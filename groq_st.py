import streamlit as st
from upload_video import upload_video
import os
import sys
from oauth2client.file import Storage


# Title of the app
st.title("Video Upload and Playback App")

# File uploader widget
uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "avi", "mov", "mkv"])

    
if uploaded_file is not None:
    save_directory = "output"
    os.makedirs(save_directory, exist_ok=True)
    file_name = uploaded_file.name
    full_path = os.path.join(save_directory, file_name)
    with open(full_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"File saved to: {full_path}")

    if st.button('press Upload',key='upload'):
        full_path = os.path.abspath(os.path.join(save_directory, file_name))
        st.write(uploaded_file)
        video_data = {
                "file": fr"{full_path}",
                "title": "Interesting Football Story!",
                "description": "#shorts \n Sharing the best football story for 2025",
                "keywords":"meme,reddit,footballstory",
                "privacyStatus":"public"
            }
        st.write(video_data['file'])
        if not os.path.exists(full_path):
            print(f"File not found at {full_path}")
            st.write(f"File not found at {full_path}")
        else:
            st.write('I think no problem with it')
            print('working file has been found ',full_path)
            upload_video(video_data)
            
            # st.write(sys.argv[0])
            # st.write("%s-oauth2.json" % sys.argv[0])
            # storage = Storage('upload_video.py-oauth2.json')
            # st.write(storage.get())

