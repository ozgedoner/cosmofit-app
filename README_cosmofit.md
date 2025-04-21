
<h1 align="center">CosmoFit - AI Powered Diet & Recipe Recommendation System</h1>
<div align="center"><img src="assets/banner.jpg" width="60%" />
  <h4>A smart diet assistant offering personalized food suggestions using ML, FastAPI, Streamlit, and ChatGPT.</h4>
</div>

# CosmoFit

## :bookmark_tabs: Table of Contents
* [General Info](#general-info)
* [Architecture](#architecture)
* [Technologies](#technologies)
* [Setup](#setup)
* [Authors](#authors)
* [Dataset](#dataset)

---

## :scroll: General Info

### 🔍 Objective

CosmoFit is a smart nutrition assistant that generates personalized, healthy recipe recommendations based on user inputs such as age, gender, height, weight, activity level, and health goals.  
It analyzes user profiles and food content using machine learning to support healthy eating habits, improve engagement, and enhance long-term well-being.

---

## 🏗️ Architecture

CosmoFit's architecture includes:

- **Frontend**: Streamlit app with modules for calorie, BMI, protein needs, waist-hip ratio, and more
- **Backend**: FastAPI server for managing user input, model communication and image handling
- **Recommendation Engine**: Unsupervised clustering (K-Means), classification (Random Forest), and cosine similarity
- **Deployment**: Dockerized setup with multi-service support (API, UI)

<p align="center"><img src="assets/architecture.png" width="70%"/></p>

---

## 🔧 Technologies Used

- Python 3.10
- scikit-learn
- pandas, numpy
- FastAPI
- Streamlit
- Docker & Docker Compose
- ChatGPT integration
- Matplotlib, seaborn (for EDA)

![](https://img.icons8.com/color/48/null/python--v1.png)
![](https://img.icons8.com/color/48/null/numpy.png)
![](https://img.icons8.com/color/48/null/pandas.png)
![](https://img.icons8.com/color/48/streamlit.png)
![](https://img.icons8.com/color/48/fastapi.png)

---

## :whale: Setup Instructions

### Run Locally

```bash
# Clone this repo
git clone https://github.com/YOUR_USERNAME/CosmoFit
cd CosmoFit

# Install requirements
pip install -r requirements.txt

# Start the app
streamlit run app/main.py
```

### With Docker Compose

```bash
docker-compose up -d --build
```
Then open `http://localhost:8501` in your browser.

---

## 📦 Dataset

Due to GitHub's file size limits, the dataset is not included in this repository.  
You can download it from the following link and place it under the `Data/` folder:

🔗 **[Download dataset from Google Drive](https://drive.google.com/file/d/1CaP8rNXXjRpfLoH__2-LPPjyk-qKAYi_/view?usp=share_link)**

---

## 👩‍💻 Authors

- [Ezgi Bahadır](https://www.linkedin.com/in/ezgi-bahad%C4%B1r-49a9601b9/) • [GitHub](https://github.com/ezgi-bhdr)
- [Gamze Kızılkaya](https://www.linkedin.com/in/gamze-k%C4%B1z%C4%B1lkaya-02481616b/) • [GitHub](https://github.com/KIZILKAYA538)
- [Özge Rabia Döner](https://www.linkedin.com/in/ozgerabiadoner/) • [GitHub](https://github.com/ozgedoner)

---
