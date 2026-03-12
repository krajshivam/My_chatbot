from groq import Groq
from config.settings import GROQ_API_KEY, MODEL_NAME, TEMPERATURE, MAX_TOKENS
from tools.retriever import retrieve

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
- Keep answers concise and clear
-You have access to documents the user has uploaded.
-Answer ONLY using the context provided below.
-Do not use any outside knowledge.
-If the exact answer is not in the context, say 'I could not find this in the document.'
-Never guess or approximate numbers — use exact figures from the context only.""",
        }
    ]


def send_message(messages: list, user_input: str) -> str:
    """Sends user message to Groq and returns AI reply."""

    context = retrieve(user_input)
    ## inject context into user message
    if context:
        augmented_input = f"""Context from document:
        {context}

User question: {user_input}"""
    else:
        augmented_input = user_input  # no document loaded, chat normally

    # add AUGMENTED message to history
    messages.append({"role": "user", "content": augmented_input})

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
