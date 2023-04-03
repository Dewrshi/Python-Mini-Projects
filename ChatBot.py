from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chatbot
chatbot = ChatBot("My Chatbot")

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on the English corpus
trainer.train("chatterbot.corpus.english")

# Start the chatbot
print("Type 'quit' to exit")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        break
    response = chatbot.get_response(user_input)
    print("Chatbot:", response)
