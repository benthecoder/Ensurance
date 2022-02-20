from platformdirs import user_runtime_dir
import streamlit as st
import streamlit.components.v1 as components

import pandas as pd

from google_nlp import *
import pickle

from visualizations import *


def main():
    st.set_page_config(
        page_title="Ensurance",
        page_icon="⚕️",
        initial_sidebar_state="expanded",
    )

    st.title("Ensurance 🏥📄")
    st.caption("Ensuring you to get the insurance you need!")

    ## User submission
    st.write(
        "Health matters. That's why we're here to provide more information about the risks you may face every day"
    )

    # st.subheader("First, let us know more about you 🧑🏻")

    # user_info = ()
    # response = ""
    # score = 0
    # submit = False

    # with st.form("user_info"):
    #     with open("data/states_dict.data", "rb") as filehandle:
    #         us_dict = pickle.load(filehandle)
    #         states_list = us_dict.values()

    #     col1, col2, col3 = st.columns(3)

    #     gender = col1.selectbox("What is your gender?", ("Male", "Female"))
    #     age = col2.number_input("What's your age?", min_value=18, max_value=90, step=1)
    #     state = col3.selectbox("What State do you live in?", states_list)

    #     txt = st.text_area(
    #         "What's your thoughts 💭 on Health Insurance in the US",
    #         placeholder="I think health insurance is broken and needs to be changed",
    #     )
    #     submitted = st.form_submit_button("Submit")

    #     if submitted:
    #         user_info = (gender, age, state)
    #         response, score = google_nlp(txt)
    #         submit = True

    # ## Visualizations
    # indent the code below
    # if submit:
    user_info = ("Male", 18, "Alaska")

    # st.success("Thanks for submitting!")

    # st.subheader(response)

    # with st.expander("See explanation"):
    #     st.markdown(f"The sentiment score for your respones was `{score}`")
    #     st.image("media/score-range.png")
    #     st.caption("Natural Language API by Google Cloud")

    st.subheader(
        "Here's some information about health insurance and delays Medical Care"
    )

    med_age, med_sex, med_time, med_type = med_care()

    st.plotly_chart(med_time)

    st.plotly_chart(med_type)

    st.subheader("Here's what we know about you 👇")

    gender = user_info[0]
    age = user_info[1]
    state = user_info[2]

    ## State stuff

    st.markdown(f"#### You're a/an `{age}` y/o `{gender}` living in `{state}`")

    st.subheader(f"Here are some risks you may face at {state}")

    st.subheader(f"Recent trends in Covid cases at {state}")
    stats, covid_avg_plot = covid_avg(state)

    col1, col2 = st.columns(2)

    col1.metric("Cases (Daily Avg.)", stats[0], f"{stats[1]}%")
    col2.metric("Deaths (Daily Avg.)", stats[2], f"{stats[3]}%")
    st.caption("The green and red metrics are displaying 14-day changes")

    st.subheader(f"COVID cases and deaths in {state}")
    st.caption("daily average for the past 90 days")

    st.plotly_chart(covid_avg_plot)

    ## Hospitalization

    hosp_stats, covid_bed_state, inf_bed_state, bed_age = hospitalization(state)

    col1, col2, col3 = st.columns(3)

    col1.metric("Confirmed Covid Cases (7 day Avg.)", hosp_stats[0])
    col2.metric("Suspected Covid Cases (7 day Avg.)", hosp_stats[1])
    col3.metric("Total Cases (7 day Avg.)", hosp_stats[2])

    st.plotly_chart(covid_bed_state)
    st.plotly_chart(inf_bed_state)
    st.plotly_chart(bed_age)

    st.subheader("Hopsitalization for COVID")

    st.subheader("Hopsitalization for Influenza")

    ## age stuff

    st.subheader(f"For people in your age group, here's what you need to know")

    st.write("The hospital admissions for your age group")
    st.plotly_chart(med_age)

    ## gender stuff

    st.subheader(f"As a {gender},")

    st.plotly_chart(med_sex)

    if gender == "Female":
        st.write("You're more likely to contract these diseases compared to males")
        st.write("You're more likely to get delays in medical care compared to males")
    else:
        st.write(
            "Throughout life, you're twice as likely as women to have a heart attack.!"
        )

    mf_fig, top_fig = infec_dis()

    st.plotly_chart(mf_fig)
    st.plotly_chart(top_fig)

    st.subheader("Hope you enjoyed the visualizations!")

    st.markdown(
        """
        ## Data Sources
        - source1
        - source2
        - source3
        """
    )


if __name__ == "__main__":
    main()
