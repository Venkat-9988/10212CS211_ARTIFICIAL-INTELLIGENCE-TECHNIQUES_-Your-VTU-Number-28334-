
# Digital Library Chatbot

documents = {
    "AI": "Artificial Intelligence and Machine Learning",
    "Python": "Python Programming and Applications",
    "NLP": "Natural Language Processing and Chatbots"
}

print("Digital Library Chatbot")

for i in range(3):
    query = input("Enter your research query: ").lower()
    found = False

    for topic, description in documents.items():
        if topic.lower() in query or any(
            word in query for word in description.lower().split()
        ):
            print("Relevant Document:", description)
            found = True
            break

    if not found:
        print("No relevant document found.")
