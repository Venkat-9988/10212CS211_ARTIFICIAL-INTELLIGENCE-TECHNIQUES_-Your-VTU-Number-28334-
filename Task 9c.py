
# Banking Assistance Chatbot

responses = {
    "balance": "Check your balance using mobile banking.",
    "transfer": "Transfer money using UPI, NEFT, or IMPS.",
    "password": "Reset your password through the official bank app."
}

print("Banking Assistance Chatbot")

for i in range(3):
    query = input("Enter your banking query: ").lower()

    if "balance" in query:
        print(responses["balance"])
    elif "transfer" in query or "upi" in query:
        print(responses["transfer"])
    elif "password" in query or "reset" in query:
        print(responses["password"])
    else:
        print("Please contact bank customer support.")
