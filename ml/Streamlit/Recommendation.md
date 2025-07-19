## Recommendation

```python

import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    return pd.read_csv('movies.csv')

st.title("Simple Movie Recommendation")

df = load_data()

search = st.text_input("Search for a movie title:")

if search:
    results = df[df['title'].str.contains(search, case=False, na=False)]
    if results.empty:
        st.write("No movies found.")
    else:
        st.write("Search results:")
        for i, row in results.iterrows():
            st.write(f"- {row['title']} (Rating: {row['rating']:.2f})")
        
        selected = st.selectbox("Choose a movie for recommendations:", results['title'])

        recs = df[(df['cluster'] == df[df['title'] == selected]['cluster'].values[0]) & (df['title'] != selected)]

        st.write(f"Movies similar to **{selected}**:")
        if recs.empty:
            st.write("No recommendations found.")
        else:
            for i, row in recs.iterrows():
                st.write(f"- {row['title']} (Rating: {row['rating']:.2f})")
else:
    st.write("Type a movie title above to start searching.")


```
