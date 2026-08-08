from rag.generate_answer import generate_answer
from rag.retriever import retrieve_chunks


WEBSITE_KEYWORDS = [
    "codemate",
    "code mate",
    "this website",
    "this platform",
    "this app",
    "this tool",
    "your platform",
    "your website",
    "who are you",
    "what is codemate",
    "what can you do",
    "what do you offer",
    "features",
    "how does this work",
    "how do you work",
    "code smarter",
    "learn faster",
    "tagline",
    "about codemate",
    "who made you",
    "coding assistant" 
]


def is_website_question(question: str) -> bool:

    question_lower = question.lower()

    return any(
        keyword in question_lower
        for keyword in WEBSITE_KEYWORDS
    )


def chat(question: str):

    # --------------------------------
    # WEBSITE QUESTION
    # --------------------------------

    if is_website_question(question):

        chunks = retrieve_chunks(
            query=question,
            top_k=5
        )

        context = "\n\n".join(
            chunk.content
            for chunk in chunks
        )

        return generate_answer(
            question=question,
            context=context
        )

    # --------------------------------
    # CODING / GENERAL QUESTION
    # --------------------------------

    return generate_answer(
        question=question
    )