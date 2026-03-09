import streamlit as st
import pandas as pd
import nltk
import re
import string

from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# -------------------------
# TEXT CLEANING FUNCTION
# -------------------------
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'\d+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    words = [word for word in words if word not in stop_words]
    return " ".join(words)

# -------------------------
# TRAIN MODEL FUNCTION
# -------------------------
@st.cache_resource
def train_models():
    df = pd.read_csv("customer_support_tickets.csv") 
    df.columns = df.columns.str.strip()
    df = df[["Ticket Description", "Ticket Type", "Ticket Priority"]]
    df = df.dropna()
    df.columns = ["ticket", "category", "priority"]

    df["clean_ticket"] = df["ticket"].apply(clean_text)

    vectorizer = TfidfVectorizer(max_features=5000)
    X = vectorizer.fit_transform(df["clean_ticket"])

    model_category = LogisticRegression(max_iter=1000)
    model_category.fit(X, df["category"])

    model_priority = LogisticRegression(max_iter=1000)
    model_priority.fit(X, df["priority"])

    return vectorizer, model_category, model_priority


vectorizer, model_category, model_priority = train_models()

# -------------------------
# STREAMLIT UI
# -------------------------
st.title("🎫 Support Ticket Classification System")
st.write("Enter support ticket text to classify category and priority.")

user_input = st.text_area("Enter Support Ticket Text")

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter ticket text.")
    else:
        cleaned = clean_text(user_input)
        vector = vectorizer.transform([cleaned])

        category = model_category.predict(vector)[0]
        priority = model_priority.predict(vector)[0]

        st.success("Prediction Result")
        st.write(f"📂 Category: **{category}**")
        st.write(f"⚡ Priority: **{priority}**")
