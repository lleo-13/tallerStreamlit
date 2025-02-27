import streamlit as st
import numpy as np
import pandas as pd
from openai import OpenAI
import gptwrapper

st.title("App Title")

st.divider()

st.subheader("CHAD BOT")

text = st.chat_input("Type a message...")

if st.button("Send"):
    #write your logic here
    response = gptwrapper.gpt_wrapper_message(text)
    st.success("You sent a message!")
    st.write(response)
else:
    st.warning("Send a message")

