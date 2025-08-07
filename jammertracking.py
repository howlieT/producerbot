teamA = input("Enter Team A Name or Colour: ")
teamB = input("Enter Team B Name or Colour: ")
print(f"Teams set: {teamA} vs {teamB}")
print("Welcome to the Jammer Tracking System!")
print("Please enter the jammer's information to start tracking.")
jammerA = input(f"Who's Jamming for {teamA}? ")
print(f"{jammerA} is jamming, are they lead?")
isLead = input("y/n: ").lower().strip() == 'y'
if isLead:
    print(f"{jammerA} is the lead jammer!")
    jammerB = input(f"Who's jamming for {teamB}? ")
    print(f"{jammerB} is jamming for team B, they are not the lead jammer."   )
else:
    print(f"{jammerA} is not the lead jammer.")
    jammerB = input(f"Who's jamming for {teamB}? ")
    print(f"{jammerB} is jamming , are they lead?")
    isLead = input("y/n: ").lower().strip() == 'y'
    if isLead:
        print(f"{jammerB} is the lead jammer!")
    else:
        print("Looks like there's no lead jammer for this jam.")
print("Jammer tracking initialized.")
print("You can now track the jammer's points and penalties.")
print("Remember to update the jammer's status as the game progresses.")

