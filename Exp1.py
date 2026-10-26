
def reflex_agent(location, status):
    if status == "Dirty":
        return "Suck"
    elif location == "A":
        return "Move Right"
    else:
        return "Move Left"


def vacuum_world():
    rooms = {"A": "Dirty", "B": "Dirty"}
    location = "A"

    while True:
        status = rooms[location]
        action = reflex_agent(location, status)

        print("Location:", location)
        print("Status:", status)
        print("Action:", action)

        if action == "Suck":
            rooms[location] = "Clean"
        elif action == "Move Right":
            location = "B"
        else:
            location = "A"

        if rooms["A"] == "Clean" and rooms["B"] == "Clean":
            print("Both rooms are clean!")
            break


vacuum_world()
