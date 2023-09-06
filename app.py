import streamlit as st
import joblib

model = joblib.load('model_joblib_test')

st.title("Big Mart Sales Prediction")

Item_Identifier  = st.number_input("Item_Identifier")
Item_Weight= st.number_input("Item_Weight")
Item_Fat_Content= st.number_input("Item_Fat_Content")
Item_Visibility=st.number_input("Item_Visibility")
Item_Type  =st.number_input("Item_Type")
Outlet_Identifier =st.number_input("Outlet_Identifier")
Outlet_Establishment_Year=st.number_input("Outlet_Establishment_Year")
Outlet_Size=st.number_input("Outlet_Size")
Outlet_Location_Type=st.number_input("Outlet_Location_Type")
Outlet_Type  =st.number_input("Outlet_Type")


if st.button("Predict"):
   
   
    result = model.predict([[Item_Identifier,Item_Weight,Item_Fat_Content,Item_Visibility,Item_Type,Outlet_Identifier,Outlet_Establishment_Year,Outlet_Size,Outlet_Location_Type,Outlet_Type]])
    st.write("Sales:" , result[0])