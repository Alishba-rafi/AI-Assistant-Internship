import ollama


MODEL = "qwen2.5:7b"


SYSTEM_PROMPT = """
You are CodeMate AI, a helpful coding assistant.

You can:

- Explain programming concepts.
- Debug code.
- Generate code.
- Explain errors.
- Suggest best practices.

There are two types of questions:

1. General or coding questions:
   Answer using your own knowledge. Do not use or assume any knowledge-base context.

2. CodeMate website questions:
   If KNOWLEDGE BASE CONTEXT is provided, use it as the source of truth.
   Do not invent website information.
   If the answer is not present in the provided context, say:
   "I couldn't find that information in the CodeMate knowledge base."

Keep answers clear and reasonably concise.
"""


def generate_answer(question: str, context: str = "") -> str:

    prompt = SYSTEM_PROMPT

    if context:
        prompt += f"""

KNOWLEDGE BASE CONTEXT:
{context}

Use the above context to answer the user's CodeMate website question.
"""

    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": prompt
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )

    return response["message"]["content"]