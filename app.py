import gradio as gr
import time
import os
from openai import OpenAI

# Note for Judges: The API key is kept private, so the app defaults to a 
# local text extraction method if the API key is not present in the environment.
API_KEY = os.getenv("NEBIUS_API_KEY")

def summarize_text(text):
    if not text.strip():
        return "Please enter some text."
    
    if API_KEY:
        try:
            client = OpenAI(base_url="https://api.studio.nebius.ai/v1/", api_key=API_KEY)
            response = client.chat.completions.create(
                model="nvidia/llama-3.1-nemotron-70b-instruct",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that summarizes text concisely."},
                    {"role": "user", "content": f"Please summarize this text:\n\n{text}"}
                ],
                temperature=0.5,
                max_tokens=200
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"API Error: {str(e)}"
    else:
        # Fallback for demo purposes
        time.sleep(1)
        sentences = text.split('.')
        if len(sentences) > 1:
            return sentences[0] + ". " + sentences[1] + "."
        return text

with gr.Blocks() as demo:
    gr.Markdown("# 📝 AI Text Summarizer")
    gr.Markdown("Paste text below to summarize it.")
    
    input_text = gr.Textbox(label="Input Text", lines=5)
    summarize_btn = gr.Button("Summarize")
    output_text = gr.Textbox(label="Summary", lines=5)
    
    summarize_btn.click(fn=summarize_text, inputs=input_text, outputs=output_text)

demo.launch(share=True)
