import streamlit as st
import pandas as pd
data={"players":["Sanju","Jaiswal","Riyan"],"Run":[1100,1000,900]}
df=pd.DataFrame(data)
st.dataframe(df)
st.image("kr.jpg",caption="Radha Krishna")
st.video("VID.mp4")
