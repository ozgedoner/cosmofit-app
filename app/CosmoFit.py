import streamlit as st
import importlib
import streamlit as st
from Calculation_Tools import app as tools_app
from Diet_Recommendation import app as diet_app
from About_CosmoFit import app as about_app


st.set_page_config(page_title="CosmoFit Diet Recommendation", page_icon="💪", layout="wide")

# Doğru isimle tanımla
PAGES = {
    "Calculation Tools": tools_app,
    "Diet Recommendations": diet_app,
    "About Us": about_app
}

selected_page = st.sidebar.selectbox("Menu", list(PAGES.keys()))
PAGES[selected_page]()


# Sidebar'dan seçim
selection = st.sidebar.radio("Select a module:", list(PAGES.keys()))

# Seçilen modül üzerinden app() fonksiyonunu çalıştır
module = PAGES[selection]
if hasattr(module, "app"):
    module.app()
else:
    st.error(f"`{selection}` modülünde `app()` fonksiyonu bulunamadı.")
