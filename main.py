from src.graph import app

def main():
    print(" Starting LinkedIn Post Generator Agent...")
    
    initial_state = {
        "topic": "Created a linkedin post generator with the help of agentic AI using langgraph",
        "iteration": 1,
        "max_iterations": 3
    }

    result = app.invoke(initial_state)

    print("\n FINAL RESULT:")
    print("-" * 50)
    print(result["post"])
    print("-" * 50)
    print(f"Status: {result['evaluation']}")
    print(f"Total Iterations: {result['iteration']}")

if __name__ == "__main__":
    main() 