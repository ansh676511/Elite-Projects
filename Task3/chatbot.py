# Simple chatbot program

# Predefined responses
responses = {
    "hi": "Hello! How can I help you?",
    "hello": "Hi there! What can I do for you?",
    "how are you": "I'm just a bot, but I'm doing fine. How about you?",
    "what is your name": "I am a simple chatbot created using Python.",
    "bye": "Goodbye! Have a nice day!",
    "help": "You can ask me basic questions like greetings or about me.",
    "what is the time": "I don't know the exact time, but it's chatbot time! 😄",
    "what is the weather": "It's always sunny in my world! ☀️",
    "tell me a joke": "Why did the computer go to the doctor? Because it had a virus! 😂"
}

# Function to get a response
def get_response(user_input):
    user_input = user_input.lower()
    if user_input in responses:
        return responses[user_input]
    else:
        return "Sorry, I didn't understand that. Try asking something else!"

# Chat loop
print("Chatbot is running! Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Bot: Goodbye! Have a nice day!")
        break
    response = get_response(user_input)
    print("Bot:", response)

