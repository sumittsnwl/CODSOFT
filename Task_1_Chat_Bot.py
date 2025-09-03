def simple_chatbot():
    print("Hello! I'm a simple chatbot. Type 'quit' or 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower().strip()     
                      
        # Greetings
        if any(word in user_input for word in ['hello', 'hi', 'hey', 'hola' , 'hy']):
            print("Chatbot: Hello there! How can I help you today?")
        
        # How are you
        elif any(word in user_input for word in ['how are you', "how's it going", "how do you do"]):
            print("Chatbot: I'm just a program, but I'm functioning well! How about you?")
        
        # Name questions
        elif any(word in user_input for word in ['your name', 'who are you', 'identify yourself']):
            print("Chatbot: I'm a simple rule-based chatbot created for a CodSoft internship.")
        
        # Time questions
        elif any(word in user_input for word in ['time', 'what time', 'current time']):
            from datetime import datetime
            current_time = datetime.now().strftime("%H:%M:%S")
            print(f"Chatbot: The current time is {current_time}.")
        
        # Date questions
        elif any(word in user_input for word in ['date', 'today', 'what date']):
            from datetime import datetime
            current_date = datetime.now().strftime("%Y-%m-%d")
            print(f"Chatbot: Today's date is {current_date}.")
        
        # Thanks
        elif any(word in user_input for word in ['thank', 'thanks', 'appreciate']):
            print("Chatbot: You're welcome! Is there anything else I can help with?")
        
        # Help
        elif any(word in user_input for word in ['help', 'what can you do']):
            print("Chatbot: I can respond to greetings, tell you the time and date, and have simple conversations. Try asking me about myself or the time!")
        
        # Exit
        elif any(word in user_input for word in ['bye', 'quit', 'exit']):
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        # Default response
        else:
            print("Chatbot: I'm not sure how to respond to that. I'm a simple chatbot with limited capabilities.")

# Run the chatbot
if __name__ == "__main__":
    simple_chatbot()