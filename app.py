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
        "Data is everywhere, and it can tell us a lot about the risks that are present in today's world. Our app analyzes that data to inform you about the risks you might face in your daily life"
    )

    st.subheader("First, let us know more about you 🧑🏻")

    user_info = ()
    response = ""
    score = 0
    submit = False

    with st.form("user_info"):
        with open("data/states_dict.pickle", "rb") as filehandle:
            us_dict = pickle.load(filehandle)
            states_list = us_dict.keys()

        col1, col2, col3 = st.columns(3)

        gender = col1.selectbox("What is your gender?", ("Male", "Female"))
        age = col2.number_input("What's your age?", min_value=18, max_value=90, step=1)
        state = col3.selectbox("What State do you live in?", states_list)

        txt = st.text_area(
            "What's your thoughts 💭 on Health Insurance in the US",
            placeholder="I think health insurance is broken and needs to be changed",
        )
        submitted = st.form_submit_button("Submit")

        if submitted:
            user_info = (gender, age, state)
            response, score = google_nlp(txt)
            submit = True

    ## Visualizations

    if submit:

        st.success("Thanks for submitting!")

        st.subheader(response)

        with st.expander("See explanation"):
            st.markdown(f"The sentiment score for your respones was `{score}`")
            st.image("media/score-range.png")
            st.caption("Natural Language API by Google Cloud")

        st.write(
            "No matter how you feel about health insurance, here's some facts you should know 👇"
        )

        st.subheader("Being uninsured = delay in medical care")

        med_age, med_sex, med_time, med_type = med_care()

        st.plotly_chart(med_time)

        st.write(
            "It's clear from the chart above that people who are not insurend are more likely to delayed medical care. You never know when accidents can happen, and being uninsured can cost you your life."
        )

        st.subheader("The type of insurance also matters")

        st.plotly_chart(med_type)

        st.write(
            "The sad reality is, people who can afford private insurance will receive more care then other types, but even they are still much better than the uninsured."
        )

        st.header("Let's go into what risks you may face. 👇")

        gender = user_info[0]
        age = user_info[1]
        state = user_info[2]

        st.caption("Just to make sure we got it right,")
        st.markdown(f"#### You're a/an `{age}` y/o `{gender}` living in `{state}`")

        st.subheader(f"Recent trends in COVID cases at {state}")
        stats, covid_avg_plot = covid_avg(state)

        col1, col2 = st.columns(2)

        col1.metric("Cases (Daily Avg.)", stats[0], f"{stats[1]}%")
        col2.metric("Deaths (Daily Avg.)", stats[2], f"{stats[3]}%")
        st.caption("The green and red metrics are displaying 14-day changes")

        st.plotly_chart(covid_avg_plot)

        st.write(
            "With the recect impact of the pandemic, understanding the covid trends in the past 7 days and number of hospitalizations can help in realizing the how having an health insurance can help you"
        )

        ## Hospitalization

        st.write(
            "With the recect impact of the pandemic, understanding the covid trends in the past 7 days and number of hospitalizations can help in realizing the how having an health insurance can help you"
        )

        st.subheader(f"Hospitalization for COVID in {state}")

        (
            hosp_stats,
            covid_bed_state,
            inf_bed_state,
            bed_age,
        ) = hospitalization(state)

        col1, col2, col3 = st.columns(3)

        col1.metric("Confirmed Covid Cases (7 day Avg.)", hosp_stats[0])
        col2.metric("Suspected Covid Cases (7 day Avg.)", hosp_stats[1])
        col3.metric("Total Cases (7 day Avg.)", hosp_stats[2])

        st.plotly_chart(covid_bed_state)

        st.metric(f"Hospital Bed Utilization for {state}", hosp_stats[3])

        st.subheader("Hopsitalization for Influenza")

        st.plotly_chart(inf_bed_state)

        st.metric(f"Hospital Bed Utilization for {state}", hosp_stats[4])

        ## age stuff
        st.header(f"Now let's go into your age")

        st.subheader("here's what you need to know")

        st.plotly_chart(med_age)

        st.write(
            "People in the age group 25-34 are most likely to be delayed medical care"
        )

        if int(age) >= 25 and int(age) <= 34:
            st.write("You are in this age group")

        st.write("The hospital admissions for your age group")
        st.plotly_chart(bed_age)

        st.write("People in the age group 70-79 are most likely to be inpatients")

        if int(age) >= 70 and int(age) <= 79:
            st.write("You are in this age group")

        ## gender stuff

        st.subheader(f"As a {gender},")

        st.plotly_chart(med_sex)

        if gender == "Female":
            st.write(
                "You may be more likely to get delays in medical care compared to males"
            )
        else:
            st.write("You're not as likely as women to get delays in medical care.")

        mf_fig, top_fig = infec_dis()

        st.plotly_chart(mf_fig)

        if gender == "Female":
            st.write(
                "You may be more likely to contract an infectious diseases compared to males"
            )
            st.write(
                "You're more likely to get delays in medical care compared to males"
            )
        else:
            st.write("You're not as likely as women to have an infectious disease.")

        st.plotly_chart(top_fig)

        if gender == "Female":
            st.write("You should watch out for Chlamydia and gonorrhea")
        else:
            st.write("You may be more at risk to contract HIV and early syphillus.")

        st.subheader("Injuries")

        fatal, nonfatal = injuries()

        st.plotly_chart(fatal)

        if gender == "Female":
            st.write("You are less likely than males to have fatal injuries")
        else:
            st.write("You may be more at risk to fatal injuries from age 23 - 40.")

        st.plotly_chart(nonfatal)

        if gender == "Female":
            st.write("You are less likely than males to have fatal injuries")
        else:
            st.write("You may be more at risk to non-fatal injuries from age 23 - 50.")

        st.subheader("Hope you enjoyed the visualizations!")

        st.subheader("How to get insurance?")

        st.markdown(
            """
            ---
            ### Datasets we used to build this
            1. COVID-19 data by the New York Times
                - <https://github.com/nytimes/covid-19-data>
            2. COVID-19 and Influenza Reported Patient Impact and Hospital Capacity by State by HealthData.gov
                - <https://beta.healthdata.gov/Hospital/COVID-19-Reported-Patient-Impact-and-Hospital-Capa/g62h-syeh>
            3. Infectious Disease 2001-2014 - dataset by health by data.world
                - <https://data.world/health/infectious-disease-2001-2014>
            4. Web-based Injury Statistics Query and Reporting System by Injury Center|CDC
                - <https://www.cdc.gov/injury/wisqars/index.html>
            5. Delay or nonreceipt of needed medical care during the past 12 months due to cost by Centers for Disease Control and Prevention
                - <https://data.cdc.gov/NCHS/Delay-or-nonreceipt-of-needed-medical-care-prescri/dmzy-x2ad>)

            """
        )

        st.markdown("Check out [Anthem](https://www.anthem.com/) for insurance!")


if __name__ == "__main__":
    main()
