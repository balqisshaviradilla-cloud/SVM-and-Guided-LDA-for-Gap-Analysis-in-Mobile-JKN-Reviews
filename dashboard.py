import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("final_result_labeled_encoded.csv") 

st.title("📊 Dashboard Analisis Ulasan Aplikasi JKN")

# Sentimen (label_svm)
st.subheader("1. Jumlah Data Sentimen")
sentimen_counts = df['label_svm'].value_counts().sort_index()
fig1, ax1 = plt.subplots()
sentimen_counts.plot(kind='bar', color='skyblue', ax=ax1)
ax1.set_xlabel("Label Sentimen (0 = Negatif, 1 = Positif)")
ax1.set_ylabel("Jumlah")
st.pyplot(fig1)

# Topik LDA
st.subheader("2. Jumlah Data Topik LDA")
lda_counts = df['Topik_LDA'].value_counts()
fig2, ax2 = plt.subplots()
lda_counts.plot(kind='bar', color='orange', ax=ax2)
ax2.set_xlabel("Topik LDA")
ax2.set_ylabel("Jumlah")
st.pyplot(fig2)

# SERVQUAL Label
st.subheader("3. Jumlah Dimensi SERVQUAL")
servqual_counts = df['servqual_label'].value_counts()
fig3, ax3 = plt.subplots()
servqual_counts.plot(kind='bar', color='lightgreen', ax=ax3)
ax3.set_xlabel("Dimensi SERVQUAL")
ax3.set_ylabel("Jumlah")
st.pyplot(fig3)
