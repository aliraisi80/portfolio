import pandas
import streamlit as st

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("Ali Raisi")
    content="""
        Hi,I am ali! I am a python programmer,
        teacher and CEO of Farvigrom Social media,
        I graduated in 2022 from software engineer,..
        """
    st.info(content)

Content2="""
Below you can find some of apps I built in python.
feel free to contact me!
"""
st.write(Content2)
col3,col4=st.columns(2)
df=pandas.read_csv("data.csv",sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write(f"[Source Code]({row['url']})")
with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write(f"[Source Code]({row['url']})")