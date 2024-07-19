import streamlit as st
import pandas as pd
import plotly.express as px
data = pd.read_csv("dataset.csv")
st.header('SDT Project')
fig = px.histogram(
    top_artists,
    x='artists',
    y='count',
    labels={'artists': 'Artist', 'count': 'Frequency of Artists'},
    title='Top Artists'
)
fig.show()
fig = px.scatter(
    top_artists,
    x='artists',
    y='count',
    labels={'artists': 'Artist', 'count': 'Number of Occurrences'},
    title='Frequency of Artists'
)
fig.show()
# Sort and take only the top 20 songs
popular_songs = popular_counts.head(20)

# Create the histogram
fig = px.histogram(
    popular_songs,
    x='track_name',
    y='count',
    labels={'track_name': 'Track Name', 'count': 'Popularity of Track'},
    title='Popularity of a Track'
)
fig.update_layout(xaxis_tickangle=-45)
fig.update_yaxes(range=[0, 50])
# Display the plot
fig.show()
fig = px.scatter(
    popular_songs,
    x='track_name',
    y='count',
    labels={'track_name': 'Track Name', 'count': 'Popularity of Track'},
    title='Popularity of a Track'
)
fig.update_layout(xaxis_tickangle=-45)
fig.update_yaxes(range=[0, 30])
fig.show()
