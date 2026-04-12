import streamlit as st
import requests

# Page Configuration
st.set_page_config(page_title="CardioX AI", page_icon="❤️")

st.title("❤️ CardioX AI Assistant")
st.markdown("---")
st.caption("Ask me about heart health in simple English or Hinglish.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history from session state on rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("How can I help you today?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Call FastAPI Backend
    try:
        # We point to the FastAPI /chat endpoint we created earlier
        backend_url = "http://127.0.0.1:8000/chat"
        payload = {"question": prompt}
        
        with st.spinner("Thinking..."):
            response = requests.post(backend_url, json=payload)
            result = response.json()
            answer = result.get("answer", "Sorry, I couldn't process that.")

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(answer)
        
        st.session_state.messages.append({"role": "assistant", "content": answer})
        
    except Exception as e:
        st.error(f"Error connecting to backend: {e}")