import streamlit as st
import pandas as pd
import plotly.express as px
data = pd.read_csv("dataset.csv")
data['duration_sec'] = data['duration_ms'] / 1000

data['duration_sec'] = pd.to_numeric(data['duration_ms'], errors='coerce') / 1000

#Function to convert seconds to minutes:seconds
def convert_seconds_to_minutes(seconds):
    if pd.isna(seconds):
        return 'N/A'
    minutes = int(seconds // 60)
    seconds = int(seconds % 60)
    return f"{minutes}:{seconds:02d}"
data['duration_min_sec'] = data['duration_sec'].apply(convert_seconds_to_minutes)
data = data.drop(columns=['duration_sec'])

st.header('Spotify Track Analysis')

for artist in data['artists']:
    print(artist)

artist_counts = data['artists'].value_counts().reset_index()
artist_counts.columns = ['artists', 'count']
top_artists = artist_counts.head(20)

show_top_artists = st.checkbox('Show only Top 20 artists')
if show_top_artists:
    data = data[data['artists'].isin(top_artists['artists'])]
    st.write("Top Artists:", top_artists['artists'].tolist())

fig = px.histogram(
    top_artists,
    x='artists',
    y='count',
    labels={'artists': 'Artist', 'count': 'Frequency of Artists'},
    title='Top Artists'
)

st.plotly_chart(fig)

fig_1 = px.scatter(
    top_artists,
    x='artists',
    y='count',
    labels={'artists': 'Artist', 'count': 'Number of Occurrences'},
    title='Frequency of Artists'
)
st.plotly_chart(fig_1)

data_filtered = data[data['popularity'] !=0]
popular_counts = data_filtered.sort_values(
    by=['popularity', 'track_name', 'duration_min_sec', 'danceability', 'energy', 'key', 'tempo'],
    ascending=False
).head(20)
popular_counts = popular_counts.value_counts(subset=['popularity', 'track_name', 'duration_min_sec', 'danceability', 'energy', 'key', 'tempo']).reset_index(name='count')
top_songs = data_filtered.sort_values(by='popularity', ascending=False).drop_duplicates(subset=['track_name'])

# Select the top 20 rows
top_20_songs = top_songs.head(20)

show_top_20_songs = st.checkbox('Show only Popular Songs')
if show_top_20_songs:
    data = data[data['track_name'].isin(top_20_songs['track_name'])]
    st.write("Popular Songs:", top_20_songs['track_name'].tolist())

# Create the histogram
fig_2 = px.histogram(
    top_20_songs,
    x='track_name',
    y='popularity',
    labels={'track_name': 'Track Name', 'popularity': 'Popularity of Track'},
    title='Popularity of a Track'
)
fig_2.update_layout(xaxis_tickangle=-45)
fig_2.update_yaxes(range=[80, 110])

# Display the plot
st.plotly_chart(fig_2)

fig_3 = px.scatter(
    popular_songs,
    x='track_name',
    y='popularity',
    labels={'track_name': 'Track Name', 'popularity': 'Popularity of Track'},
    title='Popularity of a Track'
)
fig_3.update_layout(xaxis_tickangle=-45)
fig_3.update_yaxes(range=[80, 150])
st.plotly_chart(fig_3)

popularity_by_genre = data.groupby('track_genre')['popularity'].mean().reset_index()
popularity_by_genre.columns = ['track_genre', 'average_popularity']

fig_4 = px.histogram(
    popularity_by_genre,
    x='track_genre',
    y='average_popularity',
    nbins=30,
    labels={'average_popularity': 'Average Popularity'},
    title='Distribution of Average Track Popularity by Genre'
)
fig_4.show()

fig_5 = px.scatter(
    popularity_by_genre,
    x='track_genre',
    y='average_popularity',
    labels={'track_genre': 'Genre', 'average_popularity': 'Average Popularity'},
    title='Average Popularity of Tracks by Genre'
)
fig_5.show()

options = ['Popularity by Genre Distribution', 'Popularity by Genre Scatter', 'Popular Songs Histogram', 'Popular Songs Scatter']
selected_options = st.selectbox('Choose an option:', options)

if selected_options == 'Popularity by Genre Distribution':
    st.plotly_chart(fig_4)
elif selected_options == 'Popularity by Genre Scatter':
    st.plotly_chart(fig_5)
elif selected_options == 'Popular Songs Histogram':
    st.plotly_chart(fig_2)
elif selected_options == 'Popular Songs Scatter':
    st.plotly_chart(fig_3)
    
st.write(f"You selected: {selected_options}") 
