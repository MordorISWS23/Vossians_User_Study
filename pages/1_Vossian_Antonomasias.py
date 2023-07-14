import streamlit as st
import pandas as pd
import numpy as np
import os
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.add_vertical_space import add_vertical_space
from formatting import format_sidebar_radio_va


class VossianAntonomasiasRater:
    def __init__(self, samples, ratings_fit, ratings_original, ratings_understand):
        self.sentences = list()
        self.samples = samples
        self.final_sample = None
        self.ratings_fit = ratings_fit
        self.ratings_original = ratings_original
        self.ratings_understand = ratings_understand
        self.submitted = False

    def main(self):
        format_sidebar_radio_va()
        if "data_VA_original" not in st.session_state:
            st.session_state["data_VA_original"] = {}
            st.session_state["data_VA_fit"] = {}
            st.session_state["data_VA_understand"] = {}
        st.title("Rate Vossian Antonomasias")
        st.markdown('<p style="font-size: 20px;">Please rate the following sentences with <b>1</b> being the best and '
                    '<b>5</b> being the worst evaluation.</p>', unsafe_allow_html=True)
        # create final version of data sample, new one for every participant
        self.sample()
        print(self.final_sample)
        alive_dead = {"Angela Merkel": "is",
                      "Nelson Mandela": "was",
                      "Bill Gates": "is",
                      "Alber Einstein": "was",
                      "Mark Twain": "was",
                      "Ronald Reagan": "was"
                      }
        # generate sentences from entities and domain
        for i, row in self.final_sample.iterrows():
            A = str(row['A'])
            B = str(row['B'])
            C = str(row['C'])
            sent = f"{A} {alive_dead[A]} the {B} of {C}"
            self.sentences.append(sent)
        self.handle_ratings()

    def sample(self):
        # read csv and start random process
        df_samples = pd.read_csv(self.samples)
        # randomly select combination of one A and one model for every unique value of model and A -> 42 sentences
        random_rows = df_samples.groupby(['A', 'Model']).apply(lambda x: x.sample(n=1)).reset_index(drop=True)
        # randomly select 3 A's so that every A has a unique method
        sampled_values = random_rows["A"].drop_duplicates().sample(n=3, replace=False)
        # reduce dataframe to randomly selected three A's -> 21 sentences
        reduced_other_df = random_rows[random_rows['A'].isin(sampled_values)]
        # shuffle dataframe based on column "model"
        reduced_other_df['Model'] = np.random.permutation(reduced_other_df['Model'].values)
        reduced_other_df = reduced_other_df.sort_values(by=['A'])
        reduced_other_df.reset_index(drop=True)
        self.final_sample = reduced_other_df

    def handle_ratings(self):
        key_fit = 0
        key_original = 0
        key_understand = 0
        for sent in self.sentences:
            key_fit += 1
            key_original += 1
            key_understand += 1
            add_vertical_space(2)
            st.markdown(f"**{sent}**")
            rating_fit = st.radio(label="How well does this description fit?", options=(0, 1, 2, 3, 4, 5),
                                  key=f"{key_fit}_fit",
                                  horizontal=True)
            rating_understand = st.radio(label="How understandable is this description?", options=(0, 1, 2, 3, 4, 5),
                                         key=f"{key_understand}_understand",
                                         horizontal=True)
            rating_original = st.radio(label="How original is this description?", options=(0, 1, 2, 3, 4, 5),
                                       key=f"{key_original}_original",
                                       horizontal=True)
            st.session_state.data_VA_fit[sent] = rating_fit
            st.session_state.data_VA_understand[sent] = rating_understand
            st.session_state.data_VA_original[sent] = rating_original
        rating_submit = st.button("Submit", key=f"submit_all")
        if rating_submit and not self.submitted:
            self.submitted = True
            self.ratings_to_df()
            switch_page("Who_do_you_know_❓")

    def ratings_to_df(self):
        df_id = pd.DataFrame([st.session_state.nickname], columns=["Participant"])
        data_VA_fit = st.session_state.get("data_VA_fit")
        data_VA_original = st.session_state.get("data_VA_original")
        data_VA_understand = st.session_state.get("data_VA_understand")

        if data_VA_fit:
            df_fit = pd.DataFrame([data_VA_fit])
            df_fit = pd.concat([df_id, df_fit], axis=1)
            if not os.path.exists(self.ratings_fit):
                df_fit.to_csv(self.ratings_fit)
            else:
                df_fit.to_csv(self.ratings_fit, mode="a", header=False)

        if data_VA_original:
            df_original = pd.DataFrame([data_VA_original])
            df_original = pd.concat([df_id, df_original], axis=1)
            if not os.path.exists(self.ratings_original):
                df_original.to_csv(self.ratings_original)
            else:
                df_original.to_csv(self.ratings_original, mode="a", header=False)

        if data_VA_understand:
            df_understand = pd.DataFrame([data_VA_understand])
            df_understand = pd.concat([df_id, df_understand], axis=1)
            if not os.path.exists(self.ratings_understand):
                df_understand.to_csv(self.ratings_understand)
            else:
                df_understand.to_csv(self.ratings_understand, mode="a", header=False)


# Create an instance of the VossianAntonomasiasRater class
rater = VossianAntonomasiasRater(samples="data/gen_sents.csv", ratings_fit="data/ratings_fit.csv", ratings_original="data/ratings_original.csv",
                                 ratings_understand="data/ratings_understand.csv")
# Call the main function
rater.main()
