team={
    "player1":{
        "name": "masha",
        "age" : 23,
        "position" : "middel",
        "number": 1,
        "grades":{
            "python" : 20,
            "grade2" : 20,
            "grade3": 20

        }

    },
        "player2":{
        "name": "fat",
        "age" : 24,
        "position" : "middel",
        "number": 6,
        "grades":{
            "python" : 18,
            "grade2" : 20,
            "grade3": 15

        }

    },
        "player3":{
        "name": "meli",
        "age" : 21,
        "position" : "oh",
        "number": 10,
        "grades":{
            "python" : 15,
            "grade2" : 18,
            "grade3": 20

        }

    },
}
print(team["player1"]["name"])
print(team["player2"]["age"])
print(team["player3"]["grades"]["python"])
team.update({
    "player4":{
        "name": "sool",
        "age" : 27,
        "position" : "oh",
        "number": 6,
        "grades":{
            "python" : 10,
            "grade2" : 14,
            "grade3": 20
         }
    }
})
team ["player1"]["height"]=173
team ["player2"]["grades"]["database"]=10
team["player1"]["number"]=11
team["player3"]["age"]=25
team["player2"].update({
    "position": "set",
    "height": 182
})

print(team.items())
team["player4"].pop("age")
print(team.items())
team["player2"]["grades"].pop("grade2")
print(team.items())
for key,value in team.items():
    print(key,value["name"])
for value in team.values():
    print(value["name"])
for key,value in team.items():
    print(key,value)
for key,value in team.items():
    print(value["name"])
    for grades in value["grades"].items():
        print(grades)
for key,value in team.items():
    print(key,value["name"])
    for grades in value["grades"].values():
        print(grades)
if "player1" in team:
    print("yes")
print(team["player1"].get("number"))
team["player1"].setdefault("country","iran")
for key,value in team["player1"].items():
    print(key,value)
new_dict=team.copy()
print(len(team))