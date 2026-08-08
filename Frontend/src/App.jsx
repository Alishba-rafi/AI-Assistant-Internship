
import { useState } from "react";
import "./App.css";

function App() {
  const [chatOpen, setChatOpen] = useState(false);
  const [message, setMessage] = useState("");
  const [loading, setLoading] = useState(false);

  const [messages, setMessages] = useState([
    {
      text: "Hi! 👋 I'm CodeMate AI. Ask me anything about programming, debugging, or coding concepts.",
      sender: "bot",
    },
  ]);

  const openChat = () => {
    setChatOpen(true);
  };

  const toggleChat = () => {
    setChatOpen((previous) => !previous);
  };

  const sendMessage = async () => {
    const trimmedMessage = message.trim();

    if (!trimmedMessage || loading) {
      return;
    }

    // Show user message immediately
    setMessages((previous) => [
      ...previous,
      {
        text: trimmedMessage,
        sender: "user",
      },
    ]);

    setMessage("");
    setLoading(true);

    try {
      const response = await fetch(
        "http://127.0.0.1:8000/chat",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            conversation_id: "codemate-session",
            message: trimmedMessage,
          }),
        }
      );

      if (!response.ok) {
        throw new Error(
          `Server returned ${response.status}`
        );
      }

      const data = await response.json();

      // Show AI response
      setMessages((previous) => [
        ...previous,
        {
          text: data.response,
          sender: "bot",
        },
      ]);

    } catch (error) {
      console.log("Chat error:", error);

      setMessages((previous) => [
        ...previous,
        {
          text: "Sorry, I couldn't connect to CodeMate AI.",
          sender: "bot",
        },
      ]);

    } finally {
      setLoading(false);
    }
  };

  const handleKeyDown = (event) => {
    if (event.key === "Enter") {
      sendMessage();
    }
  };

  return (
    <div>

      {/* ================= NAVBAR ================= */}

      <header className="navbar">
        <div className="logo">
          CodeMate<span>AI</span>
        </div>

        <nav>
          <a href="#home">Home</a>
          <a href="#features">Features</a>
          <a href="#about">About</a>
        </nav>
      </header>


      {/* ================= HERO ================= */}

      <section id="home" className="hero">
        <div className="hero-content">

          <p className="tagline">
            YOUR AI CODING ASSISTANT
          </p>

          <h1>
            Code Smarter.
            <br />
            Learn Faster.
          </h1>

          <p className="hero-description">
            CodeMate AI helps you understand programming concepts,
            debug errors, explain code, and improve your coding skills.
          </p>

          <button
            className="hero-button"
            onClick={openChat}
          >
            Ask CodeMate
          </button>

        </div>
      </section>


      {/* ================= FEATURES ================= */}

      <section
        id="features"
        className="features-section"
      >

        <div className="section-heading">

          <p>WHAT CAN CODEMATE DO?</p>

          <h2>
            Your personal coding companion
          </h2>

        </div>


        <div className="features">

          <div className="feature-card">
            <div className="feature-icon">💡</div>

            <h3>Learn Concepts</h3>

            <p>
              Understand programming concepts with
              simple and clear explanations.
            </p>
          </div>


          <div className="feature-card">
            <div className="feature-icon">🐛</div>

            <h3>Debug Code</h3>

            <p>
              Get help understanding errors and
              finding problems in your code.
            </p>
          </div>


          <div className="feature-card">
            <div className="feature-icon">💻</div>

            <h3>Understand Code</h3>

            <p>
              Ask CodeMate to explain difficult
              code line by line.
            </p>
          </div>


          <div className="feature-card">
            <div className="feature-icon">🚀</div>

            <h3>Improve Skills</h3>

            <p>
              Practice programming and learn
              better development techniques.
            </p>
          </div>

        </div>

      </section>


      {/* ================= ABOUT ================= */}

      <section
        id="about"
        className="about-section"
      >

        <div className="about-content">

          <p>ABOUT CODEMATE AI</p>

          <h2>
            Learn programming with an AI assistant.
          </h2>

          <p>
            CodeMate AI is designed to help students and
            developers understand programming concepts,
            troubleshoot errors, and learn coding technologies.
          </p>

        </div>

      </section>


      {/* ================= FLOATING CHAT BUTTON ================= */}

      <button
        className="chatbot-button"
        onClick={toggleChat}
        aria-label="Open CodeMate AI"
      >
        🤖
      </button>


      {/* ================= CHAT WINDOW ================= */}

      {chatOpen && (
        <div className="chatbot-window">

          <div className="chat-header">

            <div>
              <h3>CodeMate AI</h3>
              <span>● Online</span>
            </div>

            <button
              className="close-button"
              onClick={toggleChat}
              aria-label="Close chatbot"
            >
              ×
            </button>

          </div>


          <div className="chat-messages">

            {messages.map((chatMessage, index) => (
              <div
                key={index}
                className={
                  chatMessage.sender === "user"
                    ? "user-message"
                    : "bot-message"
                }
              >
                {chatMessage.text}
              </div>
            ))}

            {loading && (
              <div className="bot-message">
                CodeMate is thinking...
              </div>
            )}

          </div>


          <div className="chat-input-area">

            <input
              type="text"
              value={message}
              onChange={(event) =>
                setMessage(event.target.value)
              }
              onKeyDown={handleKeyDown}
              placeholder="Ask a coding question..."
              autoComplete="off"
              disabled={loading}
            />

            <button
              onClick={sendMessage}
              disabled={loading}
              aria-label="Send message"
            >
              {loading ? "..." : "➤"}
            </button>

          </div>

        </div>
      )}

    </div>
  );
}

export default App;

