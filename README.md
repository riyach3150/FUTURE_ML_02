# 🎫 Support Ticket Classification

## 📌 Business Scenario
  * Customer support teams receive thousands of tickets daily.  
  * Manually categorizing and prioritizing tickets increases response time and operational cost.

    This project builds an ML-based NLP system that automatically:
  - Classifies support tickets into categories
  - Predicts ticket priority (High / Medium / Low)
   This helps reduce backlog and improve customer satisfaction.

---

## 🎯 Project Objective

- Read customer support ticket text
- Clean and preprocess text data
- Convert text into numerical features using TF-IDF
- Classify ticket category
- Predict ticket priority
- Evaluate model performance using standard metrics

---

## 🛠️ Technologies Used

- Python
- Pandas
- NLTK
- Scikit-learn
- TF-IDF Vectorization
- Logistic Regression
- Matplotlib & Seaborn

---

## 🔍 Methodology

### 1️⃣ Data Preprocessing
- Lowercasing
- Removing punctuation
- Removing numbers
- Stopword removal using NLTK

### 2️⃣ Feature Extraction
 TF-IDF (Term Frequency - Inverse Document Frequency) was used to convert text into numerical vectors.

### 3️⃣ Model Training
 Two Logistic Regression models were trained:

- Model 1 → Ticket Category Classification
- Model 2 → Priority Prediction

### 4️⃣ Evaluation Metrics
- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

---

## 📊 Results & Insights (CONFUSION MATRIX)

- The model successfully learned patterns from ticket text.
- High priority tickets were identified based on urgency-related keywords.
- Category classification showed strong performance across major ticket types.
- The confusion matrices for category and priority prediction compare the model’s actual vs predicted labels.

---

## 🚀 Example Prediction

Input:
```
Payment deducted but subscription not activated.
```

Output:
```
Category: Billing
Priority: High
```

---

## 📁 Repository Structure

```
support-ticket-classification-ml/
│
├── Support_Ticket_Classification.ipynb
├── Confusion_Matrix_CP.png
├── Confusion_Matrix_PP.png
├── customer_support_tickets.csv
├── README.md
└── requirements.txt
```

---

## 💡 Business Impact

- Faster ticket routing
- Reduced manual effort
- Improved SLA compliance
- Better customer experience

💻 [GitHub Code](https://github.com/riyach3150/FUTURE_ML_02)
🚀 [Live Demo](https://futureml02-ep2ya5y9kkdycekdwonce5.streamlit.app/)
