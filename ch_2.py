import streamlit as st

st.title("Singer choice")
if st.button("Playlist"):
    st.success("Your Playlist has started ")

add_songs = st.checkbox("Add songs")

if add_songs:
    st.write("Song has been added to your Playlist ")

song_type = st.radio("Whose Concert you want to Visit:",["Karan Aujla","Diljit", "Navan Sandhu", "Mita Ror"])
st.write(f"Starting Song of {song_type}")
Singer = st.selectbox("Choose your Singer",["Akhil","Jass Manak", "Guru Randhawa "])
st.write(f"Selected Singer  {Singer}")


fees = st.slider("Fees level", 5000, 20000,10000)
st.write(f"Selected level  {Singer}")

ticket = st.number_input("How many Tickets", min_value=1,max_value=10, step = 1)
st.write(f"Selected the number of the ticket  {Singer}")
name = st.text_input("Enter your Name ")
if name :
    st.write(f"Welcome, {name}! Your have Successfully Purchased the Ticket ")

dob = st.date_input("Select you date of birth")
st.write(f"Your Date of Birth {dob}")
