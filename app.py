import streamlit as st
from src.graph import app  # Imports your graph

st.set_page_config(page_title="LinkedIn Caption Generator", layout="centered")

if "input_text" not in st.session_state:
    st.session_state.input_text = ""

def clear_input():
    st.session_state.input_text = ""

st.title(" Multi-Agent LinkedIn Caption Generator")
st.markdown("Provide your topic, key takeaways, or thoughts, and let the LangGraph agents craft a professional post.")

user_topic = st.text_area(
    "What do you want to post about?", 
    key="input_text",
    height=150,
    placeholder="e.g., The role of transformers in deep learning..."
)

col1, col2 = st.columns(2)

with col1:
    generate_btn = st.button("Generate Post", type="primary", use_container_width=True)

with col2:
    refresh_btn = st.button("Refresh / Clear", on_click=clear_input, use_container_width=True)

# --- EXECUTION LOGIC ---
if generate_btn:
    if user_topic.strip() == "":
        st.warning("Please enter a topic or some thoughts first!")
    else:
        with st.spinner("Groq agents are crafting your post..."):
            
            # 1. This is the exact state from your screenshot, but using the UI text!
            initial_state = {
                "topic": user_topic,
                "iteration": 1,
                "max_iterations": 3
            }
            
            # 2. Tell your imported graph to run
            result = app.invoke(initial_state)
            
            # 3. Print the results to the web page
            st.success("Caption Generation Complete!")
            
            st.markdown("### Your LinkedIn Caption:")
            st.write(result["post"])  # Extracts just the text, exactly like your main.py
            
            st.markdown("---")
            # Prints your evaluation and iteration stats neatly at the bottom
            st.caption(f"Status: **{result['evaluation']}** | Total Iterations: **{result['iteration']}**")