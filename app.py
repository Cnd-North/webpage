# Gerrit van Rensburg
# 2022-03-22 
# Streamlit web-app


import streamlit as st

st.set_page_config(page_title="Gerrit's space on the web", page_icon=":pizza:", layout="wide")

# Header Section
with st.container():
    st.subheader("You've arrived - Welcome! :pineapple:")
    st.title("Multi-Disciplinary Problem Solver")
    st.write("I am driven by my curiousity currently transition from Excel to Python")


# What I do
with st.comntainer():
    st.write("---")  # insort horizontal divider line
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
        Currently working on a few projects - most of them are within python.
        
        
        
        
        
        
        
        
        
            """
        )
        st.write("[Github profile >] (https://github.com/Cnd-North)")

        
