import streamlit as st
from openai import OpenAI
openkey =st.secrets["OPENAI_KEY"]

client = OpenAI(api_key=openkey)

def gpt_wrapper_message(text):
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "developer", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": text
            }
        ]
    )

    st.write(completion.choices[0].message)