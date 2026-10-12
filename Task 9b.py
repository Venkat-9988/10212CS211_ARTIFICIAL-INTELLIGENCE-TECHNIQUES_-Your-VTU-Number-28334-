
# Tourism Information Chatbot

tourism = {
    "places": "Visit Ooty and Kodaikanal.",
    "hotels": "Hotels, resorts, and lodges are available.",
    "transport": "Buses, trains, and taxis are available."
}

print("Tourism Information Chatbot")

for i in range(3):
    query = input("Enter your query: ").lower()

    if "place" in query or "tourist" in query:
        print(tourism["places"])
    elif "hotel" in query or "stay" in query:
        print(tourism["hotels"])
    elif "transport" in query or "bus" in query or "train" in query:
        print(tourism["transport"])
    else:
        print("Sorry, information not available.")
