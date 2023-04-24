import requests
import dirtyjson
import arrow
print("Welcome to the H4ALL Games script\n\n")
print("Where do I get the League ID oder Team ID or Club ID From?\nVisit www.handball4all.de and navigate via the links on the page to the site that shows teams Games.\nExample:\n* Timetable for Team: https://www.handball4all.de/home/portal/bhv#/league?ogId=35&lId=67731&tId=720111\n\nFrom the URL you can see the corresponding ID:\n* tId = Team ID (e.g. 720111)")
print("\nThis script will create a .ics file with all the games of a team\n================================================")

teamID = input("Team ID: ")
url = "https://m.h4a.mobi/php/spo-proxy_public.php?cmd=data&lvTypeNext=team&lvIDNext="+teamID
response = requests.get(url)
json_data = dirtyjson.loads(response.content)

if json_data[0]["lvTypeLabelStr"]== "/ [error]":
    print("Error: Wrong TeamID")
    exit()

games = []
for item in json_data[0]["dataList"]:
    game = {}
    game["summary"] = f"{item['gHomeTeam']} vs. {item['gGuestTeam']}"
    game["location"] = f"{item['gGymnasiumName']}, {item['gGymnasiumStreet']}, {item['gGymnasiumPostal']} {item['gGymnasiumTown']}"
    game["description"] = item["gComment"]
    dt_str = f"{item['gDate']} {item['gTime']}"
    dt_format = "DD.MM.YY HH:mm"
    game["start_time"] = arrow.get(dt_str, dt_format)
    games.append(game)

from ics import Calendar, Event

calendar = Calendar()

for game in games:
    event = Event()
    event.name = game["summary"]
    event.location = game["location"]
    event.description = game["description"]
    event.begin = game["start_time"]
    calendar.events.add(event)

with open(teamID + " games.ics", "w") as f:
    f.write(calendar.serialize())

print("Done Your file is ready at: " + teamID + " games.ics")
