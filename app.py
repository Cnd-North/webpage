# Gerrit van Rensburg
# 2022-03-22 
# Streamlit web-app


from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit.components.v1 import components

st.set_page_config(page_title="Gerrit's space on the web", page_icon=":pizza:", layout="wide")




def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Load assets

lottie_science_reading = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_au98facn.json")


# need to figure out how to incoprtate this into my site 
        # components.html(github_contributions)
        # st.markdown(github_contributions, unsafe_allow_htlm=True)
        
github_contributions = ''' <img src="http://ghchart.rshah.org/0040ff/Cnd-North" alt="My GitHub Contribution" /> '''

#github_contributions = ("https://github.com/users/Cnd-North/contributions")
#lottie_rising_squares = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_teb36nos.json")
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

img_key_draw_0 = Image.open("images/edge.png")
img_sales_prediction_0 = Image.open("images/sales_prediction_0.png")
img_sha_256 = Image.open("images/sha_256_gml_0.png")


# Header Section
with st.container():
    st.subheader("You've arrived - Welcome! :pineapple:")
    st.title("Multi-Disciplinary Problem Solver")
    st.write("Instinctive curiosity & critical thinking to solve problems with data at its core; a data stack of python, bash & sql")


# What I do
with st.container():
    st.write("---")  # insert horizontal divider line
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
        Currently working on a few projects - most of them are within Python.
        Reading up on SQL & Julia.
        
        
        

        
            """
        )

    st.markdown(github_contributions, unsafe_allow_html=True)
    st.write("My Github Contributions", "[| Github profile |](https://github.com/Cnd-North)")


    with right_column:
        st_lottie(lottie_science_reading, height=300, key="squares")
 




# Projects

with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))

    with image_column:
        st.image(img_key_draw_0)

    with text_column:
        st.subheader("Key code extraction from images of key")

        st.write(
            """
            The goal of the project is to store a digital version of physical keys as a backup.

            The Project is segmented into Three Phases - Currently on the first phase
                Phase 1 - Generate a dataset in the tens of thousands of keys and associated key codes.
                Phase 2 - Train a machine learning model to read key code based on images of keys.
                Phase 3 - Test the trained model on images real keys.
            """
        )
        st.markdown("[Additional hyperlink to project](https://www.duckduckgo.com)")

with st.container():
    image_column, text_column = st.columns((1, 2))

    with image_column:
        st.image(img_sales_prediction_0)
    
    with text_column:
        st.subheader("Sales Prediction using VARMAX")

        st.write(
            """
            Time Series Analysis & Forecasting of Store Sales using VARMAX.
            
            """
        )
        st.markdown("[Partner's Github: Abdul](https://github.com/abdul-data-diaries)")
        st.markdown("[Kaggle: Store Sales](https://www.kaggle.com/c/store-sales-time-series-forecasting)")


with st.container():
    image_column, text_column = st.columns((1, 2))

    with image_column:
        st.image(img_sha_256
        )
    
    with text_column:
        st.subheader("Hardware implementation of SHA-256")

        st.write(
            """
            Implementing the SHA-256 algorithm in Verilog.
            Validating the output with a SHA-256 algorithm implemented in python.
            Illustarted using GraphML
            
            """
        )
        st.markdown("[Partner's Github: JL](https://github.com/jt-l)")
        st.markdown("[Wikipedia: SHA-2 Hashing Family](https://en.wikipedia.org/wiki/SHA-2)")


# Plans for webpage expansion:

# WOULD BE AWESOME TO ADD SOME SIDE PAGES FOR INFO ON BOOKS I'VE READ OR INCORPRATE STORY GRAPH 
# Adding some side pages would be handy for displaying other interesting information

    # Would be great to add in IP tracking and have it added to a sqlite3 database 

    #     // get user details
    #     $user_agent = $_SERVER['HTTP_USER_AGENT']; //user browser
    #     $ip_address = $_SERVER["REMOTE_ADDR"];     // user ip adderss
    #     $page_name = $_SERVER["SCRIPT_NAME"];      // page the user looking
    #     $query_string = $_SERVER["QUERY_STRING"];   // what query he used
    #     $current_page = $page_name."?".$query_string; 


    # // get location 
    #     $url = json_decode(file_get_contents("http://api.ipinfodb.com/v3/ip-city/?key=/*userapikey*/
    #     // you can get your api key form http://ipinfodb.com/
    #     ip=".$_SERVER['REMOTE_ADDR']."&format=json"));
    #     $country=$url->countryName;  // user country
    #     $city=$url->cityName;       // city
    #     $region=$url->regionName;   // regoin
    #     $latitude=$url->latitude;    //lat and lon
    #     $longitude=$url->longitude;

    # // get time
    #     date_default_timezone_set('UTC');
    #     $date = date("Y-m-d");
    #     $time = date("H:i:s");

# Potentially add more into the key decoding project

# Potentially interface / build database for ETHmap project


    
    