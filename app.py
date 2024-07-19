import streamlit as st
import pandas as pd
import plotly.express as px
data = pd.read_csv("dataset.csv")
st.header('SDT Project')

for artist in data['artists']:
    print(artist)

artist_counts = data['artists'].value_counts().reset_index()
artist_counts.columns = ['artists', 'count']
top_artists = artist_counts.head(20)

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

data_filtered = data[data['popularity'] !=0]
popular_counts = data_filtered[['popularity', 'track_name']].value_counts().reset_index()
popular_counts.columns = ['popularity','track_name', 'count']
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
