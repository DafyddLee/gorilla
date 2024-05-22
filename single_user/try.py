import streamlit as st
import time



def loading_spinner():
    with st.spinner('Loading...'):
        time.sleep(5)  # Simulate some long-running process
        st.success('Loading done!')

# st.session_state['sheetmade'] = False
# st.session_state['authenticated'] = False

loading_spinner()