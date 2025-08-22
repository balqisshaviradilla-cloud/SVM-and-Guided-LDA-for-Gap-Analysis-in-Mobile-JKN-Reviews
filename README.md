## 📱Sentiment Analysis & Topic Modeling on Mobile JKN Reviews

# 📌 Project Overview

This project is my undergraduate thesis, focusing on sentiment analysis and topic modeling of user reviews from the Mobile JKN application (Indonesia’s National Health Insurance mobile app). The main goal is to perform a Gap Analysis by combining:
- Support Vector Machine (SVM) → for sentiment classification (positive, negative, neutral)
- Guided Latent Dirichlet Allocation (Guided LDA) → for topic modeling, mapping review topics to SERVQUAL dimensions (Reliability, Assurance, Tangibles, Empathy, Responsiveness)
This approach helps identify the gap between user expectations and perceived service quality, providing insights for improving digital public services.

## ⚙️ Methodology
The workflow of this research follows the CRISP-DM framework:
- Data Collection → Scraping 6,186 Google Play Store reviews of Mobile JKN
- Data Preprocessing → Case folding, normalization, tokenization, stopword removal
- Sentiment Analysis → Using SVM classifier
- Topic Modeling → Applying Guided LDA to map topics into SERVQUAL dimensions
- Gap Analysis → Identifying gaps between expectation vs perception based on SERVQUAL

## 🛠️ Tech Stack
- Python 🐍
- Scikit-learn → SVM implementation
- Gensim → Guided LDA modeling
- NLTK & Sastrawi → Text preprocessing (Indonesian language)
- Pandas, NumPy → Data handling
- Matplotlib → Visualization
- Streamlit → Interactive dashboard

## 📊 Key Results
- Classified sentiments of user reviews with SVM
- Identified topics in reviews mapped to SERVQUAL dimensions
- Performed Gap Analysis to highlight service areas that need improvement in Mobile JKN
