from groq import Groq
from config.settings import GROQ_API_KEY, MODEL_NAME, TEMPERATURE, MAX_TOKENS

client = Groq(api_key=GROQ_API_KEY)


def start_chat():
    """Returns a fresh empty conversation history."""
    return [
        {
            "role": "system",
            "content": """You are a helpful assistant. 
    Format all your responses as follows:
- Leave space before u start writing your answer.
- Number your points as 1> 2> and so on.
- Leave a blank line before every new point
- Keep answers concise and clear""",
        }
    ]


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
