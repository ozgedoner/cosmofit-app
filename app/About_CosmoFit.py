import streamlit as st

def app():

    st.markdown("<h1 style='text-align:center; color:#2E8B57;'> About Us </h1>", unsafe_allow_html=True)
    st.markdown("---")

    st.image("ekip.png", caption="CosmoFit Founding Team", use_container_width=True)
    st.markdown("---")

    st.markdown("""
    ### Who Are We?

    **CosmoFit** is a technology company founded in 2025 that uses artificial intelligence and machine learning technologies to provide individuals with personalized healthy recipes.

    Our goal is to prevent **unhealthy and insufficient nutrition**, which threatens both physical and psychological health, through scientifically based recipe recommendation systems. According to WHO data:

    - 39% of adults are overweight,
    - Childhood obesity rates are increasing,
    - Unhealthy diets lead to diseases such as heart disease, diabetes, and depression.

    **CosmoFit** aims not only to help individuals lose weight but also to protect and restore their health. With our AI-powered systems, we analyze recipes based on nutritional content and recommend meals tailored to personal goals.

    Our Founders:

    - [Ezgi Bahadır](https://www.linkedin.com/in/ezgi-bahad%C4%B1r-49a9601b9/)
    - [Gamze Kızılkaya](https://www.linkedin.com/in/gamze-k%C4%B1z%C4%B1lkaya-02481616b/)
    - [Özge Rabia Döner](https://www.linkedin.com/in/ozgerabiadoner/)
    """)

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("🌟 Our Mission")
        st.markdown("""
        - To promote healthy living awareness through AI-supported technologies
        - To provide individuals with personalized health-oriented recipes
        - To support both the physical and mental well-being of society
        """)

    with col2:
        st.subheader("🌎 Our Vision")
        st.markdown("""
        - To become a leader in AI-powered nutrition technologies
        - To achieve global reach with healthy eating algorithms
        - To play an active role in fighting diabetes, obesity, and eating disorders in the future
        """)

    with col3:
        st.subheader("💖 Our Values")
        st.markdown("""
        - Scientific foundation and technology-oriented approach
        - Ethical development and data security
        - Inclusivity and accessibility
        - A digital health perspective that values people
        """)

    st.markdown("---")
    st.info("Would you like to walk this journey with us? Contact us to learn more.")
