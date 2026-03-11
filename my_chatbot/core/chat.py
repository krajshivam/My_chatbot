from groq import Groq
from config.settings import GROQ_API_KEY, MODEL_NAME, TEMPERATURE, MAX_TOKENS

client = Groq(api_key=GROQ_API_KEY)


def start_chat():
    """Returns a fresh empty conversation history."""
    return []


def send_message(messages: list, user_input: str) -> str:
    """Sends user message to Groq and returns AI reply."""

    # add user message to history
    messages.append({"role": "user", "content": user_input})

    # call Groq API with full history
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS,
    )

    # extract reply
    reply = response.choices[0].message.content

    # add AI reply to history
    messages.append({"role": "assistant", "content": reply})

    return reply
