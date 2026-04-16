import streamlit as st
#page configuration

st.set_page_config(
    page_title='AI-Driven-Market Transformation',
    layout="wide",
    initial_sidebar_state="expanded" 
)

#Title
st.title("AI-Driven Market Transformation: A Comprehensive Analysis")

#Sidebar

st.sidebar.image("passport pic.jpeg", width=150)
st.sidebar.markdown("## Profile")
st.sidebar.markdown(
    """
    <div style = "text-align: left;">
        <h3>Tanmay Kumar Chaki</h3>
        <p>Age:22</p>
        <p>DOB:29-Dec-2003</p>
    </div>

""", unsafe_allow_html=True
)

st.sidebar.header("Navigation")
intro = st.sidebar.button("Introduction")
my_intro = st.sidebar.button("Tanmay Chaki's Introduction")
project_intro = st.sidebar.button("Project")
project_aspect = st.sidebar.button("Project Aspect")


# st.sidebar.write("**Name:** Tanmay Kumar Chaki")
# st.sidebar.write("**Age:** 22")
# st.sidebar.write("**Date of Birth:** 29 Dec 2003")



st.markdown(
    """
<style>
div.stbutton > button {
    width: 100%;
    height: 50px;
    border_radius: 10px;
}

</style>

"""
, unsafe_allow_html=True
)

st.markdown("""

<style>
         .fade-in {
            animation:fadIN 1s ease-in;
            }   
            
         @keyframes fadeIn {
            from {opacity: 0;} to {opacity: 1;}}

</style>

""", unsafe_allow_html=True)

st.markdown('<div class = "fade-in">Hello</div>', unsafe_allow_html=True)


col1, col2 = st.columns(2)

with col1:
    st.subheader("Welcome to my Website !")
    st.write("Hi There !")

with col2:
    st.write("")

