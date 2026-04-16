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

st.sidebar.image("passport pic.jpeg", width=60)
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

st.markdown('<div class = "fade-in">created on 16-Apr-2026</div>', unsafe_allow_html=True)


col1, col2 = st.columns(2)

with col1:
    st.subheader("Welcome to my Website !")
    st.markdown("""
                <dev style="
                max-width: 600px;
                margin: auto;
                text-align: left;
                line-height: 1.5;
                ">
                This project presents a comprehensive analytical study of the structural transformation in global financial markets driven by the rapid advancement of artificial intelligence (AI). The analysis focuses on key market indices and leading equities, including Tesla Inc., Apple Inc., NIFTY 50, S&P 500, and BSE SENSEX, to evaluate market behavior before and after the AI acceleration phase (post-2020).

Using a structured framework based on CRISP-DM, KDD, and SEMMA methodologies, the study integrates financial time-series data with statistical modeling and machine learning techniques. Key financial indicators such as returns, volatility, trading volume, and technical signals were engineered to capture both performance and risk dynamics.

The analysis reveals notable shifts in market behavior in the post-AI era. Statistical testing, including ANOVA and hypothesis testing, indicates changes in volatility patterns and return distributions, suggesting increased market responsiveness and the influence of algorithmic and AI-driven trading systems. In particular, technology-driven equities such as Tesla and Apple exhibit heightened sensitivity to market sentiment and innovation cycles, while broader indices like the S&P 500 and NIFTY 50 reflect systemic changes in market efficiency and sectoral dominance.

The project further highlights an increase in short-term volatility and trading activity, pointing toward faster information assimilation and reduced latency in market reactions. However, this increased efficiency is accompanied by episodic instability, reinforcing the trade-off between speed and stability in AI-influenced markets.

An interactive dashboard built using Microsoft Power BI provides a comparative visualization of pre- and post-AI market regimes, enabling intuitive exploration of trends, risk metrics, and statistical insights.

In conclusion, the study demonstrates that AI has contributed to a measurable transformation in financial markets, impacting volatility structures, trading behavior, and sectoral performance. These findings align with modern financial theories such as the Efficient Market Hypothesis, while also highlighting emerging complexities introduced by high-frequency and AI-driven trading environments.

This project showcases the integration of data science, statistical analysis, and financial domain knowledge to generate actionable insights, reflecting real-world analytical practices used in quantitative finance and investment research.</dev>""",unsafe_allow_html=True)


page = st.sidebar.radio(
    "Navigation",
    ("Introduction", "Tanmay Chaki's Introduction", "Project", "Project Aspect")
)
if page == "Introduction":
   st.title("Introduction")


with col2:
    st.write("")

