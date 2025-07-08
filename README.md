# 🛌 Sleep Disorder Prediction

This project uses Machine Learning to predict sleep disorders (Insomnia or Sleep Apnea) based on an individual's health and lifestyle data. The goal is to help identify people at risk of sleep disorders using a simple and effective predictive model.

## 📁 Project Structure

```
sleep-disorder-prediction/
├── Sleep_health.ipynb               # Jupyter Notebook with training and analysis
├── sleep_disorder_model.pkl         # Trained Decision Tree model (best accuracy)
├── sleep_health_dataset.csv         # Dataset used (from Kaggle)
├── app.py                           # Streamlit app for user input and predictions
├── requirements.txt                 # Dependencies used in the project
├── .gitignore                       # Files to ignore during Git operations
└── README.md                        # Project overview and instructions
```

## 📊 Dataset

- **Source**: Kaggle (Sleep Health and Lifestyle Dataset)
- Features include: Age, Gender, Occupation, Sleep Duration, Stress Level, BMI Category, Heart Rate, Blood Pressure, etc.

## 🧠 Models Used

- Logistic Regression
- Random Forest
- ✅ **Decision Tree (Best Accuracy)**

## ✅ Final Model

- Model: Decision Tree
- Saved as: `sleep_disorder_model.pkl`
- Target Variable: `Sleep Disorder` (Insomnia / Sleep Apnea)

## ⚠️ Disclaimer

This project is a machine learning demonstration and should **not** be used for medical diagnosis or treatment.
Please consult a licensed healthcare provider for professional advice.


## 🚀 How to Run the Streamlit App

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the app:

```bash
streamlit run app.py
```

3. Fill in your details on the web form and get a prediction!

## 💡 Features Used in Prediction

- Gender, Age, Occupation
- Sleep Duration, Quality of Sleep
- Physical Activity, Stress Level
- BMI Category, Heart Rate, Daily Steps
- Upper and Lower Blood Pressure

## 🛠 Tools & Libraries

- Python, Pandas, NumPy
- scikit-learn, matplotlib, seaborn
- Streamlit (for interface)

## 👨‍💻 Author

Adarsh Kumar Srivastava

---
