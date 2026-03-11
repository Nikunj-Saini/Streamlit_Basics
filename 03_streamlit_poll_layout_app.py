import streamlit as st

st.title("Favourite Singer Poll")

col1, col2 = st.columns(2)

with col1:
    st.header("Singer 1")
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRRfH8OGjQrRF7t3j6O90lO_l9ikBnS9wonpegVod1gzon8ZQHOFTCYeXM&s")
    vote1 = st.button("Karan Aujla")

with col2:
    st.header("Singer 2")
    st.image("https://akm-img-a-in.tosshub.com/indiatoday/images/story/202506/diljit-dosanjh-reacts-to-criticism-of-speaking-only-about-punjab--not-india-260145597-16x9_0.jpg?VersionId=RIpTI1AllCWAdmxPPKam_Snr0.tsujrl&size=690:388")
    vote2 = st.button("Diljit Dosanjh")

# Voting result
if vote1:
    st.success("Thanks for choosing Karan Aujla")

elif vote2:
    st.success("Thanks for choosing Diljit")

# Sidebar inputs
name = st.sidebar.text_input("Enter your name")

tea = st.sidebar.selectbox(
    "Choose your thing",
    ["Dance", "Music", "Gym", "Gaming"]
)

st.write(f"Welcome {name}, and you have a good choice: {tea}")

# Expander section
with st.expander("Show the selection process"):
    st.write("""
    1. First Subscribe  
    2. Follow Ups  
    3. Repeat
    """)
