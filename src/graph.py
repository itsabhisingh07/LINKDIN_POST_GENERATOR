from langgraph.graph import StateGraph, START, END
from langchain_core.messages import SystemMessage, HumanMessage
from src.config import llm
from src.state import LinkPost, PostEvaluation

# --- NODE 1: GENERATOR ---
def generate_post(state: LinkPost):
    print(f"--- GENERATING POST (Iteration {state.get('iteration', 1)}) ---")
    messages = [
        SystemMessage(content="You are a AI researcher/Student."),
        HumanMessage(content=f"""Generate a short and insightful post about "{state['topic']}".
        Rules:
        - Do not use question-answer format.
        - max 300-400 characters
        - use simple english to understand by more user
        - mention all technologies required for it
        - overview about what it is generally do
        """)
    ]
    response = llm.invoke(messages).content
    return {"post": response}

# --- NODE 2: EVALUATOR ---
def evaluate_post(state: LinkPost):
    print("--- EVALUATING POST ---")
    
    # Create the structured evaluator
    structured_evaluator = llm.with_structured_output(PostEvaluation)

    messages = [
        SystemMessage(content="You are an AI evaluator model. Your task is to evaluate a LinkedIn post."),
        HumanMessage(content=f"""
        Topic: "{state['topic']}"
        Post: "{state['post']}"
        
        EVALUATION CRITERIA:
        1. Length must be 300-400 characters.
        2. Must mention relevant technologies.
        3. No emojis, hashtags, or bullet points.
        
        Respond ONLY with the strict structure.
        """)
    ]
    
    response = structured_evaluator.invoke(messages)
    
    # Map the Pydantic response back to our state dictionary
    return {
        "evaluation": response.evaluation,
        "feedback": response.feedback
    }

# --- NODE 3: OPTIMIZER ---
def optimizer_post(state: LinkPost):
    print("--- OPTIMIZING POST ---")
    messages = [
        SystemMessage(content="You improve the tweet based on the given Topic and criteria."),
        HumanMessage(content=f"""
        Improve the post based on the feedback: "{state['feedback']}"
        
        Topic: "{state['topic']}"
        Original post: "{state['post']}"
        
        Re-Write it as 300-400 characters, and perfect to post.
        """)
    ]
    response = llm.invoke(messages).content
    
    # Increment iteration count
    return {
        "post": response, 
        "iteration": state["iteration"] + 1
    }

# --- ROUTING LOGIC ---
def route_evaluation(state: LinkPost):
    if state["evaluation"] == "approved" or state["iteration"] >= state["max_iterations"]:
        return "approved"
    else:
        return "needs_improvement"

# --- GRAPH CONSTRUCTION ---
workflow = StateGraph(LinkPost)

workflow.add_node("generate", generate_post)
workflow.add_node("evaluate", evaluate_post)
workflow.add_node("optimize", optimizer_post)

workflow.add_edge(START, "generate")
workflow.add_edge("generate", "evaluate")

workflow.add_conditional_edges(
    "evaluate",
    route_evaluation,
    {
        "approved": END,
        "needs_improvement": "optimize"
    }
)
workflow.add_edge("optimize", "evaluate")

# Compile the graph
app = workflow.compile()