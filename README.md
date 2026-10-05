<div align="center">

# ✈️ TripMate AI — Multi-Agent Travel Planner

### *An Autonomous Travel Planning System with LangGraph, MCP, Supervisor Agent, Guardrails & Human-in-the-Loop (HITL)*

[![FastAPI](https://img.shields.io/badge/FastAPI-0.136+-009688.svg?style=flat&logo=FastAPI&logoColor=white)](https://fastapi.tiangolo.com)
[![LangGraph](https://img.shields.io/badge/LangGraph-1.2.2-FF4F00.svg?style=flat&logo=LangGraph&logoColor=white)](https://langchain-ai.github.io/langgraph/)
[![Model Context Protocol](https://img.shields.io/badge/MCP-Standard-0A84FF.svg?style=flat)](https://modelcontextprotocol.io)
[![Groq](https://img.shields.io/badge/Groq-Llama%203.3%20%2F%20GPT--OSS-F55036.svg?style=flat)](https://groq.com)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Checkpointer-336791.svg?style=flat&logo=PostgreSQL&logoColor=white)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED.svg?style=flat&logo=Docker&logoColor=white)](https://www.docker.com/)

</div>

---

## 📖 Overview

**TripMate AI** is an advanced, production-ready multi-agent travel planning platform. Powered by **LangGraph**, **Groq LLMs**, and the **Model Context Protocol (MCP)**, TripMate AI breaks down complex travel planning requests into coordinated sub-tasks delegated to specialized AI agents.

The system features **Input Guardrails**, dynamic **Supervisor Orchestration**, **PostgreSQL State Persistence**, and a **Human-in-the-Loop (HITL)** approval gate where travelers can review, revise, and refine draft itineraries before the final plan is generated.

---

## ✨ Key Features

- 🧠 **Supervisor Agent Orchestration**: Parses user queries, extracts travel constraints (origin, destination, dates, budget), and coordinates specialist sub-agents.
- 🛡️ **Input Guardrails**: Validates and protects the pipeline from off-topic, malicious, or unsafe prompts before agent execution.
- 👤 **Human-in-the-Loop (HITL)**: Utilizes LangGraph `interrupt()` and state checkpointing to pause execution, allowing users to approve drafts or request targeted revisions.
- 🔌 **Model Context Protocol (MCP)**:
  - **AviationStack MCP**: Live flight schedules, airline routes, and pricing estimates.
  - **Tavily MCP**: Web intelligence for top-rated hotels, neighborhood guides, and attractions.
  - **Custom Weather MCP Server**: Live climate forecasting and multi-day weather predictions via Open-Meteo.
- 💰 **Budget & Cost Analyzer**: Formulates detailed breakdowns for flights, stays, activities, dining, and contingency buffers.
- 🗓️ **Day-by-Day Master Itinerary**: Produces comprehensive morning, afternoon, and evening schedules with transport advice.
- 💾 **PostgreSQL State Persistence**: Resumes paused multi-turn agent threads reliably via `PostgresSaver`.
- 📄 **One-Click PDF Export & Copy**: Generates formatted, printer-ready PDF travel documents in the browser.
- 🐳 **Docker & Container Ready**: Includes pre-configured `Dockerfile` and `.dockerignore` for one-command deployment.

---

## 🏗️ Multi-Agent Architecture

```mermaid
flowchart TD
    User([👤 User Request]) --> Supervisor[🧠 Supervisor Agent & Guardrails]

    Supervisor -- Guardrail Blocked --> Blocked[🚫 Guardrail Blocked Node]
    Blocked --> EndNode([🏁 End / Response])

    Supervisor -- Guardrail Passed --> FlightAgent[✈️ Flight Agent / MCP]
    FlightAgent --> HotelAgent[🏨 Hotel Agent / MCP]
    HotelAgent --> WeatherAgent[🌦️ Weather Agent / MCP]
    WeatherAgent --> BudgetAgent[💰 Budget Agent]
    BudgetAgent --> ItineraryAgent[🗓️ Itinerary Agent]

    ItineraryAgent --> DraftPlan[📝 Synthesized Draft Itinerary]
    DraftPlan --> HITL{👤 Human-in-the-Loop Review}

    HITL -- "Revise with Feedback" --> ResumeRevision[✏️ State Resume with Feedback]
    ResumeRevision --> FinalAgent[✨ Final Synthesis Agent]

    HITL -- "Approve Draft" --> FinalAgent
    FinalAgent --> FinalPlan[📄 Polished Final Travel Plan]
    FinalPlan --> EndNode

    subgraph StatePersistence["💾 State Persistence (PostgresSaver)"]
        Supervisor -. Checkpoint .-> DB[(PostgreSQL)]
        HITL -. Pause / Interrupt .-> DB
        ResumeRevision -. Resume Thread .-> DB
    end
```

---

## 🤖 The Specialist Agents

| Agent | Responsibility | Tools / Sources |
| :--- | :--- | :--- |
| **Supervisor Agent** | Analyzes parameters, checks guardrails, extracts constraints, routes workflow | Groq LLM, Regex Extractor |
| **Flight Agent** | Locates flight routes, departure/arrival airports, and airline recommendations | AviationStack MCP, Aviation Tools |
| **Hotel Agent** | Identifies accommodations across budget, mid-range, and luxury tiers | Tavily Web Search MCP |
| **Weather Agent** | Analyzes climate conditions and multi-day forecasts for packing tips | Custom Weather MCP (Open-Meteo) |
| **Budget Agent** | Calculates estimated expenses across flights, hotels, food, and activities | Cost Allocation Engine |
| **Itinerary Agent** | Generates detailed day-wise travel plans with sightseeing and dining spots | Synthesis Engine |
| **HITL & Final Agent** | Incorporates traveler feedback to refine and finalize the master itinerary | LangGraph State Interrupter |

---

## 🛠️ Tech Stack

- **Backend Framework**: [FastAPI](https://fastapi.tiangolo.com/) + [Uvicorn](https://www.uvicorn.org/)
- **Multi-Agent Orchestration**: [LangGraph](https://langchain-ai.github.io/langgraph/) & [LangChain](https://www.langchain.com/)
- **LLM Provider**: [Groq](https://groq.com/) (`llama-3.3-70b-versatile` / `openai/gpt-oss-20b`)
- **Protocol**: [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) (`mcp`, `langchain-mcp-adapters`)
- **Database / Checkpointer**: [PostgreSQL](https://www.postgresql.org/) (`psycopg`, `langgraph-checkpoint-postgres`)
- **Frontend**: HTML5, CSS3 (Modern Glassmorphism & Responsive Design), Vanilla JavaScript
- **Libraries**: `marked.js` (Markdown parsing), `html2pdf.js` (PDF export)
- **Containerization**: Docker

---

## 📁 Project Structure

```plaintext
TripMate-AI--A-Multi-agent-travel-planner/
├── app.py                         # FastAPI web application & API routes
├── backend.py                     # LangGraph workflow, agent nodes & checkpointer
├── custom_weather_mcp_server.py   # Custom Weather MCP Server (Open-Meteo)
├── mcp_client.py                  # MultiServer MCP client integration
├── requirements.txt               # Python package dependencies
├── Dockerfile                     # Docker container configuration
├── .dockerignore                  # Docker build exclusions
├── .env                           # Environment credentials & API keys (local)
├── static/
│   ├── style.css                  # UI styling (dark mode, glassmorphism)
│   └── scripts.js                 # Frontend interactions & API handlers
├── templates/
│   └── index.html                 # Main web application interface
└── tools/
    ├── flight_tool.py             # Flight data lookup helpers
    ├── tavily_tool.py             # Search tool helpers
    └── weather_tool.py            # Weather tool helpers
```

---

## 🚀 Getting Started

### 1. Prerequisites

- **Python 3.10+** (Python 3.11 recommended)
- **PostgreSQL Database** (Local instance or cloud provider like Render, Supabase, Neon)
- **API Keys**:
  - [Groq API Key](https://console.groq.com/) (Required)
  - [Tavily API Key](https://tavily.com/) (Required for search & hotels)
  - [AviationStack API Key](https://aviationstack.com/) (Optional for live flights)

---

### 2. Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/TripMate-AI--A-Multi-agent-travel-planner.git
   cd TripMate-AI--A-Multi-agent-travel-planner
   ```

2. **Create and activate a virtual environment**:
   ```bash
   # Windows
   python -m venv .venv
   .venv\Scripts\activate

   # Linux / macOS
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

---

### 3. Environment Configuration

Create a `.env` file in the root directory:

```env
# LLM Configuration
GROQ_API_KEY=your_groq_api_key_here
GROQ_MODEL=openai/gpt-oss-20b

# PostgreSQL Database (External Connection String)
DATABASE_URL=postgresql://user:password@hostname:5432/dbname?sslmode=require

# External APIs
TAVILY_API_KEY=your_tavily_api_key_here
AVIATION_STACK_API_KEY=your_aviationstack_api_key_here
OPENWEATHER_API_KEY=your_openweather_api_key_here
```

---

### 4. Run the Application

Start the FastAPI application:

```bash
uvicorn app:app --host 127.0.0.1 --port 8000 --reload
```

Open your browser and navigate to:
```
http://127.0.0.1:8000
```

---

## 🐳 Running with Docker

You can build and run the entire application using Docker:

### 1. Build the Docker Image
```bash
docker build -t tripmate-ai .
```

### 2. Run the Container
```bash
docker run -p 8000:8000 --env-file .env tripmate-ai
```

Access the application at `http://localhost:8000`.

---

## 🔌 API Reference

### 1. Plan a Trip (Generate Draft)
- **Endpoint**: `POST /api/travel`
- **Request Body**:
  ```json
  {
    "message": "Plan a 7-day trip to Japan from Delhi under 2 lakhs with budget hotels.",
    "thread_id": "optional-custom-thread-id"
  }
  ```
- **Response**:
  ```json
  {
    "success": true,
    "thread_id": "user_a1b2c3d4",
    "requires_approval": true,
    "selected_agents": ["flight_agent", "hotel_agent", "weather_agent", "budget_agent", "itinerary_agent"],
    "supervisor_reasoning": "Supervisor delegated tasks across all 5 specialist agents...",
    "itinerary": "### 7-Day Japan Travel Plan..."
  }
  ```

---

### 2. Human-in-the-Loop Review (Approve or Revise)
- **Endpoint**: `POST /api/travel/approve`
- **Request Body**:
  ```json
  {
    "thread_id": "user_a1b2c3d4",
    "approved": false,
    "feedback": "Reduce the hotel budget and add one free relaxation day."
  }
  ```
- **Response**:
  ```json
  {
    "success": true,
    "thread_id": "user_a1b2c3d4",
    "requires_approval": false,
    "answer": "### Final Polished Travel Plan..."
  }
  ```

---

### 3. Health Check
- **Endpoint**: `GET /health`
- **Response**:
  ```json
  {
    "status": "ok",
    "message": "TripMate AI API is running",
    "features": ["supervisor_agent", "input_guardrail", "human_in_the_loop"]
  }
  ```

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📜 License

Distributed under the MIT License. See [`LICENSE`](file:///c:/TripMate-AI--A-Multi-agent-travel-planner/LICENSE) for more information.

---

<div align="center">
  <sub>Built with ❤️ using FastAPI, LangGraph, Groq, PostgreSQL, and MCP.</sub>
</div>