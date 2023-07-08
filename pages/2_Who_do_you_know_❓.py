import random
import os
import streamlit as st
import pandas as pd
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.add_vertical_space import add_vertical_space
from formatting import format_sidebar_radio_know


class KnowledgeInquirer:
    def __init__(self, know_file, sample_file):
        self.knowledge_file = know_file
        self.submitted = False
        self.sample = sample_file
        self.entities = None

    def main(self):
        st.title("How well do you know these personalities?")
        format_sidebar_radio_know()
        if "data_know" not in st.session_state:
            st.session_state.data_know = {}
        df_samples = pd.read_csv(self.sample)
        self.get_entities(df_samples)
        #random.shuffle(self.entities)  # Randomly shuffle the entities
        self.inquire_knowledge_ents(self.entities)

    def get_entities(self, data):
        sources = list(data.source)
        targets = list(data.target)
        self.entities = list(set(sources + targets))

    def inquire_knowledge_ents(self, ents):
        key_know = 0
        for ent in ents:
            key_know += 1
            add_vertical_space(2)
            st.markdown(f"**{ent}**")
            knowledge = st.radio(label="label", label_visibility="hidden",
                                 options=("",
                                          "I know exactly who that person is.",
                                          "I have heard of the name but I cannot relate it to anything.",
                                          "I have never heard of that name before."), key=f"{ent}_{key_know}",
                                 horizontal=False)
            st.session_state.data_know[ent] = knowledge

        add_vertical_space(2)
        know_submit = st.button("Submit", key="submit")
        if know_submit and not self.submitted:
            self.submitted = True
            self.knowledge_to_df()
            switch_page("3_Goodbye")

    def knowledge_to_df(self):
        data_know = st.session_state.get("data_know")
        df_id = pd.DataFrame([st.session_state.nickname], columns=["Participant"])
        if data_know:
            df_know = pd.DataFrame([data_know])
            df_know = df = pd.concat([df_id, df_know], axis=1)
            # Check if dataframe is empty (write)
            if not os.path.exists(self.knowledge_file):
                df_know.to_csv(self.knowledge_file)
            else:
                df_know.to_csv(self.knowledge_file, mode="a", header=False)


# Create an instance of the KnowledgeInquirer class
inquirer = KnowledgeInquirer("data/knowledge_ents.csv", "data/samples.csv")
# Call the main function
inquirer.main()
