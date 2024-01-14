import streamlit as st
from llama_hub.tools.arxiv import ArxivToolSpec
from llama_index.agent import OpenAIAgent

# Initialize the agent with arXiv tool
tool_spec = ArxivToolSpec()
agent = OpenAIAgent.from_tools(tool_spec.to_tool_list())

# Streamlit app
st.title('Scientific Paper Query')

# User input
user_query = st.text_input('Enter your query about scientific developments:')

# When the user presses the 'Search' button
if st.button('Search'):
    # Assuming the agent.chat method returns a response you can display
    response = agent.chat(user_query)
    
    # Display the response
    st.write(response)
