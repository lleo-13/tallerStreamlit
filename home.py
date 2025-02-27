import streamlit as st
import numpy as np
import pandas as pd
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key="OPENAI_KEY")


from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "developer", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a haiku about recursion in programming."
        }
    ]
)

print(completion.choices[0].message)

st.title("App Title")

st.divider()

st.subheader("CHAD BOT")

text = st.chat_input("Type a message...")

if st.button("Send"):
    #write your logic here
    st.success("You sent a message!")
else:
    st.warning("Send a message")

