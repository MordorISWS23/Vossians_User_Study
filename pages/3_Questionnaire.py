import os
import pandas as pd
import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from formatting import format_sidebar_radio_question


class Questionnaire:
    def __init__(self, part_file):
        self.interests = None
        self.social_media_use = None
        self.education = None
        self.age = None
        self.gender = None
        self.participants_file = part_file
        self.page_id = None
        self.submitted = False

    def main(self):
        format_sidebar_radio_question()
        st.title("Some questions about yourself")
        st.subheader("Please fill out all of the following questions:")

        if os.path.exists(self.participants_file):
            df = pd.read_csv(self.participants_file)
            self.page_id = len(df)

        with st.form(key=str(self.page_id)):
            self.display_questions()
            submission = st.form_submit_button('Submit')
            if submission and not self.submitted:
                self.submitted = True
                self.demographics_to_df()
                switch_page("goodbye")

    def display_questions(self):
        self.gender = st.radio("What is your gender?", ("", "m", "f", "non-binary", "rather not say"),
                               horizontal=True, key=f"gender")
        self.age = st.radio("What is your age?", ("", "18-28", "28-38", "38-48", "48-58", "58-68"), horizontal=True,
                            key=f"age"
                            )
        self.education = st.radio("What is the highest level of education you have completed?",
                                  ("", "10th Grade", "High School Graduation",
                                   "Bachelor's Degree", "Master's Degree", "PhD"), key=f"education", horizontal=True
                                  )
        self.social_media_use = st.multiselect("What kind of social media platform do you use? "
                                               "(You may select multiple options)",
                                               ["Twitter", "Facebook", "Reddit", "Instagram", "Pinterest",
                                                "LinkedIn", "Whatsapp", "Signal", "Telegram", "other"],
                                               key=f"socialmedia"
                                               )

        self.interests = st.multiselect("What are you interested in? "
                                        "(You may select multiple options)",
                                        ["Music", "Politics", "Computers", "Art", "Sports",
                                         "other"],
                                        key=f"GIF_person"
                                        )

    def demographics_to_df(self):
        st.session_state.data = {
            "id": self.page_id,
            "age": self.age,
            "gender": self.gender,
            "education": self.education,
            "social_media_use": self.social_media_use,
            "interests": self.interests
        }

        # Write dictionary to dataframe
        data_part = st.session_state.get("data")
        df_id = pd.DataFrame([st.session_state.nickname], columns=["Participant"])
        if data_part:
            df_part = pd.DataFrame([data_part])
            df_part = df = pd.concat([df_id, df_part], axis=1)
            # Check if dataframe is empty (write)
            if not os.path.exists(self.participants_file):
                df_part.to_csv(self.participants_file)
            else:
                df_part.to_csv(self.participants_file, mode="a", header=False)


# Create an instance of the Questionnaire class
questionnaire = Questionnaire("data/participants.csv")
# Call the main function
questionnaire.main()
