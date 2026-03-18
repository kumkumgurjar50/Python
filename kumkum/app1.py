import streamlit as st
st.title("Wel Come")
st.sidebar.title("Menu")
option=st.sidebar.selectbox("Select Option",["Home","About"])
col1,col2=st.columns(2)
col1.write("Left")
col2.write("Right")
with st.expander("More"):
    st.write("Hidden text")
