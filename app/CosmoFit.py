import streamlit as st
import importlib
import About_CosmoFit
import Diet_Recommendation
import Calculation_Tools

st.set_page_config(page_title="CosmoFit Diet Recommendation", page_icon="💪", layout="wide")

# Doğru isimle tanımla
PAGES = {
    "💪 Personal Diet Recommendation": Diet_Recommendation,
    "📊 Calculation Tools": Calculation_Tools,
    "🌱 About CosmoFit": About_CosmoFit
}

# Sidebar'dan seçim
selection = st.sidebar.radio("Select a module:", list(PAGES.keys()))

# Seçilen modül üzerinden app() fonksiyonunu çalıştır
module = PAGES[selection]
if hasattr(module, "app"):
    module.app()
else:
    st.error(f"`{selection}` modülünde `app()` fonksiyonu bulunamadı.")
