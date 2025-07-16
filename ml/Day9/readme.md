
# Text
```python

!pip install -q "lxml[html_clean]" newspaper3k
!python -m nltk.downloader punkt

!pip install -q newspaper3k
!python -m nltk.downloader punkt


import gradio as gr
from transformers import pipeline
from newspaper import Article

# Load summarization model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Extract article text from URL
def extract_text_from_url(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        return article.text
    except Exception as e:
        return f"Error fetching article: {e}"

# Summarization logic
def summarize_input(text, url):
    if url.strip():
        text = extract_text_from_url(url)

    if not text or len(text.strip()) < 50:
        return "Please provide at least 50 characters of content."

    summary = summarizer(text, max_length=180, min_length=40, do_sample=False)[0]["summary_text"]
    return summary

# Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("##  AI Text & URL Summarizer")
    gr.Markdown("Paste text OR enter a URL to summarize content. Powered by BART.")

    with gr.Row():
        text_input = gr.Textbox(label="Text Input", placeholder="Paste long text here...", lines=10)
        url_input = gr.Textbox(label="URL Input", placeholder="https://example.com/article")

    summarize_button = gr.Button("Summarize")
    output = gr.Textbox(label="Summary Output", lines=6)

    summarize_button.click(
        fn=summarize_input,
        inputs=[text_input, url_input],
        outputs=output
    )

demo.launch(share=True)


```
# Agent

```python

from crewai import Agent, Task, Crew, Process, LLM


llm = LLM(model="gemini/gemini-2.0-flash")


fact_agent = Agent(
    role="Fact Expert",
    goal="Answer general knowledge questions with accurate and concise information.",
    backstory="An AI assistant trained in trivia, science, history, and general facts.",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

explanation_agent = Agent(
    role="Friendly Explainer",
    goal="Break down complex answers into simple, easy-to-understand explanations.",
    backstory="A helpful teacher who simplifies answers for students and beginners.",
    verbose=True,
    allow_delegation=False,
    llm=llm
)


task1 = Task(
    description="""Question: What causes lightning during a thunderstorm?
Please provide a factual and scientific explanation.""",
    expected_output="A concise scientific explanation of lightning formation.",
    agent=fact_agent
)

task2 = Task(
    description="""Question: Explain how lightning works in a way that a 10-year-old could understand.""",
    expected_output="A simplified, analogy-based explanation of lightning for a child.",
    agent=explanation_agent
)
crew = Crew(
    agents=[fact_agent, explanation_agent],
    tasks=[task1, task2],
    verbose=True,
    process=Process.sequential,  
)

crew_output = crew.kickoff()
print("\nCrew Output:")
print(crew_output)


```
LangGraph

```python

import os
import google.generativeai as genai
os.environ["GOOGLE_API_KEY"] = "AIzaSyB_V3DqJiHPzsbklDmkQQNnSORGPTNnNyo"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

model = genai.GenerativeModel("gemini-1.5-flash")

def chat_node(state):
  user_input=state["message"]
  history=state.get["history",[]]

  prompt = "\n".join([f"User: {h['user']}\nBot: {h['bot']}" for h in history])
  prompt += f"\n\nUser: {user_input}\nBot:"

  response=model.generate_content(prompt)
  replay=response.text.strip()
  history.append({"user":user_input,"bot":replay})

  return {"message": "", "history": history, "reply": reply}


```
