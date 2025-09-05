# Beverage Price Prediction – CodeX Project

## 📌 Overview
This project was developed as part of the **Codebasics Virtual Internship** with AtliQ Technologies.  
The goal was to build a **machine learning model** that predicts the most suitable **price range** for a beverage product, based on consumer survey data.

Pricing is one of the most critical business decisions in the beverage industry.  
Our model helps companies avoid costly pricing errors by recommending price ranges that align with consumer demographics, habits, and preferences.

---

## 🗂 Project Structure
```
beverage-price-prediction/
│── artifacts/
│   └── model_data.joblib        # Saved ML model & encoders
│
│── Jupyter notebook/            # EDA & model development notebooks
│── main.py                      # Streamlit app (frontend mockup)
│── prediction_helper.py         # Helper functions for prediction
│── README.md                    # Project documentation
│── .gitignore
```

---

## ⚙️ Features
- Cleaned and analyzed consumer survey data.
- Applied **feature engineering** to capture customer behaviors.
- Built a classification model to predict beverage price ranges:
  - Price buckets: *50-100, 100-150, 150-200, 200-250*.
- **Streamlit mockup app** for interactive predictions.
- Provides **business-ready insights** for market entry strategies, packaging, and consumer targeting.

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/beverage-price-prediction.git
cd beverage-price-prediction
```

### 2. Install Dependencies
It’s recommended to use a virtual environment:
```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit App
```bash
streamlit run main.py
```

---

## 🧑‍💻 How It Works
1. The user inputs consumer details (age, income, preferences, etc.) through the Streamlit interface.  
2. Encoders and the trained model (saved in `artifacts/model_data.joblib`) transform the inputs.  
3. The app outputs the most likely **price range** that customers in that segment would accept.  

---

## 📊 Business Use Cases
- **Market Entry**: Identify optimal price ranges for launching new beverages.  
- **Product Line Design**: Differentiate pricing for 250ml, 500ml, 1L packages.  
- **Dynamic Pricing**: Adjust prices across channels (retail vs. online).  
- **Investor Confidence**: Show data-driven strategies for profitability.  

---

## 🛠 Tech Stack
- **Python**, **scikit-learn**, **XGBoost**  
- **Streamlit** (frontend mockup)  
- **pandas**, **NumPy**, **joblib**  

---

## 🙌 Acknowledgements
This project was completed as part of the  
**#CodebasicsVirtualInternship** led by Dhaval Patel and Hemanand Vadivel.  
Special thanks to the Codebasics community for guidance and support.  

---

## 📬 Contact
**Bharath Srinivas**  
- LinkedIn: [linkedin.com/in/bharath-srinivas-286460344](https://linkedin.com/in/bharath-srinivas-286460344)  
 
