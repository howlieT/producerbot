jammerNumber = input("Who's Jamming? ")
print(f"{jammerNumber} is jamming, are they lead?")
isLead = input("y/n: ").lower().strip() == 'y'
if isLead:
    print(f"{jammerNumber} is the lead jammer!")
else:
    print(f"{jammerNumber} is not the lead jammer.")
print("Jammer tracking initialized.")
print("You can now track the jammer's points and penalties.")
print("Remember to update the jammer's status as the game progresses.")