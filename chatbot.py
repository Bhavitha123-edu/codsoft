def chatbot():
    print("Hello! I'm a simple rule-based chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ").lower().strip()
        
        # Exit condition
        if user_input == 'quit':
            print("Chatbot: Goodbye!")
            break
            
        # Greeting responses
        elif 'hello' in user_input or 'hi' in user_input:
            print("Chatbot: Hi there! How can I help you today?")
            
        # Help request
        elif 'help' in user_input:
            print("Chatbot: I'm here to assist! You can ask about the weather, time, or just say hi!")
            
        # Weather query
        elif 'weather' in user_input:
            print("Chatbot: I can't check real-time weather, but it's always sunny in the digital world!")
            
        # Time query
        elif 'time' in user_input:
            print("Chatbot: I don't have a clock, but it's time to have a great conversation!")
            
        # Thank you response
        elif 'thank' in user_input:
            print("Chatbot: You're welcome!")
            
        # Default response for unrecognized input
        else:
            print("Chatbot: Sorry, I didn't understand that. Try saying 'hello', 'help', 'weather', or 'time'.")

if __name__ == "__main__":
    chatbot()
