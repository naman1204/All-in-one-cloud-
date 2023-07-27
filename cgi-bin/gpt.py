#!/usr/bin/python3
import cgi
import openai
print("content-type: text/html")
print()

form = cgi.FieldStorage()
prompt = form.getvalue("prompt")

mykey = "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"
openai.api_key = mykey
# Define the list of prompts you want to use
prompts = [
    {"role": "system", "content": "You are an expert language translator in all languages."},
    {"role": "user", "content": prompt},  # User-provided prompt
    {"role": "system", "content": "You are a DevOps expert."},
    {"role": "user", "content": "As a DevOps expert, how can I automate server provisioning?"},
    {"role": "system", "content": "You are an ML expert."},
    {"role": "user", "content": "As an ML expert, how can I improve the accuracy of my model?"},
    {"role": "system", "content": "You are a full-stack expert."},
    {"role": "user", "content": "As a full-stack expert, what are the best practices for designing scalable web applications?"}
]

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    max_tokens=150,  # Increase the max_tokens to allow for longer responses
    temperature=0,
    messages=prompts  # Use the defined prompts list
)
print(response.choices[0].message.content)

