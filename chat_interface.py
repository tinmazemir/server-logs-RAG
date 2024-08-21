import streamlit as st
import answer_with_chatgpt as chatgpt
import search_index as search_index
from streamlit_chat import message

chatgpt.define_openai_key()
jsonData, index = search_index.read_data()


st.title("Server Log Analyser Assistant")

k_slider = st.sidebar.slider(
    'How many logs to search for?',
    1, 20, (1)
)

st.text_input("Search logs", key="query")

st.button("Search", key="search")

if st.session_state.search:
   distance, indices = search_index.search_index(searchText=st.session_state.query,index=index,k=k_slider)
   logs = search_index.log_finder_from_index(indices,jsonData)
   response = chatgpt.get_chatgpt_response(logs=logs,question=st.session_state.query)
   st.write(response.choices[0].message.content)
   st.write(logs)


