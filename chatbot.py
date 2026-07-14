"""
Project 1: Rule-Based AI Chatbot
DecodeLabs - AI Internship (Batch 2026)

A simple rule-based chatbot that responds to predefined user inputs
using dictionary lookups (hash maps) instead of long if-elif chains.

Architecture (IPO Model):
    INPUT   -> Sanitization & Normalization
    PROCESS -> Intent Matching via dictionary .get()
    OUTPUT  -> Response Generation (with fallback)
"""

# ----------------------------
# Knowledge Base (5+ intents)
# ----------------------------
responses = {
    "hello": "Hi there! How can I help you today?",
    "hi": "Hello! What can I do for you?",
    "how are you": "I'm just a program, but I'm running smoothly! How about you?",
    "what is your name": "I'm ChatBot, your friendly rule-based assistant.",
    "what can you do": "I can chat with you using predefined rules. Try asking me about myself!",
    "help": "You can say things like 'hello', 'how are you', or 'what is your name'.",
    "thank you": "You're welcome!",
    "thanks": "Anytime!",
}

# Exit commands that break the loop
EXIT_COMMANDS = {"exit", "quit", "bye", "goodbye"}

# Fallback response for unrecognized input
FALLBACK_RESPONSE = "I do not understand. Type 'help' to see what I can respond to."


def sanitize_input(raw_input: str) -> str:
    """Normalize user input: lowercase + strip whitespace."""
    return raw_input.lower().strip()


def get_response(user_input: str) -> str:
    """Look up the cleaned input in the knowledge base with a fallback."""
    return responses.get(user_input, FALLBACK_RESPONSE)


def main():
    print("ChatBot: Hello! I'm a rule-based chatbot. Type 'exit' to quit.")

    while True:
        raw_input_text = input("You: ")
        clean_input = sanitize_input(raw_input_text)

        if clean_input in EXIT_COMMANDS:
            print("ChatBot: Goodbye! Have a great day.")
            break

        reply = get_response(clean_input)
        print(f"ChatBot: {reply}")


if __name__ == "__main__":
    main()
