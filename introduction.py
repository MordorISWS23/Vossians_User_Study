import streamlit as st
import numpy as np
import pandas as pd
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.add_vertical_space import add_vertical_space
from formatting import format_sidebar_intro, write_footer

from faker import Faker
fake = Faker()
Faker.seed(42)

def sample(data):
    nickname = st.session_state["nickname"]

    # read csv and start random process
    df_samples = pd.read_csv(data)
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
    reduced_other_df.to_csv(f"data/{nickname}_ents.csv")
    sentences = []
    alive_dead = {"Angela Merkel": "is",
                  "Nelson Mandela": "was",
                  "Bill Gates": "is",
                  "Albert Einstein": "was",
                  "Mark Twain": "was",
                  "Ronald Reagan": "was"
                  }
    for i, row in reduced_other_df.iterrows():
        A = str(row['A'])
        B = str(row['B'])
        C = str(row['C'])
        sent = f"{A} {alive_dead[A]} the {B} of {C}"
        model = str(row['Model'])
        sentences.append((str(sent), model))
    df = pd.DataFrame(sentences, columns=["Sentence", "Model"])
    
    nickname = st.session_state["nickname"]
    df.to_csv(f"data/{nickname}_samples.csv")

def get_nickname():
    if "nickname" not in st.session_state:
        st.session_state["nickname"] = ""
    with st.form("formid"):
        placeholder = st.empty()
        text = placeholder.text_input(label="la", label_visibility="hidden", max_chars=20, help=None)
        st.session_state["nickname"] = text
        add_vertical_space(1)
        submission = st.form_submit_button("Submit")
        if submission:
            name = st.session_state['nickname']
            if len(name) > 1:
                name = name[0].upper() + name[1:]
                placeholder.empty()
                st.info(f"Thank you, {name}.")
            elif len(name) < 1:
                st.info(f"Please enter a nickname with at least one letter.")
            else:
                name = name[0].upper()
                placeholder.empty()
                st.info(f"Thank you, {name}.")
            add_vertical_space(3)


def display_intro():
    st.markdown(
        f"""
        <style>
        [data-testid="stSidebar"] > div:not(:first-child) {{
            margin-left: 50px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
    st.title("*Vossian Antonomasias*")
    add_vertical_space(2)
    with st.container():
        left_col, right_col = st.columns([1, 2], gap="large")

        left_col.subheader("Welcome to the Study 'Vossian Antonomasias'!")
        intro = "<p style='font-size: 25px;'>This is a research study that shall test whether machines can be as " \
                "<i>creative</i> as humans.</p>"
        left_col.markdown(intro, unsafe_allow_html=True)
        add_vertical_space(3)
        expander = st.expander("What are Vossian Antonomasias?")
        expander.markdown('<p style="font-size: 16px;">Vossian antonomasias refer to someone by a special '
                          'characteristic instead of their name.  \
                         <br>   For example, calling Bill Gates "the Henry Ford of the computer age" '
                          'highlights his influence as entrepeneur and his effect on the development of technology. \
                         <br> It is a way to describe someone by an important quality they possess. </p>',
                          unsafe_allow_html=True)
        add_vertical_space(2)
        left_col.empty()
        # Insert Image
        right_col.image(
            "data/hotpotAI_thunberg_parks_climate_change.png", width=300
        )
        right_col.markdown('<p style="font-size: 15px;">Picture created with hotpotAi inspired by: "Greta Thunberg '
                           'is the Rosa Parks of climate change."</p>', unsafe_allow_html=True)

    # Add some vertical space
    add_vertical_space(3)


def display_about_study():
    # ---- What to do in the study ----
    with st.container():
        how = "<p style='font-size: 25px;'>How the study works:</p>"
        st.markdown(how, unsafe_allow_html=True)

        st.markdown("<p style='font-size: 20px;'>1. You will be a given 21 sentences to rate that "
                    "were generated with different methods. We want to find out,"
                    " which method generates the best Vossian Antonomasias.</p>",
                    unsafe_allow_html=True)
        st.markdown("<p style='font-size: 20px;'>2. After rating the sentences,"
                    " we will ask you some questions about the persons that were in the sentences you rated.</p>",
                    unsafe_allow_html=True)
        add_vertical_space(1)
        
        st.session_state["nickname"] = fake.unique.ean(length=13)

        add_vertical_space(2)
        st.markdown('<p style="font-size: 20px; font-weight: bold;">About this study:</p>', unsafe_allow_html=True)
        st.markdown('<p style="font-size: 20px;">The entire study should take about 10 minutes. \
                     All your answers will be collected anonymously. \
                     We do not collect personal information, like your name. \
                     You are free to quit the study at any time. The data that we collect is stored on a server of '
                    'the University of Bremen, in Germany. \
                 After the study finishes, the data from all participants will be analysed '
                    'together and the results might be published in future research papers. '
                    'After finishing the experiment, it is not possible to withdraw your data '
                    'because of the anonymization. <br> If you have'
                    ' any questions about this study, please contact Johanna Rockstroh'
                    ' (rockstro@uni-bremen.de). <br> <br> If you want to proceed with the study, '
                    'please click "Start".</p>', unsafe_allow_html=True)

        st.markdown("<style>div.stButton>button:first-child {height: 2em; width: 4em; font-size:30px}</style>",

                    unsafe_allow_html=True)


def main():
    st.set_page_config(
        page_title="Vossian Antonomasias",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    format_sidebar_intro()
    display_intro()
    display_about_study()
    # Update status of start with button "start"
    start = st.button("Start")
    write_footer()
    # Check session state to switch page
    if start:
        if len(st.session_state["nickname"]) < 2:
            st.info("Please enter a nickname before continuing.")
        else:
            # create current sample
            sample("data/gen_sents.csv")
            # switch to page for ratings
            switch_page("vossian_antonomasias")


# Call the main function
main()
