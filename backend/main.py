from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from schemas import ChatRequest, ChatResponse
from ai_service import chat


app = FastAPI(title="CodeMate AI")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


conversations = {}


@app.get("/")
def root():
    return {
        "message": "CodeMate AI API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/chat", response_model=ChatResponse)
def chat_endpoint(request: ChatRequest):

    if request.conversation_id not in conversations:
        conversations[request.conversation_id] = []

    conversations[request.conversation_id].append({
        "role": "user",
        "content": request.message
    })

    answer = chat(request.message)

    conversations[request.conversation_id].append({
        "role": "assistant",
        "content": answer
    })

    return {
        "conversation_id": request.conversation_id,
        "message": request.message,
        "response": answer
    }