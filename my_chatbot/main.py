from core.chat import start_chat, send_message


def main():
    print("Chatbot ready. Type 'quit' to exit.\n")

    messages = start_chat()

    while True:
        user_input = input("You: ").strip()

        if not user_input:  # ignore empty input
            continue

        if user_input.lower() == "quit":
            print("Good Bye!")
            break

        reply = send_message(messages, user_input)
        print(f"Bot: {reply}\n")


if __name__ == "__main__":
    main()
