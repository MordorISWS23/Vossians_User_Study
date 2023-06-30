import streamlit as st
from formatting import format_sidebar_goodbye


class ThankYouPage:
    def __init__(self):
        self.page_title = "Thank You"
        self.thank_you = """
                    ## Thank you for participating in the study!
                    """
        self.text = '<p style="font-size: 20px;">We greatly appreciate your time and effort in  \
                         completing the questionnaire and providing valuable feedback. \
                         Your participation is instrumental in advancing our research. \
                          <br> If you have any further questions or would like to learn more about the study,\
                        please do not hesitate to contact Johanna Rockstroh. </p>'

        self.text1 = '<p style="font-size: 20px;">Thank you once again for your participation!</p>'

    def main(self):
        format_sidebar_goodbye()
        st.markdown(self.thank_you, unsafe_allow_html=True)
        st.markdown(self.text, unsafe_allow_html=True)
        st.markdown(self.text1, unsafe_allow_html=True)


# Create an instance of the ThankYouPage class
thank_you_page = ThankYouPage()
# Call the main function
thank_you_page.main()
