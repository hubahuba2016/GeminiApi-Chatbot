import google.generativeai as genai

# Configure your API key (REPLACE with your actual key!)
genai.configure(api_key="YOUR API KEY HERE")

model = genai.GenerativeModel('gemini-pro')

def automated_conversation():
    try:
        chat = model.start_chat()  # This should now work correctly
        while True:
            user_input = input("You: ")
            if user_input.lower() == "exit":
                print("Conversation ended.")
                break

            try:
                response = chat.send_message(user_input)
                print("AI:", response.text)
            except Exception as e:
                print(f"Error communicating with AI: {e}")  # More specific error message

    except Exception as e:
        print(f"Error starting chat or API issue: {e}") # Handle API key issues, etc.

# Start the automated conversation
automated_conversation()
