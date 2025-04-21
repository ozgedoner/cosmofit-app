import streamlit as st

def app():
    import streamlit as st
    from PIL import Image
    import matplotlib.pyplot as plt
    import datetime


    import pandas as pd
    from Generate_Recommendations import Generator
    from random import uniform as rnd
    from ImageFinder.ImageFinder import get_images_links as find_image
    from streamlit_echarts import st_echarts
    import openai
    import os
    from dotenv import load_dotenv
    import base64


    import streamlit as st
    from PIL import Image, ImageDraw

    import folium
    from streamlit_folium import st_folium



    if "country" not in st.session_state:
        st.session_state.country = None

    if "risk_score" not in st.session_state:
        st.session_state.risk_score = None

    if "recommendations" not in st.session_state:
        st.session_state.recommendations = None

    if "generated" not in st.session_state:
        st.session_state.generated = False

    import pandas as pd

    # Reload after reset
    file_path = "/Users/ozgedoner/Desktop/CosmoFit/csv/extended_merged_obesity_coordinates.csv"
    obesity_df = pd.read_csv(file_path)



    # 🌗 Tema geçişi
    if "dark_mode" not in st.session_state:
        st.session_state.dark_mode = False

    if st.button("🌙 Dark Mode" if not st.session_state.dark_mode else "☀️ Light Mode"):
        st.session_state.dark_mode = not st.session_state.dark_mode

    # Tema CSS + Hover Efektler + Renk Güncellemeleri
    if st.session_state.dark_mode:
        st.markdown("""
            <style>
                body, .stApp {
                    background-color: #121212;
                    color: #ffffff;
                }
                h1, h2, h3, h4, h5, h6, .stText, .stMarkdown, .stTitle, .stDataFrame, .stTabs, label, .css-1v0mbdj, .css-1d391kg {
                    color: white !important;
                }
                .stTextInput>div>div>input,
                .stTextArea>div>textarea,
                .stSelectbox>div>div>div>input,
                .stNumberInput>div>input,
                .stButton>button,
                .stSelectbox>div>div {
                    background-color: #1e1e1e !important;
                    color: white !important;
                }
                .stButton>button:hover {
                    border: 1px solid #ffffff;
                    background-color: #333333;
                    transition: 0.3s;
                }
                .stTabs [data-baseweb="tab"] {
                    background-color: #000000;
                    border: 1px solid #333333;
                    color: white;
                }
                .stTabs [aria-selected="true"] {
                    border-bottom: 2px solid #ffffff;
                }
                .stDataFrame, .dataframe, .stMarkdown p, .stMarkdown span, .stMarkdown div {
                    color: white !important;
                }
                .echarts-legend {
                    color: white !important;
                }
                .st-echarts text {
                    fill: white !important;
                }
                .st-expander, .st-expander p, .st-expander div {
                    color: white !important;
                }
            </style>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <style>
                body, .stApp {
                    background-color: #ffffff;
                    color: #000000;
                }
                h1, h2, h3, h4, h5, h6, .stText, .stMarkdown, .stTitle, .stDataFrame, .stTabs, label, .css-1v0mbdj, .css-1d391kg {
                    color: black !important;
                }
                .stTextInput>div>div>input,
                .stTextArea>div>textarea,
                .stSelectbox>div>div>div>input,
                .stSelectbox>div>div,
                .stNumberInput>div>input,
                .stButton>button {
                    background-color: white !important;
                    color: black !important;
                }
                .stButton>button:hover {
                    border: 1px solid #000000;
                    background-color: #f0f0f0;
                    transition: 0.3s;
                }
                .stTabs [data-baseweb="tab"] {
                    background-color: #ffffff;
                    border: 1px solid #cccccc;
                    color: black;
                }
                .stTabs [aria-selected="true"] {
                    border-bottom: 2px solid #000000;
                }
                .stDataFrame, .dataframe, .stMarkdown p, .stMarkdown span, .stMarkdown div {
                    color: black !important;
                }
                .st-expander, .st-expander p, .st-expander div {
                    color: black !important;
                }
            </style>
        """, unsafe_allow_html=True)

    import streamlit as st
    import base64

    # Tabağın dönmesi için CSS ve yazılar
    banner_css = """
    <style>
    @keyframes spin {
      0% { transform: rotate(0deg);}
      100% { transform: rotate(360deg);}
    }
    .banner-container {
      position: relative;
      text-align: center;
      margin-bottom: 40px;
    }
    .banner-container img.bg {
      width: 100%;
      max-height: 220px;
      object-fit: cover;
      opacity: 1;
      display: block;
      margin: 0 auto;
    }
    .rotating-img {
      animation: spin 12s linear infinite;
      width: 180px;
      height: 180px;
      border-radius: 50%;
      display: block;
      object-fit: cover;
      filter: drop-shadow(0 0 10px rgba(0,0,0,0.4));
      background-color: white;
      position: absolute;
      top: 5%;
      left: 40.5%;
      transform: translate(-50%, -50%);
      z-index: 2;
    }
    </style>
    """


    # Path to the folder containing the images
    image_path = "Images"  # Example: if images are stored under an "assets" folder in your project

    # Encode plate image
    tabak_file_path = os.path.join(image_path, "/Users/ozgedoner/Desktop/CosmoFit/Images/tabak.png")
    with open(tabak_file_path, "rb") as tabak_file:
        encoded_tabak = base64.b64encode(tabak_file.read()).decode()

    # Encode banner image
    banner_encoded = None
    banner_file_path = os.path.join(image_path, "/Users/ozgedoner/Desktop/CosmoFit/Images/banner.jpg")
    try:
        with open(banner_file_path, "rb") as banner_file:
            banner_encoded = base64.b64encode(banner_file.read()).decode()
    except FileNotFoundError:
        st.warning("📸 Banner image (banner.jpg) not found in the specified folder. Continuing...")

    # HTML Göster
    if banner_encoded:

        html = f"""
        <div class="banner-container">
          <img src="data:image/jpeg;base64,{banner_encoded}" class="bg">
          <img src="data:image/png;base64,{encoded_tabak}" class="rotating-img">
        </div>
        """
        st.markdown(banner_css, unsafe_allow_html=True)
        st.markdown(html, unsafe_allow_html=True)
    else:
        st.warning("Banner bulunamadı. Tabağın gösterimi atlandı.")

    import streamlit as st
    import pandas as pd
    from streamlit_echarts import st_echarts




    #st.markdown("<h1 style='text-align: center; color: #00BFFF;'> Automatic Diet Recommendation</h1>", unsafe_allow_html=True)
    #st.markdown("#### Lütfen bilgilerini girerek sana özel bir diyet planı oluşturalım.")

    #with st.form("diet_form", clear_on_submit=False):
        #st.markdown("###  Kişisel Bilgiler")
        #age = st.number_input(" Age", min_value=2, max_value=100, value=25)
    # height = st.number_input("Height (cm)", min_value=50, max_value=250, value=170)
    # weight = st.number_input("️Weight (kg)", min_value=10, max_value=250, value=70)

    # st.markdown("###  Cinsiyet")
    # gender = st.radio("Select Gender", ["Male", "Female"], horizontal=True)

    # st.markdown("Aktivite Seviyesi")
        #activity = st.select_slider(
            #"Choose your activity level",
    #    options=[
    #  "🛋️ Little/no exercise",
    #   "🚶 Lightly active",
    #    "🏋️ Moderately active",
    #    "🚴 Very active",
    #  "💼 Extra active"
    #     ],
    #    value="🚶 Lightly active"
    #  )

    #  st.markdown("###  Kilo Planı")
    #  plan = st.selectbox("Choose your weight goal", ["Lose weight", "Maintain weight", "Gain weight"])

       # st.markdown("### Günlük Öğün Sayısı")
    # meals = st.slider("Meals per day", 1, 6, 3)

    # submitted = st.form_submit_button("🚀 Generate", use_container_width=True)

    #if submitted:
    # st.success("✅ Öneriler hazır! AI tarafından hesaplanıyor...")
        # AI hesaplamaları burada yapılabilir




    nutritions_values = ['Calories', 'FatContent', 'SaturatedFatContent', 'CholesterolContent', 'SodiumContent',
                         'CarbohydrateContent', 'FiberContent', 'SugarContent', 'ProteinContent']
    # Streamlit states initialization
    if 'person' not in st.session_state:
        st.session_state.generated = False
        st.session_state.recommendations = None
        st.session_state.person = None
        st.session_state.weight_loss_option = None


    class Person:

        def __init__(self, age, height, weight, gender, activity, meals_calories_perc, weight_loss):
            self.age = age
            self.height = height
            self.weight = weight
            self.gender = gender
            self.activity = activity
            self.meals_calories_perc = meals_calories_perc
            self.weight_loss = weight_loss

        def calculate_bmi(self, ):
            bmi = round(self.weight / ((self.height / 100) ** 2), 2)
            return bmi

        def display_result(self):
            bmi = self.calculate_bmi()
            bmi_string = f'{bmi} kg/m²'

            # Görseldeki sınıflandırmaya göre renk ve kategori
            if bmi < 18.5:
                category = 'Underweight (<18.5)'
                color = '#00BCD4'  # turkuaz
            elif 18.5 <= bmi < 25.0:
                category = 'Normal weight (18.5–24.9)'
                color = '#4CAF50'  # yeşil
            elif 25.0 <= bmi < 30.0:
                category = 'Overweight (25.0–29.9)'
                color = '#FFEB3B'  # sarı
            elif 30.0 <= bmi < 35.0:
                category = 'Obesity I (30.0–34.9)'
                color = '#FF9800'  # turuncu
            elif 35.0 <= bmi < 40.0:
                category = 'Obesity II (35.0–39.9)'
                color = '#FF5722'  # koyu turuncu
            else:
                category = 'Obesity III (>=40.0)'
                color = '#D32F2F'  # kırmızı

            return bmi_string, category, color

        def calculate_bmr(self):
            if self.gender == 'Male':
                bmr = 10 * self.weight + 6.25 * self.height - 5 * self.age + 5
            else:
                bmr = 10 * self.weight + 6.25 * self.height - 5 * self.age - 161
            return bmr

        def calories_calculator(self):
            activites=['Little/no exercise', 'Light exercise', 'Moderate exercise (3-5 days/wk)', 'Very active (6-7 days/wk)', 'Extra active (very active & physical job)']
            weights=[1.2,1.375,1.55,1.725,1.9]
            weight = weights[activites.index(self.activity)]
            maintain_calories = self.calculate_bmr()*weight
            return maintain_calories


        def generate_recommendations(self, ):
            total_calories = self.weight_loss * self.calories_calculator()
            recommendations = []
            for meal in self.meals_calories_perc:
                meal_calories = self.meals_calories_perc[meal] * total_calories
                if meal == 'breakfast':
                    recommended_nutrition = [meal_calories, rnd(10, 30), rnd(0, 4), rnd(0, 30), rnd(0, 400), rnd(40, 75),
                                             rnd(4, 10), rnd(0, 10), rnd(30, 100)]
                elif meal == 'launch':
                    recommended_nutrition = [meal_calories, rnd(20, 40), rnd(0, 4), rnd(0, 30), rnd(0, 400), rnd(40, 75),
                                             rnd(4, 20), rnd(0, 10), rnd(50, 175)]
                elif meal == 'dinner':
                    recommended_nutrition = [meal_calories, rnd(20, 40), rnd(0, 4), rnd(0, 30), rnd(0, 400), rnd(40, 75),
                                             rnd(4, 20), rnd(0, 10), rnd(50, 175)]
                else:
                    recommended_nutrition = [meal_calories, rnd(10, 30), rnd(0, 4), rnd(0, 30), rnd(0, 400), rnd(40, 75),
                                             rnd(4, 10), rnd(0, 10), rnd(30, 100)]
                generator = Generator(recommended_nutrition)
                recommended_recipes = generator.generate().json()['output']
                recommendations.append(recommended_recipes)
            for recommendation in recommendations:
                for recipe in recommendation:
                    recipe['image_link'] = find_image(recipe['Name'])
            return recommendations


    class Display:
        def __init__(self):
            self.plans = ["Maintain weight", "Mild weight loss", "Weight loss", "Extreme weight loss"]
            self.weights = [1, 0.9, 0.8, 0.6]
            self.losses = ['-0 kg/week', '-0.25 kg/week', '-0.5 kg/week', '-1 kg/week']
            pass

        def display_bmi(self, person):
            from PIL import Image, ImageDraw
            import uuid
            import os

            st.header("BMI CALCULATOR")

            # Calculate BMI and determine classification
            bmi = person.calculate_bmi()
            bmi_string = f"{bmi} kg/m²"

            if bmi < 18.5:
                category = "Underweight (<18.5)"
                color = "#00BCD4"
            elif 18.5 <= bmi < 25.0:
                category = "Normal weight (18.5–24.9)"
                color = "#4CAF50"
            elif 25.0 <= bmi < 30.0:
                category = "Overweight (25.0–29.9)"
                color = "#FFEB3B"
            elif 30.0 <= bmi < 35.0:
                category = "Obesity I (30.0–34.9)"
                color = "#FF9800"
            elif 35.0 <= bmi < 40.0:
                category = "Obesity II (35.0–39.9)"
                color = "#FF5722"
            else:
                category = "Obesity III (>=40.0)"
                color = "#D32F2F"

            # Display BMI info
            st.metric(label="Your Body Mass Index", value=bmi_string)
            st.markdown(f"<p style='color:{color}; font-size:24px;'><strong>{category}</strong></p>",
                        unsafe_allow_html=True)
            st.markdown("✅ Healthy BMI range: <strong>18.5 kg/m² – 24.9 kg/m²</strong>", unsafe_allow_html=True)

            # Ranges and corresponding visual percentages on the image
            bmi_breakpoints = [0, 18.5, 24.9, 29.9, 34.9, 39.9, 60]
            zone_percentages = [0.04, 0.18, 0.33, 0.48, 0.63, 0.78, 0.93]  # proportional X locations

            def get_arrow_x(bmi, img_width):
                for i in range(1, len(bmi_breakpoints)):
                    if bmi <= bmi_breakpoints[i]:
                        bmi_min = bmi_breakpoints[i - 1]
                        bmi_max = bmi_breakpoints[i]
                        ratio = (bmi - bmi_min) / (bmi_max - bmi_min)
                        px_start = zone_percentages[i - 1] * img_width
                        px_end = zone_percentages[i] * img_width
                        return int(px_start + ratio * (px_end - px_start))
                return int(zone_percentages[-1] * img_width)

            # Load the image and draw the red arrow
            img_path = "/Users/ozgedoner/Desktop/CosmoFit/Images/bmi_chart.png"  # Make sure this file is present in your app folder
            image = Image.open(img_path).convert("RGBA")
            img_width, img_height = image.size
            arrow_x = get_arrow_x(bmi, img_width)

            draw = ImageDraw.Draw(image)
            draw.polygon([(arrow_x, 30), (arrow_x - 12, 10), (arrow_x + 12, 10)], fill="red")

            # Save to a temporary file to prevent overlapping arrows
            temp_path = f"/tmp/bmi_arrow_{uuid.uuid4().hex[:6]}.png"
            image.save(temp_path)

            # Display updated image
            st.image(temp_path, caption="BMI Classification Chart", use_container_width=True)
            st.success(f"📌 You fall into the category: **{category}**")

        def display_calories(self, person):
            st.header('CALORIES CALCULATOR')
            maintain_calories = person.calories_calculator()
            st.write(
                'The results show a number of daily calorie estimates that can be used as a guideline for how many calories to consume each day to maintain, lose, or gain weight at a chosen rate.')
            for plan, weight, loss, col in zip(self.plans, self.weights, self.losses, st.columns(4)):
                with col:
                    st.metric(label=plan, value=f'{round(maintain_calories * weight)} Calories/day', delta=loss,
                              delta_color="inverse")

        def display_recommendation(self, person, recommendations):
            st.header('DIET RECOMMENDATOR')
            with st.spinner('Generating recommendations...'):
                meals = person.meals_calories_perc
                st.subheader('Recommended recipes:')
                for meal_name, column, recommendation in zip(meals, st.columns(len(meals)), recommendations):
                    with column:
                        # st.markdown(f'<div style="text-align: center;">{meal_name.upper()}</div>', unsafe_allow_html=True)
                        st.markdown(f'##### {meal_name.upper()}')
                        for recipe in recommendation:

                            recipe_name = recipe['Name']
                            expander = st.expander(recipe_name)
                            recipe_link = recipe['image_link']
                            recipe_img = f'<div><center><img src={recipe_link} alt={recipe_name}></center></div>'
                            nutritions_df = pd.DataFrame({value: [recipe[value]] for value in nutritions_values})

                            expander.markdown(recipe_img, unsafe_allow_html=True)
                            expander.markdown(
                                f'<h5 style="text-align: center;font-family:sans-serif;">Nutritional Values (g):</h5>',
                                unsafe_allow_html=True)
                            expander.dataframe(nutritions_df)
                            expander.markdown(f'<h5 style="text-align: center;font-family:sans-serif;">Ingredients:</h5>',
                                              unsafe_allow_html=True)
                            for ingredient in recipe['RecipeIngredientParts']:
                                expander.markdown(f"""
                                            - {ingredient}
                                """)
                            expander.markdown(
                                f'<h5 style="text-align: center;font-family:sans-serif;">Recipe Instructions:</h5>',
                                unsafe_allow_html=True)
                            for instruction in recipe['RecipeInstructions']:
                                expander.markdown(f"""
                                            - {instruction}
                                """)
                            expander.markdown(
                                f'<h5 style="text-align: center;font-family:sans-serif;">Cooking and Preparation Time:</h5>',
                                unsafe_allow_html=True)
                            expander.markdown(f"""
                                    - Cook Time       : {recipe['CookTime']}min
                                    - Preparation Time: {recipe['PrepTime']}min
                                    - Total Time      : {recipe['TotalTime']}min
                                """)


        def display_meal_choices(self, person, recommendations):
            st.subheader('Choose your meal composition:')
            # Display meal compositions choices
            if len(recommendations) == 3:
                breakfast_column, launch_column, dinner_column = st.columns(3)
                with breakfast_column:
                    breakfast_choice = st.selectbox(f'Choose your breakfast:',
                                                    [recipe['Name'] for recipe in recommendations[0]])
                with launch_column:
                    launch_choice = st.selectbox(f'Choose your launch:', [recipe['Name'] for recipe in recommendations[1]])
                with dinner_column:
                    dinner_choice = st.selectbox(f'Choose your dinner:', [recipe['Name'] for recipe in recommendations[2]])
                choices = [breakfast_choice, launch_choice, dinner_choice]
            elif len(recommendations) == 4:
                breakfast_column, morning_snack, launch_column, dinner_column = st.columns(4)
                with breakfast_column:
                    breakfast_choice = st.selectbox(f'Choose your breakfast:',
                                                    [recipe['Name'] for recipe in recommendations[0]])
                with morning_snack:
                    morning_snack = st.selectbox(f'Choose your morning_snack:',
                                                 [recipe['Name'] for recipe in recommendations[1]])
                with launch_column:
                    launch_choice = st.selectbox(f'Choose your launch:', [recipe['Name'] for recipe in recommendations[2]])
                with dinner_column:
                    dinner_choice = st.selectbox(f'Choose your dinner:', [recipe['Name'] for recipe in recommendations[3]])
                choices = [breakfast_choice, morning_snack, launch_choice, dinner_choice]
            else:
                breakfast_column, morning_snack, launch_column, afternoon_snack, dinner_column = st.columns(5)
                with breakfast_column:
                    breakfast_choice = st.selectbox(f'Choose your breakfast:',
                                                    [recipe['Name'] for recipe in recommendations[0]])
                with morning_snack:
                    morning_snack = st.selectbox(f'Choose your morning_snack:',
                                                 [recipe['Name'] for recipe in recommendations[1]])
                with launch_column:
                    launch_choice = st.selectbox(f'Choose your launch:', [recipe['Name'] for recipe in recommendations[2]])
                with afternoon_snack:
                    afternoon_snack = st.selectbox(f'Choose your afternoon:',
                                                   [recipe['Name'] for recipe in recommendations[3]])
                with dinner_column:
                    dinner_choice = st.selectbox(f'Choose your  dinner:', [recipe['Name'] for recipe in recommendations[4]])
                choices = [breakfast_choice, morning_snack, launch_choice, afternoon_snack, dinner_choice]

                # Calculating the sum of nutritional values of the choosen recipes
            total_nutrition_values = {nutrition_value: 0 for nutrition_value in nutritions_values}
            for choice, meals_ in zip(choices, recommendations):
                for meal in meals_:
                    if meal['Name'] == choice:
                        for nutrition_value in nutritions_values:
                            total_nutrition_values[nutrition_value] += meal[nutrition_value]

            total_calories_chose = total_nutrition_values['Calories']
            loss_calories_chose = round(person.calories_calculator() * person.weight_loss)

            # Display corresponding graphs
            st.markdown(
                f'<h5 style="text-align: center;font-family:sans-serif;">Total Calories in Recipes vs {st.session_state.weight_loss_option} Calories:</h5>',
                unsafe_allow_html=True)
            total_calories_graph_options = {
                "xAxis": {
                    "type": "category",
                    "data": ['Total Calories you chose', f"{st.session_state.weight_loss_option} Calories"],
                },
                "yAxis": {"type": "value"},
                "series": [
                    {
                        "data": [
                            {"value": total_calories_chose,
                             "itemStyle": {"color": ["#33FF8D", "#FF3333"][total_calories_chose > loss_calories_chose]}},
                            {"value": loss_calories_chose, "itemStyle": {"color": "#3339FF"}},
                        ],
                        "type": "bar",
                    }
                ],
            }
            st_echarts(options=total_calories_graph_options, height="400px", )
            st.markdown(f'<h5 style="text-align: center;font-family:sans-serif;">Nutritional Values:</h5>',
                        unsafe_allow_html=True)
            nutritions_graph_options = {
                "tooltip": {"trigger": "item"},
                "legend": {"top": "5%", "left": "center"},
                "series": [
                    {
                        "name": "Nutritional Values",
                        "type": "pie",
                        "radius": ["40%", "70%"],
                        "avoidLabelOverlap": False,
                        "itemStyle": {
                            "borderRadius": 10,
                            "borderColor": "#fff",
                            "borderWidth": 2,
                        },
                        "label": {"show": False, "position": "center"},
                        "emphasis": {
                            "label": {"show": True, "fontSize": "40", "fontWeight": "bold"}
                        },
                        "labelLine": {"show": False},
                        "data": [
                            {"value": round(total_nutrition_values[total_nutrition_value]), "name": total_nutrition_value}
                            for total_nutrition_value in total_nutrition_values],
                    }
                ],
            }
            st_echarts(options=nutritions_graph_options, height="500px", )


    display = Display()
    title = "<h1 style='text-align: center;'>Automatic Diet Recommendation</h1>"
    st.markdown(title, unsafe_allow_html=True)

    with st.form("recommendation_form"):
        st.write("Modify the values and click the Generate button to use")

        @st.cache_data
        def load_data():
            return pd.read_csv("/Users/ozgedoner/Desktop/CosmoFit/csv/extended_merged_obesity_coordinates.csv")

        obesity_df = load_data()
        country_options = sorted(obesity_df["Country"].unique().tolist())

        # 🌍 Country seçimi
        country = st.selectbox("🌍 What country do you live in?", country_options)

        age = st.number_input('Age', min_value=2, max_value=120, step=1)
        height = st.number_input('Height(cm)', min_value=50, max_value=300, step=1)
        weight = st.number_input('Weight(kg)', min_value=10, max_value=300, step=1)
        gender = st.radio('Gender', ('Male', 'Female'))

        activity = st.select_slider(
            'Activity',
            options=[
                'Little/no exercise',
                'Light exercise',
                'Moderate exercise (3-5 days/wk)',
                'Very active (6-7 days/wk)',
                'Extra active (very active & physical job)'
            ]
        )

        option = st.selectbox('Choose your weight loss plan:', display.plans)
        st.session_state.weight_loss_option = option
        weight_loss = display.weights[display.plans.index(option)]

        number_of_meals = st.slider('Meals per day', min_value=3, max_value=5, step=1, value=3)
        if number_of_meals == 3:
            meals_calories_perc = {'breakfast': 0.35, 'lunch': 0.40, 'dinner': 0.25}
        elif number_of_meals == 4:
            meals_calories_perc = {'breakfast': 0.30, 'morning snack': 0.05, 'lunch': 0.40, 'dinner': 0.25}
        else:
            meals_calories_perc = {'breakfast': 0.30, 'morning snack': 0.05, 'lunch': 0.40, 'afternoon snack': 0.05, 'dinner': 0.20}

        generated = st.form_submit_button("Generate")

    # ✅ Form gönderildiyse tüm değerleri kaydet
    if generated:
        st.session_state.generated = True
        st.session_state.country = country  # 🔥 Ülke verisini session'a kaydediyoruz
        person = Person(age, height, weight, gender, activity, meals_calories_perc, weight_loss)
        st.session_state.person = person

        with st.container():
            display.display_bmi(person)
        with st.container():
            display.display_calories(person)

        with st.spinner('Generating recommendations...'):
            recommendations = person.generate_recommendations()
            st.session_state.recommendations = recommendations



    if st.session_state.generated:
        person = st.session_state.person
        recommendations = st.session_state.recommendations

        with st.container():
            display.display_bmi(person)
        with st.container():
            display.display_calories(person)

        if recommendations is not None:
            with st.container():
                display.display_recommendation(person, recommendations)
                st.success('Recommendation Generated Successfully !', icon="✅")

            with st.container():
                display.display_meal_choices(person, recommendations)
        else:
            st.error("🚨 No recommendations found. Please re-submit the form.")


    # 🌍 Show Global Obesity Map
    with st.expander("🗺️ Show Global Obesity Risk Map", expanded=True):

        try:
            if not st.session_state.get("country"):
                st.warning("🌍 Please select your country first to view the map.")
            else:
                # Ülke adlarını normalize et (küçük harf ve boşluk temizliği)
                obesity_df["Country_clean"] = obesity_df["Country"].str.lower().str.strip()
                selected_country_clean = st.session_state.country.lower().strip()

                # Eşleşen ülke satırını al
                selected_row = obesity_df[obesity_df["Country_clean"] == selected_country_clean]

                if not selected_row.empty:
                    center_lat = selected_row["Latitude"].values[0]
                    center_lon = selected_row["Longitude"].values[0]
                    center_risk = selected_row["Risk"].values[0]

                    m = folium.Map(location=[center_lat, center_lon], zoom_start=4)

                    def risk_color(risk):
                        if risk >= 50:
                            return "darkred"
                        elif risk >= 40:
                            return "red"
                        elif risk >= 30:
                            return "orange"
                        elif risk >= 20:
                            return "yellow"
                        else:
                            return "green"

                    # Diğer ülkeleri çiz
                    for _, row in obesity_df.iterrows():
                        folium.CircleMarker(
                            location=[row['Latitude'], row['Longitude']],
                            radius=7,
                            color=risk_color(row['Risk']),
                            fill=True,
                            fill_opacity=0.5,
                            popup=f"{row['Country']}: {row['Risk']}% obesity risk",
                            tooltip=row['Country']
                        ).add_to(m)

                    # Kullanıcının ülkesini vurgula
                    folium.CircleMarker(
                        location=[center_lat, center_lon],
                        radius=10,
                        color=risk_color(center_risk),
                        fill=True,
                        fill_opacity=0.9,
                        popup=f"📍 You: {st.session_state.country} — {center_risk}% obesity risk",
                        tooltip=f"📍 You: {st.session_state.country}"
                    ).add_to(m)

                    st_folium(m, width=800, height=500)

                else:
                    st.warning(f"⚠️ Selected country '{st.session_state.country}' was not found in the dataset.")

        except Exception as e:
            st.error(f"🌍 Map could not be loaded. Error: {e}")


    # 🔐 OpenAI API Key Setup
    from dotenv import load_dotenv
    import openai
    import os
    import streamlit as st

    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")

    # GPT-powered Recipe Explanation Function
    def explain_recipe(recipe_name, ingredients=None, language="en"):
        system_prompt = {
            "tr": "Sen profesyonel bir diyetisyen ve beslenme uzmanısın. Tarifleri besin değerlerine, olası alerjenlere, hazırlanış önerilerine göre açıkla ve sağlıklı alternatifler öner. Ayrıca genel soruları da açıklayıcı ve güvenilir şekilde cevapla.",
            "en": "You are a professional dietitian and nutrition expert. Explain recipes in terms of nutritional value, potential allergens, preparation tips, and suggest healthy alternatives. Also answer general questions clearly and accurately."
        }[language]

        if ingredients:
            user_content = f"Recipe: '{recipe_name}'. Ingredients: {', '.join(ingredients)}. Explain and suggest improvements."
        else:
            user_content = recipe_name

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_content}
        ]

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
                temperature=0.7,
                max_tokens=400
            )
            return response["choices"][0]["message"]["content"]
        except Exception as e:
            return f"ChatGPT error: {str(e)}"


    # GPT-powered Recipe Explanation Function
    def explain_recipe(recipe_name, ingredients=None, language="en"):
        system_prompt = {
            "tr": "Sen profesyonel bir diyetisyen ve beslenme uzmanısın. Tarifleri besin değerlerine, olası alerjenlere, hazırlanış önerilerine göre açıkla ve sağlıklı alternatifler öner. Ayrıca genel soruları da açıklayıcı ve güvenilir şekilde cevapla.",
            "en": "You are a professional dietitian and nutrition expert. Explain recipes in terms of nutritional value, potential allergens, preparation tips, and suggest healthy alternatives. Also answer general questions clearly and accurately."
        }[language]

        if ingredients:
            user_content = f"Recipe: '{recipe_name}'. Ingredients: {', '.join(ingredients)}. Explain and suggest improvements."
        else:
            user_content = recipe_name

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_content}
        ]

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
                temperature=0.7,
                max_tokens=400
            )
            return response["choices"][0]["message"]["content"]
        except Exception as e:
            return f"ChatGPT error: {str(e)}"

    # CosmoFit Assistant Page
    st.title("🍽️ CosmoFit Assistant")
    st.write("Get personalized recipe insights and fitness suggestions!")

    # Retrieve user inputs from session state if available
    person = st.session_state.get("person", None)
    age = person.age if person else 28
    bmi = person.calculate_bmi() if person else 27.4
    activity = person.activity if person else "Light exercise"

    # Tabs for assistant
    tabs = st.tabs(["💬 Ask the Dietitian", "🧠 Recipe Analysis", "🏋️ Fitness Recommendation"])

    with tabs[0]:
        st.markdown("### 🤖 Talk to a dietitian")
        user_prompt = st.text_input("Ask anything (e.g. What is a ketogenic diet?)", key="dietitian_input")
        if st.button("Answer", key="dietitian_button"):
            if user_prompt.strip():
                chat_response = explain_recipe(user_prompt.strip(), ingredients=None, language="en")
                st.success(chat_response)

    with tabs[1]:
        st.markdown("### 📟 Get Recipe Feedback")
        recipe_name = st.text_input("Recipe Name", "Mexican Chicken Potato Soup", key="recipe_name")
        ingredients = st.text_area("Ingredients", "chicken, potatoes, onion, garlic, chili powder, cumin, broth", key="ingredients_input").split(",")
        if st.button("Explain Recipe", key="explain_button"):
            explanation = explain_recipe(recipe_name.strip(), [i.strip() for i in ingredients if i.strip()], language="en")
            st.info(explanation)

    with tabs[2]:
        st.markdown("### 🏃‍♀️ Fitness Plan Based on Your Goal")
        goal = st.radio("What is your fitness goal?", ["Lose weight", "Maintain fitness", "Gain weight"], key="goal_radio")

        st.markdown(f"#### 👤 Profile Summary: {age} years old | Activity: {activity} | BMI: {bmi}")

        st.markdown("#### 📋 Weekly Plan Suggestion")
        if goal == "Lose weight":
            st.markdown("""
            - Monday: 30 mins walk + 15 mins stretching
            - Tuesday: Light yoga or active rest
            - Wednesday: 20 mins cycling + core workout
            - Thursday: 40 mins swimming or brisk walk
            - Friday: Rest day
            - Saturday: 30 mins dance/pilates
            - Sunday: Outdoor walking + meditation
            """)
            st.video("https://www.youtube.com/watch?v=ml6cT4AZdqI")
            st.success("🏃 Recommended for moderate to high body mass index and sedentary lifestyle.")
        elif goal == "Maintain fitness":
            st.markdown("""
            - Monday: Strength + 20 mins cardio
            - Tuesday: Yoga + mobility
            - Wednesday: HIIT or cardio boxing
            - Thursday: Rest or stretching
            - Friday: Core + full body circuit
            - Saturday: Outdoor cycling or jog
            - Sunday: Rest
            """)
            st.video("https://www.youtube.com/watch?v=UBMk30rjy0o")
            st.info("💪 Great for maintaining a healthy routine.")
        elif goal == "Gain weight":
            st.markdown("""
            - Monday: Full body strength
            - Tuesday: Protein-rich meal prep + rest
            - Wednesday: Upper body focus + walk
            - Thursday: Rest + breathing exercises
            - Friday: Lower body strength
            - Saturday: Outdoor activities
            - Sunday: Stretching and nutrition planning
            """)
            st.video("https://www.youtube.com/watch?v=qXr7xHZUxvY")
            st.warning("🍽️ Make sure to consume more calories than you burn.")

        # 💬 AI-Powered Fitness Suggestions
        if st.button("💌 Get AI-Personalized Fitness Advice", key="fitness_advice"):
            prompt = f"I want to {goal.lower()}. My BMI is {bmi} and I am {age} years old. Suggest an ideal weekly workout plan with explanations."
            st.markdown("🤖 Generating suggestions from your virtual coach...")
            st.info(explain_recipe(prompt, language="en"))

        # 🧮 Estimate Calories Burned
        duration = st.slider("Select exercise duration (minutes)", 10, 120, 30, key="exercise_duration")
        burn_rate = {"Lose weight": 7, "Maintain fitness": 5, "Gain weight": 4}[goal]
        st.metric("🔥 Estimated Calories Burned", f"{duration * burn_rate} kcal")

        # 📅 Progress Tracker
        if st.checkbox("📅 Track My Weekly Progress", key="weekly_tracker"):
            st.markdown("#### Select Completed Days:")
            days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
            progress = {day: st.checkbox(day, key=f"day_{day}") for day in days}

        # 🌟 Daily Motivation
        if st.button("🌞 Get Daily Motivation", key="daily_motivation"):
            st.success(explain_recipe("Motivate me to continue exercising today.", language="en"))



    # 🧠 GPT: Explain a recipe
    def explain_recipe(recipe_name, ingredients=None):
        system_prompt = "You are a professional dietitian. Explain the recipe's nutritional value, allergens, tips, and healthy swaps."
        if ingredients:
            user_content = f"Recipe: '{recipe_name}'. Ingredients: {', '.join(ingredients)}. Please explain and give suggestions."
        else:
            user_content = recipe_name

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_content}
                ],
                temperature=0.7,
                max_tokens=400
            )
            return response["choices"][0]["message"]["content"]
        except Exception as e:
            return f"ChatGPT error: {e}"



    from PIL import Image
    import os
    # User feedback data (make sure the images are in the 'images/' folder)
    users = [
        {
            "name": "Selin Aksoy",
            "title": "Student",
            "comment": "With CosmoFit recipes, I'm eating healthy and learning how to cook. I lost 1.5 kg in 2 weeks!",
            "image": "/Users/ozgedoner/Desktop/CosmoFit/user_images/selin.png"
        },
        {
            "name": "Murat Aydın",
            "title": "HR Specialist",
            "comment": "The recipes are both practical and tasty. I maintain my shape with high-protein meals.",
            "image": "/Users/ozgedoner/Desktop/CosmoFit/user_images/murat.jpg"
        },
        {
            "name": "Ece Yıldız",
            "title": "Graphic Designer",
            "comment": "I feel more energetic. CosmoFit has become a guide to my healthy lifestyle.",
            "image": "/Users/ozgedoner/Desktop/CosmoFit/user_images/ece.png"
        },
        {
            "name": "Kaan Demir",
            "title": "Teacher",
            "comment": "I used to struggle with dieting, but CosmoFit recipes kept the flavor while I lost weight. I'm continuing!",
            "image": "/Users/ozgedoner/Desktop/CosmoFit/user_images/kaan.jpg"
        },
        {
            "name": "Zeynep Gül",
            "title": "Engineer",
            "comment": "It helped a lot with meal planning. My habits completely changed thanks to CosmoFit.",
            "image": "/Users/ozgedoner/Desktop/CosmoFit/user_images/zeynep.jpg"
        },
        {
            "name": "Emre Can",
            "title": "Software Developer",
            "comment": "Thanks to easy-to-make healthy recipes, I lost 3 kg even at the office. Highly recommended!",
            "image": "/Users/ozgedoner/Desktop/CosmoFit/user_images/emre.jpg"
        }
    ]

    # Title
    st.markdown("## 👥 User Testimonials")

    # Display each user testimonial
    for user in users:
        col1, col2 = st.columns([1, 3])
        with col1:
            if os.path.exists(user["image"]):
                st.image(Image.open(user["image"]), width=100)
            else:
                st.error("Image not found.")
        with col2:
            st.markdown(f"**{user['name']}**  \n*{user['title']}*")
            st.markdown(f"💬 {user['comment']}")
        st.markdown("---")


if __name__ == "__main__":
    app()
