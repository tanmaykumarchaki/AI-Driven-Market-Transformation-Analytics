import streamlit as st
#page configuration

st.set_page_config(
    page_title='AI-Driven-Market Transformation',
    layout="wide"
)

#Title
st.title("AI-Driven Market Transformation: A Comprehensive Analysis")

#Sidebar
st.sidebar.header("Navigation")
intro = st.sidebar.button("Introduction")
my_intro = st.sidebar.button("Tanmay Chaki's Introduction")
project_intro = st.sidebar.button("Project")
project_aspect = st.sidebar.button("Project Aspect")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Welcome to my Website !")
    st.write("Hi There !")

with col2:
    st.write("")
