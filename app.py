import streamlit as st

st.title("Download button, without rerun")

x = st.slider("VALUE:", 0, 100, 42)

download_button_clicked = st.download_button("Click to download", data=str(x))
st.write(download_button_clicked)
