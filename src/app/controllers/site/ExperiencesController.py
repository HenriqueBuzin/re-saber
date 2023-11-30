from googleapiclient.discovery import build
from flask import render_template
import os

def get():

   YOUTUBE_API_KEY = os.environ["YOUTUBE_API_KEY"]
   YOUTUBE_PLAYLIST_ID = 'PLgnq4U0mFSEIdDyo-ENrtcxTWrUEQvErm'

   youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

   cache = {}

   totalPlaylistItems = 0

   if 'total_playlist_items' not in cache:
      # Make API request to retrieve the total playlist items
      nextPageToken = None

      while True:
         request = youtube.playlistItems().list(
               part="snippet",
               maxResults=500,
               playlistId=YOUTUBE_PLAYLIST_ID,
               pageToken=nextPageToken
         )

         response = request.execute()
         playlistItems = response.get('items', [])
         totalPlaylistItems += len(playlistItems)

         nextPageToken = response.get('nextPageToken')

         if not nextPageToken:
               break

      cache['total_playlist_items'] = totalPlaylistItems

   items = []

   for i in range(0, totalPlaylistItems, 500):
      request = youtube.playlistItems().list(
         part="snippet",
         maxResults=500,
         playlistId=YOUTUBE_PLAYLIST_ID,
         pageToken=None
      )

      response = request.execute()
      playlistItems = response.get('items', [])
      items += playlistItems

   # Filter items to extract video thumbnail URL, title, and video ID
   filtered_items = []
   for item in items:
      thumbnail_url = item['snippet']['thumbnails']['high']['url']
      title = item['snippet']['title']
      video_id = item['snippet']['resourceId']['videoId']

      filtered_item = {
         'thumbnail_url': thumbnail_url,
         'title': title,
         'video_id': video_id
      }

      filtered_items.append(filtered_item)

   return render_template('site/experiences.html', items=filtered_items)
