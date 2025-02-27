import streamlit as st
from openai import OpenAI
openkey =st.secrets["OPENAI_KEY"]

client = OpenAI(api_key=openkey)

def gpt_wrapper_message(prompt):
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return(completion.choices[0].message["content"])