import folium
import openrouteservice
import json
import webbrowser





def readfile():
    info = []
    with open("locations.json") as f:
        data = json.load(f)

    for feature in data['features']:
        row = []
        row.append(feature['City'])
        row.append(feature['geometry']['coordinates'])
        info.append(row)
    return info


def LatLon(target,info):
    for city in info:
        if city[0] == target:
            lat, lon = city[1]
            return lat, lon


def func(goals,start):
    info = readfile()


    Slat, Slon = LatLon(start,info)

    client = openrouteservice.Client(
        key='5b3ce3597851110001cf624819b9f2c0b69e4727b1695d0849e408f6')  # Specify your personal API key
    m = folium.Map(location=[31.182882, 34.811615], zoom_start=8)
    html = f'HI there. You are In Palestine. <br> You are travelling from : {start}:! <br>'

    iframe = folium.IFrame(html,width=200,height=100)

    popup = folium.Popup(iframe,max_width=200)

    marker = folium.Marker([Slon, Slat], popup=popup).add_to(m)

    for goal in goals:
        Glat, Glon = LatLon(goal,info)
        folium.Marker(
            [Glon, Glat]
        ).add_to(m)
        coordinates = [[Slat, Slon], [Glat, Glon]]
        route = client.directions(coordinates=coordinates, profile='driving-car', format='geojson')

        folium.GeoJson(route, name='route').add_to(m)
    m.save("route.html")
    url = 'route.html'
    webbrowser.open(url, new=2)

# url = 'route.html'
# webbrowser.open(url, new=2)
# routes = client.directions(coordinates)
# print(routes)


# directions

# add geojson to map

# display map
