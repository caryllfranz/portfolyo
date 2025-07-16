import random
import time
import streamlit as st

# Streamed response emulator
def response_generator():
    responses = [
        "connect me through linkedin https://www.linkedin.com/in/caryllfmc/",
        "Hello, contact me @caryllcarino",
        "Hello, call me at #09687056310",
        "boss??",
        "EVERYDAY IS A GOOD DAY TO LEARN",
        "Consistency is the key!"
    ]
    
    response = random.choice(responses)
    
    for word in response.split():
        yield word + " "
        time.sleep(0.05)

st.title("CHATBOT")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Kamusta ang buhay-buhay boss??"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container with streaming effect
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        response_content = ""

        # Generate the response word by word
        for word in response_generator():
            response_content += word
            response_placeholder.markdown(response_content)
        
        # Save full response to session state after streaming
        st.session_state.messages.append({"role": "assistant", "content": response_content})
