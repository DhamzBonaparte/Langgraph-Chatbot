# 🧠 Stateful RAG Agent with LangGraph, LangChain & SQLite

A conversational AI assistant that remembers information within a conversation thread while maintaining strict memory isolation across different sessions.

Unlike traditional chatbots that lose context between conversations, this project uses **LangGraph for state management**, **LangChain for orchestration**, and **SQLite for persistent storage** to create a truly stateful AI experience.

## ✨ Features

### 🔹 Thread-Based Memory
- Remembers user information within the active conversation.
- Maintains context across multiple interactions.
- Preserves conversational continuity.

### 🔹 Persistent SQLite Storage
- Stores memory beyond runtime.
- Survives application restarts and page refreshes.
- Provides lightweight and reliable local storage.

### 🔹 Context Isolation
- Each thread has its own dedicated memory.
- Information does not leak between conversations.
- Enables safe multi-thread conversational experiences.

### 🔹 Retrieval-Augmented Generation (RAG)
- Retrieves relevant context before generating responses.
- Improves answer quality and consistency.
- Creates more personalized interactions.

### 🔹 Interactive Streamlit Interface
- Simple and intuitive chat interface.
- Easily switch between conversation threads.
- Real-time interaction with persistent memory.

---

## 🏗️ Tech Stack

- **LangChain** – LLM orchestration and prompt management
- **LangGraph** – Stateful workflow and memory management
- **SQLite** – Persistent conversation storage
- **Streamlit** – Interactive web application
- **OpenAI / Compatible LLMs** – Natural language generation

---

## 🚀 How It Works

1. A user starts a conversation in a thread.
2. User information and conversation history are stored in SQLite.
3. LangGraph manages the state of each conversation thread.
4. Relevant context is retrieved before every response.
5. The LLM generates responses using both current input and stored memory.
6. Switching threads creates isolated conversational contexts.

---

## 🔍 Example

### Thread 1

**User:**
```text
My name is Sulav.
```

**Assistant:**
```text
Nice to meet you, Sulav.
```

Later in the same thread:

**User:**
```text
What is my name?
```

**Assistant:**
```text
Your name is Sulav.
```

### Thread 2

**User:**
```text
What is my name?
```

**Assistant:**
```text
I don't know your name.
```

This demonstrates that memory is preserved within a thread while remaining isolated from other conversations.

---

## 🎯 Why This Project?

Most AI assistants are stateless by default, meaning they lose context between conversations.

This project explores how to build AI systems that:

- Remember important information
- Maintain context over time
- Support long-running conversations
- Persist memory across sessions
- Isolate memory between users or threads
- Deliver a more human-like conversational experience

---

## 📂 Use Cases

- Personal AI Assistants
- Customer Support Chatbots
- Internal Knowledge Assistants
- Multi-Session Chat Applications
- Enterprise AI Workflows
- Long-Term Conversational Agents
- AI-Powered Productivity Tools

---

## 🎥 Demo Scenario

✅ Thread A

```text
My name is Sulav.
```

Agent remembers the information.

✅ Thread B

```text
What is my name?
```

Agent responds:

```text
I don't know your name.
```

✅ Back to Thread A

```text
What is my name?
```

Agent responds:

```text
Your name is Sulav.
```

Memory works exactly as intended while remaining isolated to each thread.

---

## 🔮 Future Improvements

- Vector Database Integration (ChromaDB, Pinecone, FAISS)
- Semantic Memory Retrieval
- Long-Term Memory Compression
- User Authentication
- Multi-User Support
- Hybrid SQLite + Vector Store Architecture
- Conversation Analytics Dashboard
- Agent Tool Calling and Automation

---

## 🤝 Contributing

Contributions, suggestions, and feedback are welcome.

Feel free to open an issue or submit a pull request to improve the project.

---

## 📜 License

This project is open-source and available under the MIT License.

---

### ⭐ If you found this project useful, consider giving it a star!

Built with ❤️ using **LangChain**, **LangGraph**, **Streamlit**, and **SQLite**.