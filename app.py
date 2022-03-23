# Gerrit van Rensburg
# 2022-03-22 
# Streamlit web-app

from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Gerrit's space on the web", page_icon=":pizza:", layout="wide")




def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Load assets

lottie_rising_squares = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_teb36nos.json")
# lottie_square_interactivity = """

# <lottie-player id="firstLottie" src="https://assets1.lottiefiles.com/packages/lf20_teb36nos.json" style="width:400px; height: 400px;">"></lottie-player>

# <script>
# LottieInteractivity.create({
#     mode:"scroll",
#     player:'#firstLottie',
#     actions: [
#         {
#             visibility:[0,1],
#             type: "seek",
#             frames: [0, 31],
#         },
#     ]
# });
# </script>

# """

img_key_draw_0 = Image.open("images/key_draw_0.png")

# Header Section
with st.container():
    st.subheader("You've arrived - Welcome! :pineapple:")
    st.title("Multi-Disciplinary Problem Solver")
    st.write("I am driven by my curiousity currently transition from Excel to Python")


# What I do
with st.container():
    st.write("---")  # insert horizontal divider line
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
        Currently working on a few projects - most of them are within python.
        
        
        
        

        
            """
        )
        st.write("[Github profile >](https://github.com/Cnd-North)")

    with right_column:
        st_lottie(lottie_rising_squares, height=300, key="squares")
 




# Projects

with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))

    with image_column:
        st.image(img_key_draw_0)

    with text_column:
        st.subheader("One of my porjects focuses on..")

        st.write(
            """
            Additional text
            """
        )
        st.markdown("[Additional hyperlink to project](https://www.duckduckgo.com)")

# with st.container():
#     image_column, text_column = st.columns((1, 2))

#     with image_column:
#         st.image(image variable name)
    
#     with text_column:
#         st.subheader("One of my porjects focuses on..")

#         st.write(
#             """
#             Additional text
#             """
#         )
#         st.markdown("[Additional hyperlink to project](https://www.duckduckgo.com)")