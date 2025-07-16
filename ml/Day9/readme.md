
# Text
```python

from transformers import pipeline
import gradio as gr


summarizer=pipeline("summarization",model="facebook/bart-large-cnn")

def summarize(text):
  if len(text.strip())<50:
    return "please enter the 50 characters of text"

    summary = summarizer(text, max_length=150, min_length=30, do_sample=False)[0]['summary_text']
    return summary

demo = gr.Interface(
    fn=summarize,
    inputs=gr.Textbox(lines=15, placeholder="text here..."),
    outputs="text",
    title=" AI Text Summarizer",
    description="Paste any long article or paragraph"
)
demo.launch(share=True)

```
