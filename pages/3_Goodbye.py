import streamlit as st
from formatting import format_sidebar_goodbye, write_footer
from streamlit_extras.add_vertical_space import add_vertical_space


class ThankYouPage:
    def __init__(self):
        self.thank_you = """
            ## Thank you for participating in the study!
            """
        self.text = '<p style="font-size: 20px;">We greatly appreciate your time and effort in  \
                 completing the questionnaire and providing valuable feedback. \
                 <br>  Your participation is instrumental in advancing our research. \
                 If you have any further questions or would like to learn more about the study,\
                please do not hesitate to contact Johanna Rockstroh. </p>'

        self.text1 = '<p style="font-size: 20px;">Thank you once again for your participation!</p>'
        self.impressum = '<p style="font-size: 12px; font-weight: bold;">Impressum</p>'
        self.address = '<p style="font-size: 12px;">Universität Bremen ' \
                       '<br> Bibliothekstraße 1 ' \
                       '<br> D-28359 Bremen </p>'
        self.legal = '<p style="font-size: 12px; font-weight: bold;">Rechtsform</p>'
        self.text_legal = '<p style="font-size: 12px;">Die Universität Bremen ist eine Körperschaft des ' \
                          'Öffentlichen Rechts. Sie wird durch die Rektorin Prof. Dr. Jutta Günther ' \
                          'gesetzlich vertreten.  ' \
                          '<br> Zuständige Aufsichtsbehörde ist die Senatorin für Wissenschaft' \
                          ' und Häfen, Katharinenstraße 37, 28195 Bremen. </p>'
        self.responsibility_cont = '<p style="font-size: 12px; font-weight: bold;">Inhaltliche Verantwortlichkeit ' \
                                   'i. S. v. § 5 TMG und § 18 Abs. 2 MStV</p>'
        self.text_res_cont = '<p style="font-size: 12px;">Für die Richtigkeit und Aktualität der veröffentlichten Inhalte ' \
                             '(auch Kommentare von Leser*innen) sind die jeweiligen Ersteller*innen der einzelnen Seiten ' \
                             'verantwortlich. Trotz sorgfältiger inhaltlicher Kontrolle übernehmen wir keine Haftung ' \
                             'für die Inhalte externer Links. Für den Inhalt der verlinkten Seiten sind ausschließlich ' \
                             'deren Betreiber verantwortlich.' \
                             '<br> <br> Johanna Rockstroh' \
                             '<br> Universität Bremen' \
                             '<br> Bibliothekstraße 5' \
                             '<br> D-28359 Bremen' \
                             '<br> Tel.: +49 421 218 64424' \
                             '<br> E-Mail: rockstro@uni-bremen.de  </p>'
        self.responsibility_tech = '<p style="font-size: 12px; font-weight: bold;">Technische Verantwortlichkeit ' \
                                   'i. S. v. § 5 TMG und § 18 Abs. 2 MStV</p>'
        self.text_res_tech = '<p style="font-size: 12px;">' \
                             'Johanna Rockstroh' \
                             '<br> Universität Bremen' \
                             '<br> Bibliothekstraße 5' \
                             '<br> D-28359 Bremen' \
                             '<br> Tel.: +49 421 218 64424' \
                             '<br> E-Mail: rockstro@uni-bremen.de </p>'
        self.image_descr = '<p style="font-size: 14px;">Picture created with hotpotAi inspired by: "Angela ' \
                           'Merkel is the PSY of politicians."</p>'

    def main(self):
        format_sidebar_goodbye()
        write_footer()
        st.markdown(self.thank_you, unsafe_allow_html=True)
        st.markdown(self.text, unsafe_allow_html=True)
        st.markdown(self.text1, unsafe_allow_html=True)
        add_vertical_space(2)
        st.image("data/hotpotAI_merkel_psy_politics.png")
        st.markdown(self.image_descr, unsafe_allow_html=True)
        add_vertical_space(6)
        st.markdown(self.impressum, unsafe_allow_html=True)
        st.markdown(self.address, unsafe_allow_html=True)
        st.markdown(self.legal, unsafe_allow_html=True)
        st.markdown(self.text_legal, unsafe_allow_html=True)
        st.markdown(self.responsibility_cont, unsafe_allow_html=True)
        st.markdown(self.text_res_cont, unsafe_allow_html=True)
        st.markdown(self.responsibility_tech, unsafe_allow_html=True)
        st.markdown(self.text_res_tech, unsafe_allow_html=True)


# Create an instance of the ThankYouPage class
thank_you_page = ThankYouPage()
# Call the main function
thank_you_page.main()
