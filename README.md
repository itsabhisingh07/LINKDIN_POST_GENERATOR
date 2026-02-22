#  Agentic AI LinkedIn Post Generator

An intelligent, multi-agent AI system designed to automatically generate, evaluate, and optimize professional LinkedIn posts. 

Built using **LangGraph** and **Groq**, this tool takes a simple topic and iteratively refines it until it meets strict formatting and quality criteria suitable for professional networking.

##  Features
* **Agentic Workflow:** Utilizes LangGraph to create a stateful, cyclical workflow between a Generator, Evaluator, and Optimizer.
* **Strict Evaluation:** Uses Pydantic for structured outputs to ensure the generated post adheres to specific constraints (e.g., character limits, no emojis, professional tone).
* **Iterative Optimization:** Automatically rewrites the post based on AI feedback until it is "approved" or hits a maximum iteration limit.
* **High-Speed Inference:** Powered by the `llama-3.3-70b-versatile` model hosted on Groq for lightning-fast reasoning.

##  Tech Stack
* **Framework:** LangChain, LangGraph
* **LLM:** Meta Llama 3.3 70B (via Groq)
* **Environment:** Python, `uv` package manager

##  How to Run Locally

### 1. Clone the repository
```bash
git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)
cd YOUR_REPO_NAME
```

2. Set up the environment
Create a .env file in the root directory and add your Groq API key:

Plaintext
GROQ_API_KEY=your_api_key_here
3. Install dependencies
If you are using uv (recommended):

Bash
uv sync
Or, using standard pip:

Bash
pip install -r requirements.txt
4. Run the Agent
Bash
python main.py