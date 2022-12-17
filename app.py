import streamlit as st
import numpy as np
from pandas import DataFrame
# from keybert import KeyBERT
import seaborn as sns
import os
import json

import tika
tika.initVM()
from tika import parser

# from transformers import AutoTokenizer, AutoModelForSequenceClassification
# from transformers_interpret import SequenceClassificationExplainer


st.set_page_config(
    page_title="Классификация и анализ договоров",
    page_icon="🎈",
)

def _max_width_():
    max_width_str = f"max-width: 1400px;"
    st.markdown(
        f"""
    <style>
    .reportview-container .main .block-container{{
        {max_width_str}
    }}
    </style>    
    """,
        unsafe_allow_html=True,
    )
_max_width_()

st.title("🔑 Классификация и анализ договоров")
st.header("")

st.markdown("")
st.markdown("## 📌 Загрузите документы")

uploaded_files = st.file_uploader('doc, docx, pdf',
                                  accept_multiple_files=True)

if uploaded_files:
    st.text(parser.from_file(uploaded_files[0])['content'])

# if uploaded_files:

#     @st.cache(allow_output_mutation=True)
#     def load_model():
#         return KeyBERT("sberbank-ai/ruBert-base")
#     kw_model = load_model()

#     @st.cache(allow_output_mutation=True)
#     def load_clf_model():
#         model_ = AutoModelForSequenceClassification.from_pretrained('model2')
#         tokenizer = AutoTokenizer.from_pretrained('sberbank-ai/ruBert-base')
#         return model_, tokenizer
#     clf_model, clf_tokenizer = load_clf_model()

#     for doc in 

#     keywords = kw_model.extract_keywords(
#         doc,
#         keyphrase_ngram_range=(1, 10),
#         top_n=10,
#     )

#     st.header("")

#     df_key = (
#         DataFrame(keywords, columns=["Keyword/Keyphrase", "Relevancy"])
#         .sort_values(by="Relevancy", ascending=False)
#         .reset_index(drop=True)
#     )
#     df_key.index += 1

#     # Add styling
#     cmGreen = sns.light_palette("green", as_cmap=True)
#     cmRed = sns.light_palette("red", as_cmap=True)
#     df = df_key.style.background_gradient(cmap=cmGreen, subset=["Relevancy"])

#     c1, c2, c3 = st.columns([1, 3, 1])
#     format_dictionary = {
#         "Relevancy": "{:.1%}",
#     }
#     df_key = df_key.format(format_dictionary)
#     with c2:
#         st.table(df_key)
