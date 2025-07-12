def get_bot_reply(user_input):
    user_input = user_input.lower().strip()

    if user_input in ["hello", "hi", "hey"]:
        return "Hi there!"
    elif user_input in ["how are you", "how are you doing"]:
        return "I'm fine, thanks! How can I help you?"
    elif user_input in ["bye", "goodbye", "see you"]:
        return "Goodbye! Have a great day!"
    elif user_input in ["what's your name", "who are you"]:
        return "I'm a simple chatbot made with Python."
    else:
        return "Sorry, I didn't understand that."

def run_chatbot():
    print("🤖 Chatbot: Hello! Type something to chat. Type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        reply = get_bot_reply(user_input)
        print("Chatbot:", reply)

        if user_input.lower().strip() in ["bye", "goodbye", "see you"]:
            break

run_chatbot()