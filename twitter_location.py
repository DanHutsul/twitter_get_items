#!/usr/bin/python3.6

from flask import Flask, render_template
import tweepy
import pandas as pd
import folium

app = Flask(__name__)

@app.route('/')
def main():
    # Authenticate to Twitter
    auth = tweepy.OAuthHandler("ZxDwkJ0fHdqxc7Irljy82emIQ", "9NuxQMVXgOdQbo28sqOc25GhXgLr8OTrxCFE9iphwZlirRBDdN")
    auth.set_access_token("1161015575512064000-9bJgvnlgNTzx0IAudrdtT8SvgBXGvZ", "2vIYX8HLBg5uWXLREfgodKWQBT88aHgxTmFaL5JvDIv03")

    # Create API object
    api = tweepy.API(auth)

    name = "realdonaldtrump"
    data = pd.read_csv('worldcities.csv',
                       error_bad_lines=False)
    city = data['city_ascii']
    lt = data['lat']
    ln = data['lng']

    api = tweepy.API(auth)
    friends_location = []
    for user in tweepy.Cursor(api.friends, screen_name=name).items():
      location = user.location
      if location:
        for i in range(len(city)):
          if city[i] in location:
            latitude = lt[i]
            longitude = ln[i]
            friends_location.append((user.screen_name, latitude, longitude))
            break

    map = folium.Map(location=[latitude, longitude],
                      zoom_start=10)

    location_map = folium.FeatureGroup(name="Location")
    for user in friends_location:
      folium.Marker(location=[user[1], user[2]], popup= "@" + user[0] + "\n").add_to(map)

    map.add_child(location_map)
    map.add_child(folium.LayerControl())
    map.save('map.html')
    return render_template('map.html')

if __name__ == '__main__':
  app.run(debug=True)