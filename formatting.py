import pandas as pd
import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
from os.path import exists
from glob import glob


def display_num_participants():
    # manually write content into sidebar
    ratings_files = glob("data/*original.csv")
    return len(ratings_files)

def format_sidebar_intro():
    no_sidebar_style = """
            <style>
                div[data-testid="stSidebarNav"] {display: none;}
            </style>
        """
    st.markdown(no_sidebar_style, unsafe_allow_html=True)

    # hides button to close sidebar, open settings
    no_button_style = """
            <style>
                button[kind="header"] {display:none;}
            </style>
        """
    st.markdown(no_button_style, unsafe_allow_html=True)
    num_users = display_num_participants()
    with st.sidebar:
        add_vertical_space(8)
        pages = """
            ### <span style="color: #F4AA08">Introduction</span>

            ### Vossian Antonomasias

            ### Who do you know ❓

            ### Goodbye
            """
        st.markdown(pages, unsafe_allow_html=True)
        add_vertical_space(3)
        # add content to show number of prompts
        st.write(f"Number of participants: {num_users}")


def format_sidebar_goodbye():
    no_sidebar_style = """
            <style>
                div[data-testid="stSidebarNav"] {display: none;}
            </style>
        """
    st.markdown(no_sidebar_style, unsafe_allow_html=True)

    # hides button to close sidebar, open settings
    no_button_style = """
            <style>
                button[kind="header"] {display:none;}
            </style>
        """
    st.markdown(no_button_style, unsafe_allow_html=True)

    num_users = display_num_participants()
    with st.sidebar:
        add_vertical_space(8)
        pages = """
            ### Introduction

            ### Vossian Antonomasias

            ### Who do you know ❓

            ### <span style="color: #F4AA08">Goodbye</span>
            """
        st.markdown(pages, unsafe_allow_html=True)
        add_vertical_space(3)
        # add content to show number of prompts
        st.write(f"Number of participants: {num_users}")


def format_sidebar_radio_va():
    no_sidebar_style = """
                <style>
                    div[data-testid="stSidebarNav"] {display: none;}
                </style>
            """
    st.markdown(no_sidebar_style, unsafe_allow_html=True)

    # hides button to close sidebar, open settings
    no_button_style = """
                <style>
                    button[kind="header"] {display:none;}
                </style>
            """
    st.markdown(no_button_style, unsafe_allow_html=True)
    # hides the first option in a radio group
    # note: this applies to ALL radio groups across the app; it cannot be done for an individual button!
    st.markdown(
        """ <style>
                div[role="radiogroup"] >  :first-child{
                    display: none !important;
                }
            </style>
            """,
        unsafe_allow_html=True
    )

    num_users = display_num_participants()
    with st.sidebar:
        add_vertical_space(8)
        pages = """
                        ### Introduction

                        ### <span style="color: #F4AA08">Vossian Antonomasias</span>

                        ### Who do you know ❓

                        ### Goodbye
                        """
        st.markdown(pages, unsafe_allow_html=True)
        add_vertical_space(3)
        # add content to show number of prompts
        st.write(f"Number of participants: {num_users}")


def format_sidebar_radio_know():
    no_sidebar_style = """
                <style>
                    div[data-testid="stSidebarNav"] {display: none;}
                </style>
            """
    st.markdown(no_sidebar_style, unsafe_allow_html=True)

    # hides button to close sidebar, open settings
    no_button_style = """
                <style>
                    button[kind="header"] {display:none;}
                </style>
            """
    st.markdown(no_button_style, unsafe_allow_html=True)
    # hides the first option in a radio group
    # note: this applies to ALL radio groups across the app; it cannot be done for an individual button!
    st.markdown(
        """ <style>
                div[role="radiogroup"] >  :first-child{
                    display: none !important;
                }
            </style>
            """,
        unsafe_allow_html=True
    )

    num_users = display_num_participants()
    with st.sidebar:
        add_vertical_space(8)
        pages = """
                        ### Introduction

                        ### Vossian Antonomasias

                        ### <span style="color: #F4AA08">Who do you know ❓</span>

                        ### Goodbye
                        """
        st.markdown(pages, unsafe_allow_html=True)
        add_vertical_space(3)
        # add content to show number of prompts
        st.write(f"Number of participants: {num_users}")


def format_sidebar_radio_question():
    no_sidebar_style = """
                <style>
                    div[data-testid="stSidebarNav"] {display: none;}
                </style>
            """
    st.markdown(no_sidebar_style, unsafe_allow_html=True)

    # hides button to close sidebar, open settings
    no_button_style = """
                <style>
                    button[kind="header"] {display:none;}
                </style>
            """
    st.markdown(no_button_style, unsafe_allow_html=True)
    # hides the first option in a radio group
    # note: this applies to ALL radio groups across the app; it cannot be done for an individual button!
    st.markdown(
        """ <style>
                div[role="radiogroup"] >  :first-child{
                    display: none !important;
                }
            </style>
            """,
        unsafe_allow_html=True
    )

    num_users = display_num_participants()
    with st.sidebar:
        add_vertical_space(8)
        pages = """
                        ### Introduction

                        ### Vossian Antonomasias

                        ### Who do you know ❓

                        ### Goodbye
                        """
        st.markdown(pages, unsafe_allow_html=True)
        add_vertical_space(3)
        # add content to show number of prompts
        st.write(f"Number of participants: {num_users}")
