import streamlit as st
import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.agent import MemoryAgent

st.set_page_config(page_title="Infinite Memory Agent", layout="wide")

st.title("🧠 NeuroHack Memory: Infinite Cognitive Persistence")
st.markdown("This agent remembers facts from Turn 1 to Turn 1000.")


if "agent" not in st.session_state:
    st.session_state.agent = MemoryAgent()
if "messages" not in st.session_state:
    st.session_state.messages = []


with st.sidebar:
    st.header("Memory State (Database)")
    if st.button("Refresh Memory View"):
        memories = st.session_state.agent.memory_store.get_all_memories()
        for m in memories:
            with st.expander(f"Turn {m.get('turn', '?')} - {m.get('category', 'Info')}"):
                st.write(m.get('content'))
                st.caption(m.get('timestamp'))


for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if "metadata" in msg:
            with st.expander("System Logic"):
                st.json(msg["metadata"])

if prompt := st.chat_input("Say something..."):
    
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    
    with st.chat_message("assistant"):
        with st.spinner("Thinking & Retrieving..."):
            result = st.session_state.agent.process_message(prompt)
            st.markdown(result["response"])
            
            
            debug_info = {
                "Memories Used": [m['content'] for m in result['active_memories']],
                "New Memory Stored": result['new_memory_saved']
            }
            with st.expander("Memory Operations"):
                st.json(debug_info)
    
    st.session_state.messages.append({
        "role": "assistant", 
        "content": result["response"],
        "metadata": debug_info
    })