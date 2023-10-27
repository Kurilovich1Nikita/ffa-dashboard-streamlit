# Import libraries
import streamlit as st
import pandas as pd
import openpyxl 

# Page setup with your custom icon
st.set_page_config(page_title="FFA", page_icon="ffa_icon_jrQ_icon.png", layout="wide")

st.title("FFA Search Engine")

# Connect to the Google Sheet
#sheet_id = "1nctiWcQFaB5UlIs6z8d1O6ZgMHFDMAoo3twVxYnBUws"
#sheet_name = "charlas"
#url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
#df = pd.read_csv(url, dtype=str).fillna("")
df = pd.read_excel('SearchengineFFA1.xlsx')

# Show the dataframe (we'll delete this later)
st.write(df)

# # Use a text_input to get the keywords to filter the dataframe
text_search = st.text_input("Search URL by Title, Program Type, Author or Keywords", value="")

# # Filter the dataframe using masks
m1 = df["Author"].str.contains(text_search)
m2 = df["Title"].str.contains(text_search)
m3 = df["ProgramType"].str.contains(text_search)
m4 = df["Keywords"].str.contains(text_search)
df_search = df[m1 | m2 | m3| m4]

# # Show the results, if you have a text_search
if text_search:
    st.write(df_search)

# # Another way to show the filtered results
# # Show the cards
N_cards_per_row = 3
if text_search:
    for n_row, row in df_search.reset_index().iterrows():
        i = n_row%N_cards_per_row
        if i==0:
            st.write("---")
            cols = st.columns(N_cards_per_row, gap="large")
        # draw the card
        with cols[n_row%N_cards_per_row]:
            st.markdown(f"*{row['ProgramType'].strip()}*")
            st.markdown(f"**{row['Author'].strip()}**")
            st.markdown(f"*{row['Title'].strip()}*")
            st.markdown(f"**{row['URL']}**")

