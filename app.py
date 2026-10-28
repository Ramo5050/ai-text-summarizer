import gradio as gr
import time

def mock_summarize(text):
    if not text.strip():
        return "Please enter some text."
    
    time.sleep(1.5) 
    
    # A slightly better fake: just grab the first two sentences.
    sentences = text.split('.')
    if len(sentences) > 1:
        summary = sentences[0] + ". " + sentences[1] + "."
    else:
        summary = text
        
    return summary

with gr.Blocks() as demo:
    gr.Markdown("# 📝 AI Text Summarizer")
    gr.Markdown("Paste text below to summarize it.")
    
    input_text = gr.Textbox(label="Input Text", lines=5)
    summarize_btn = gr.Button("Summarize")
    output_text = gr.Textbox(label="Summary", lines=5)
    
    summarize_btn.click(fn=mock_summarize, inputs=input_text, outputs=output_text)

demo.launch(share=True)