import streamlit as st
import streamlit.components.v1 as components

import pandas as pd

from google_nlp import *
import pickle


def main():
    ## streamlit config
    st.set_page_config(
        page_title="Ensurance",
        page_icon="🏥",
        initial_sidebar_state="expanded",
    )

    st.title("Do you need insurance?")
    st.subheader("Get recommendations on insurance for your travels!")

    with st.form("thoughts"):
        st.write("What are your thoughts on Health Insurance in the US?")
        txt = st.text_area("Don't worry, only you can see this")

        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write("Sentiment:", google_nlp(txt))

    st.subheader("Let us know more about you")

    with open("data/us_states.data", "rb") as filehandle:
        us_list = pickle.load(filehandle)

    with st.form("user_info"):
        gender = st.selectbox("What is your gender?", ("Male", "Female"))
        age = st.number_input("What's your age?", min_value=18, max_value=90, step=1)
        state = st.selectbox("What State do you live in?", us_list)
        submitted = st.form_submit_button("Submit")

        if submitted:
            user_info = (gender, age, state)


if __name__ == "__main__":
    main()
