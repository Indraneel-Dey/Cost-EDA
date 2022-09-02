import pandas as pd
import streamlit as st
from streamlit_pandas_profiling import st_profile_report
from pandas_profiling import ProfileReport

df = pd.read_csv('Cost Pivot.csv')
df.columns = ['Month', 'Ashirbad Wheat Flour Total Cost', 'Fair and Lovely Face Cream Total Cost', 
              'Fortune Cooking Oil Total Cost', 'Maggi Sauce Total Cost', 'Potatoes Total Cost', 'Sriram Papad Total Cost', 
              'Ashirbad Wheat Flour Marginal Cost', 'Fair and Lovely Face Cream Marginal Cost', 'Fortune Cooking Oil Marginal Cost', 
              'Maggi Sauce Marginal Cost', 'Potatoes Marginal Cost', 'Sriram Papad Marginal Cost']
profile = ProfileReport(df)

st.write('Indraneel Dey')
st.write('21f3002696')
st.write('Indian Institute of Technology, Madras')
st.title('Profile Report of Total and Marginal Costs')
st.write(df)
st_profile_report(profile)
