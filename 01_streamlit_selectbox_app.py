import streamlit as st
st.title("Hello Bacha Party")
st.subheader("Crushed With the T i lllp ")
st.text('N i k u n j    A a l i y a   R e e ')
st.write("Choose your Favorite Singer")

singers = st.selectbox("Your fav singer :", ["Karan Aujla","Diljit","Akhil","Guru"])
st.write(f"You have choosen {singers} You have a very great choice" )
st.success(f"Your are Done  Now proceed to the next step ")

