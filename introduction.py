import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.add_vertical_space import add_vertical_space
from formatting import format_sidebar_intro

#TODO: delete text from textinput

def clear_nickname():
    st.session_state["text"] = ""

def get_nickname():
    if "text" not in st.session_state:
        st.session_state.text = ""
    st.markdown("<p style='font-size: 20px;'>To optimize the processing of the data that were collected"
                " in the study, we would like you to enter a nickname:</p>", unsafe_allow_html=True)
    nickname = st.text_input(label="la",  label_visibility="hidden", max_chars=20, key="text")
    st.session_state["nickname"] = nickname
    add_vertical_space(1)
    submission = st.button("Submit")
    if submission:
        st.info(f"Thank you, {st.session_state['nickname']}")
    add_vertical_space(3)


def display_intro():
    with st.container():
        left_col, right_col = st.columns([1, 2])
        with left_col:
            st.title("*Vossian Antonomasias*")
            st.subheader("Welcome to the Study 'Vossian Antonomasias'!")
            intro = "<p style='font-size: 25px;'>This is a research study that shall test whether machines can be as " \
                    "creative as" \
                    " humans. </i></p>"
            st.markdown(intro, unsafe_allow_html=True)
        with right_col:
            # Insert Image
            st.image(
                "data/hotpotAI_thunberg_parks_climate_change.png",
                width=200
            )

    # Add some vertical space
    add_vertical_space(3)


def display_about_study():
    # ---- What to do in the study ----
    with st.container():
        how = "<p style='font-size: 25px;'>How the study works:</p>"
        st.markdown(how, unsafe_allow_html=True)

        st.markdown("<p style='font-size: 20px;'>1. You will be a given X different sentences to rate. "
                    "Add more information.</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 20px;'>2. After rating the sentences,"
                    " we will ask you some questions about the persons that were in the sentences you rated.</p>",
                    unsafe_allow_html=True)
        st.markdown("<p style='font-size: 20px;'>4. Finally, we would like you to answer some questions about "
                    "yourself.</p>",
                    unsafe_allow_html=True)
        add_vertical_space(1)
        how = "<p style='font-size: 25px;'>Before the study starts:</p>"
        st.markdown(how, unsafe_allow_html=True)

        get_nickname()

        st.markdown('<p style="font-size: 20px; font-weight: bold;">About this study:</p>', unsafe_allow_html=True)
        st.markdown('<p style="font-size: 20px;">The entire study should take about 10 minutes. \
                     All your answers will be collected anonymously. \
                     We do not collect personal information, like your name or IP address. \
                     You are free to quit the study at any time. The data that we collect is stored on a server of '
                    'the University of XXX, in XXX. \
                 After the study finishes, the data from all participants will be analysed '
                    'together and the results might be published in future research papers. '
                    'After finishing the experiment, it is not possible to withdraw your data '
                    'because of the anonymization. <br> If you have'
                    'any questions about this study, please contact: XXX'
                    ' (XXX@XXX) <br> <br> If you want to proceed with the study, '
                    'please click "Start"!</p>', unsafe_allow_html=True)

        st.markdown("<style>div.stButton>button:first-child {height: 2em; width: 4em; font-size:30px}</style>",

                    unsafe_allow_html=True)


def main():
    st.set_page_config(
        page_title="Vossian Antonomasias",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    if "nickname" not in st.session_state:
        st.session_state.nickname = None
    format_sidebar_intro()
    display_intro()
    display_about_study()
    # Update status of start with button "start"
    start = st.button("Start")
    # Check session state to switch page
    if start:
        if st.session_state.nickname is None:
            st.info("Please enter a nickname.")
        else:
            switch_page("vossian_antonomasias")


# Call the main function
main()
