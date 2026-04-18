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

# 

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
                text-align: center;
                line-height: 1.5;
                ">
                This project presents a comprehensive analytical study of the structural transformation in global financial markets driven by the rapid advancement of artificial intelligence (AI). The analysis focuses on key market indices and leading equities, including Tesla Inc., Apple Inc., NIFTY 50, S&P 500, and BSE SENSEX, to evaluate market behavior before and after the AI acceleration phase (post-2020).

Using a structured framework based on CRISP-DM, KDD, and SEMMA methodologies, the study integrates financial time-series data with statistical modeling and machine learning techniques. Key financial indicators such as returns, volatility, trading volume, and technical signals were engineered to capture both performance and risk dynamics.

The analysis reveals notable shifts in market behavior in the post-AI era. Statistical testing, including ANOVA and hypothesis testing, indicates changes in volatility patterns and return distributions, suggesting increased market responsiveness and the influence of algorithmic and AI-driven trading systems. In particular, technology-driven equities such as Tesla and Apple exhibit heightened sensitivity to market sentiment and innovation cycles, while broader indices like the S&P 500 and NIFTY 50 reflect systemic changes in market efficiency and sectoral dominance.

The project further highlights an increase in short-term volatility and trading activity, pointing toward faster information assimilation and reduced latency in market reactions. However, this increased efficiency is accompanied by episodic instability, reinforcing the trade-off between speed and stability in AI-influenced markets.

An interactive dashboard built using Microsoft Power BI provides a comparative visualization of pre- and post-AI market regimes, enabling intuitive exploration of trends, risk metrics, and statistical insights.

In conclusion, the study demonstrates that AI has contributed to a measurable transformation in financial markets, impacting volatility structures, trading behavior, and sectoral performance. These findings align with modern financial theories such as the Efficient Market Hypothesis, while also highlighting emerging complexities introduced by high-frequency and AI-driven trading environments.

This project showcases the integration of data science, statistical analysis, and financial domain knowledge to generate actionable insights, reflecting real-world analytical practices used in quantitative finance and investment research.</dev>""",unsafe_allow_html=True)






with col2:
    page = st.sidebar.radio(
    "Navigation",
    ("Introduction", "Tanmay Chaki's Introduction", "Project", "Project Aspect")
)
    if page == "Introduction":
        st.title("Introduction")
        st.markdown("""
        <dev style ="
            max-width: 600px;
            margin: auto;
            text-align: center;
            line-height: 1.5;
                   ">


The global financial market has undergone a significant transformation with the rapid advancement of Artificial Intelligence (AI) and automation technologies. Traditionally, market behavior was primarily influenced by macroeconomic indicators, corporate performance, and investor sentiment. However, in the modern era, AI-driven systems have fundamentally altered how information is processed, decisions are made, and trades are executed. The rise of algorithmic trading, high-frequency systems, and predictive analytics has accelerated market efficiency while simultaneously introducing new layers of complexity and volatility.

In this evolving landscape, financial markets such as S&P 500, NIFTY 50, and BSE SENSEX, along with leading equities like Apple Inc. and Tesla Inc., provide a robust foundation for analyzing structural changes before and after the widespread adoption of AI. By examining historical price movements, volatility patterns, trading volumes, and technical indicators, it becomes possible to identify how AI has influenced market dynamics over time.

This project aims to leverage modern data science tools and methodologies to analyze these transformations. Using Python for statistical computing and feature engineering, and interactive dashboards built with Microsoft Power BI, the study explores key financial patterns such as returns, volatility clustering, and regime shifts. These tools enable not only efficient data processing but also intuitive visualization of complex relationships within the data.

To ensure a systematic and industry-aligned approach, the analysis is structured using the CRISP-DM (Cross Industry Standard Process for Data Mining) and KDD (Knowledge Discovery in Databases) methodologies. These frameworks guide the project from data collection and preprocessing to modeling, evaluation, and interpretation, ensuring that insights are both technically sound and contextually meaningful.

By comparing pre-AI and post-AI market regimes, this study seeks to uncover underlying patterns and statistically validate changes in market behavior. Furthermore, by applying hypothesis testing and advanced statistical techniques, the project attempts to project future market tendencies under the current AI-driven ecosystem. While financial markets remain inherently uncertain, the integration of AI, statistical modeling, and data-driven methodologies provides a powerful lens through which emerging trends and potential future scenarios can be analyzed.

Ultimately, this project reflects the growing convergence of finance, data science, and artificial intelligence, demonstrating how modern analytical tools can be used to interpret past behavior, understand present dynamics, and cautiously anticipate future market movements.

    </dev>
""", unsafe_allow_html= True)

    if page == "Tanmay Chaki's Introduction":
        st.title("About Me !")
        st.markdown("""

            <dev style ="
                max-width: 600px;
                margin: auto;
                text-align: center;
                line-height: 1.5;
    ">
            

I am a student with a strong interest in Data Science, Artificial Intelligence, and analytical problem-solving. My focus lies in understanding how data can be transformed into meaningful insights, particularly in domains such as financial markets and real-world decision systems.

I have developed practical skills in data visualization using tools like Microsoft Power BI and Python-based libraries, enabling me to represent complex datasets in a clear and interpretable manner. I am comfortable working with data pipelines, feature engineering, and exploratory analysis to uncover patterns and trends.

My growing interest in AI and statistical modeling drives me to explore how modern technologies are reshaping industries, especially finance. Through projects like this, I aim to strengthen my analytical thinking, apply structured methodologies such as CRISP-DM and KDD, and build solutions that combine technical knowledge with practical insights.

                </dev>



""", unsafe_allow_html=True)
        
    if page == "Project":
        st.title("Project Insight")
        st.markdown("""

        <dev style="
            max-width: 600px;
            margin: auto;
            text-align: center;
            line-height: 1.5;">
                    

This project is designed to analyze and interpret the structural transformation of financial markets in the era of Artificial Intelligence (AI). The primary aim is to investigate how AI-driven technologies have influenced market behavior, particularly in terms of returns, volatility, trading dynamics, and overall efficiency. By conducting a comparative study across key financial instruments such as Tesla Inc., Apple Inc., NIFTY 50, S&P 500, and BSE SENSEX, the project seeks to identify measurable differences between pre-AI and post-AI market regimes.

The clarity of this project lies in its structured and purpose-driven approach. Rather than focusing solely on price prediction, the analysis is centered on understanding *why* and *how* market behavior has evolved. The project employs well-defined phases based on CRISP-DM and KDD methodologies, ensuring a systematic progression from data collection and preprocessing to statistical analysis, modeling, and interpretation. This clarity allows for reproducibility, logical flow, and meaningful conclusions grounded in data rather than assumptions.

What makes this project exceptional is its integration of multiple analytical dimensions—financial theory, statistical validation, and modern data science tools. The use of Python enables robust data processing and feature engineering, while advanced statistical techniques such as ANOVA and hypothesis testing provide empirical validation of observed patterns. Additionally, the incorporation of interactive dashboards using Microsoft Power BI enhances interpretability by translating complex analytical outputs into intuitive visual insights. This combination mirrors real-world practices used in quantitative finance and investment research.

Furthermore, the project goes beyond conventional academic analysis by addressing a contemporary and highly relevant question: the impact of AI on market dynamics. In doing so, it captures not only historical patterns but also emerging trends shaped by algorithmic trading, automation, and rapid information processing. This positions the project at the intersection of finance and technology, making it both timely and practically valuable.

The project serves its purpose by delivering a comprehensive framework for analyzing market transformations and generating actionable insights. It demonstrates how data-driven methodologies can be applied to evaluate risk, detect structural changes, and support informed decision-making in uncertain environments. While acknowledging the inherent unpredictability of financial markets, the study provides a grounded perspective on how AI influences market efficiency and behavior.

In conclusion, this project stands out due to its clarity of objective, methodological rigor, and relevance to modern financial ecosystems. It not only showcases technical proficiency in data science and visualization but also reflects a deeper understanding of market mechanisms and the evolving role of AI in shaping them.

                    
</dev>
""", unsafe_allow_html=True)
    
    if page == 'Project Aspect':
        st.title("What does the Project Serve ?")
        st.markdown("""
            <dev style = "
                max-width: 600px;
                margin: auto;
                text-align: center;
                line-height: 1.5;"
                >
                    
            

1. Multi-Market Analysis
   The project analyzes diverse financial instruments including Tesla Inc., Apple Inc., NIFTY 50, S&P 500, and BSE SENSEX to ensure a global and comparative perspective.

2. Pre-AI vs Post-AI Comparison
   A structured segmentation of data into pre-2020 and post-2020 periods to evaluate the impact of AI-driven market transformation.

3. Data Engineering and Feature Creation
   Development of key financial indicators such as returns, volatility, and momentum to extract meaningful insights from raw OHLCV data.

4. Statistical Validation (ANOVA & Hypothesis Testing)
   Application of statistical techniques to validate whether observed changes in market behavior are significant and not due to randomness.

5. Volatility and Risk Analysis
   Examination of how AI has influenced market risk, including changes in volatility patterns and uncertainty levels.

6. Behavioral Pattern Detection
   Identification of patterns such as seasonality, trading volume impact, and regime shifts in market behavior.

7. Integration of Data Science Tools
   Use of Python for computation and analysis, combined with Microsoft Power BI for building interactive and insightful dashboards.

8. Methodological Framework Implementation
   Structured execution using CRISP-DM and KDD methodologies to ensure a systematic and industry-relevant analytical process.

9. Insight Generation and Interpretation
   Transformation of statistical outputs into meaningful business and financial insights that explain *why* changes occur in the market.

10. Final Outcome - Analytical Dashboard & Report
    The project delivers an interactive dashboard and a detailed analytical report that clearly demonstrates how AI has transformed financial markets and provides a data-driven perspective on future trends.

                    
                    
                    
                    </dev>

""", unsafe_allow_html=True)

st.title("Analyzed Datasets and Visualisation")

button1 , button2 , button3, button4, button5 , button6 = st.columns(6)

with button1:
    if st.button("TESLA"):
        st.session_state.active_section = 'TESLA'

        if st.session_state.active_section == "TESLA":
            st.subheader("High-Low-Open-Close")
            with open("tesla.txt", "r", encoding="utf-8") as file:
              tesla = file.read()
            st.markdown("""
<div style="
    width: 100%;
    margin: auto;
    text-align: center;
    line-height: 1.7;
    font-size: 18px;
">
{tesla}
</div>
""", unsafe_allow_html=True)


    
with button2:
    if st.button("APPLE"):
        st.session_state.active_section = 'APPLE'

with button3:
    if st.button("NIFTY 50"):
        st.session_state.active_section = 'NIFTY 50'

with button4:
    if st.button("SENSEX"):
        st.session_state.active_section = 'SENSEX'

with button5:
    if st.button("S&P 500"):
        st.session_state.active_section =  'S&P 500'

with button6:
    if st.button("DashBoard"):
       st.session_state.active_section = 'DashBoard'
