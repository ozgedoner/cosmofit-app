import streamlit as st

st.title("🛠️ CosmoFit Calculation Tools")

# Tabs
tabs = st.tabs([
    "Calorie Calculator",
    "Ideal Weight",
    "Daily Protein Requirement",
    "Risk (Waist Circumference)",
    "Body Mass Index (BMI)",
    "Waist-Hip Ratio"
])

# 1. Calorie Calculator
with tabs[0]:
    st.subheader("🔥 Calorie Calculator (Simple)")
    weight = st.number_input("Your Weight (kg):", 30, 200)
    multiplier = st.select_slider("Your Activity Level", options=[1.2, 1.375, 1.55, 1.725, 1.9],
                                  format_func=lambda x: {
                                      1.2: "Sedentary",
                                      1.375: "Lightly Active",
                                      1.55: "Moderately Active",
                                      1.725: "Very Active",
                                      1.9: "Super Active"
                                  }[x])
    if st.button("Calculate", key="calorie"):
        st.success(f"Your estimated daily calorie need: {round(weight * 24 * multiplier)} kcal")

# 2. Ideal Weight
with tabs[1]:
    st.subheader("🎯 Ideal Weight Calculator")
    gender = st.radio("Your Gender:", ["Female", "Male"], key="ideal_gender")
    height_cm = st.number_input("Height (cm):", 140, 220, key="ideal_height")
    if st.button("Calculate", key="ideal"):
        height_in = height_cm / 2.54
        ideal = 45.5 + 2.3 * (height_in - 60) if gender == "Female" else 50 + 2.3 * (height_in - 60)
        st.success(f"Your ideal weight: {ideal:.1f} kg")

# 3. Protein
with tabs[2]:
    st.subheader("🍗 Daily Protein Requirement")
    weight = st.number_input("Your Weight (kg):", 30, 200, key="protein_weight")
    level = st.selectbox("Activity Level", ["Low", "Medium", "High"])
    ratio = {"Low": 0.8, "Medium": 1.0, "High": 1.2}[level]
    if st.button("Calculate", key="protein"):
        need = weight * ratio
        st.success(f"Your daily protein requirement: {need:.1f} grams")

# 4. Risk (Waist Circumference)
with tabs[3]:
    st.subheader("⚠️ Risk Based on Waist Circumference")
    gender = st.radio("Your Gender:", ["Female", "Male"], key="risk_gender")
    waist = st.number_input("Waist Circumference (cm):", 50, 150, key="risk_waist")
    risk = ""
    if st.button("Calculate", key="risk"):
        if gender == "Female":
            if waist <= 80:
                risk = "Low risk"
            elif waist <= 88:
                risk = "Moderate risk"
            else:
                risk = "High risk"
        else:
            if waist <= 94:
                risk = "Low risk"
            elif waist <= 102:
                risk = "Moderate risk"
            else:
                risk = "High risk"
        st.success(f"Result: {risk}")

# 5. BMI
with tabs[4]:
    st.subheader("📏 Body Mass Index (BMI)")
    weight = st.number_input("Weight (kg):", 30, 200, key="bmi_weight")
    height = st.number_input("Height (cm):", 140, 220, key="bmi_height")
    if st.button("Calculate", key="bmi"):
        h_m = height / 100
        bmi = weight / (h_m ** 2)
        st.success(f"BMI: {bmi:.2f}")

# 6. Waist-Hip Ratio
with tabs[5]:
    st.subheader("📐 Waist-Hip Ratio")
    gender = st.radio("Your Gender:", ["Female", "Male"], key="whr_gender")
    waist = st.number_input("Waist (cm):", 50, 150, key="whr_waist")
    hip = st.number_input("Hip (cm):", 50, 150, key="whr_hip")
    if st.button("Calculate", key="whr"):
        ratio = waist / hip
        if gender == "Female":
            if ratio <= 0.80:
                result = "Low risk"
            elif ratio <= 0.84:
                result = "Moderate risk"
            else:
                result = "High risk"
        else:
            if ratio <= 0.95:
                result = "Low risk"
            elif ratio <= 1.0:
                result = "Moderate risk"
            else:
                result = "High risk"
        st.success(f"Ratio: {ratio:.2f} - {result}")
