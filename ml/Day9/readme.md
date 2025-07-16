
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


## medical image analysis


```python

!pip install agno
!pip install duckduckgo-search
!pip install pillow
!pip install gradio

import os
from PIL import Image as PILImage
from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.media import Image as AgnoImage
import gradio as gr

# Load Google API Key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Prompt for medical image analysis
query = """
You are a highly skilled medical imaging expert with extensive knowledge in radiology and diagnostic imaging. Analyze the patient's medical image and structure your response as follows:

### 1. Image Type & Region
- Specify imaging modality (X-ray/MRI/CT/Ultrasound/etc.)
- Identify the patient's anatomical region and positioning
- Comment on image quality and technical adequacy

### 2. Key Findings
- List primary observations systematically
- Note any abnormalities in the patient's imaging with precise descriptions
- Include measurements and densities where relevant
- Describe location, size, shape, and characteristics
- Rate severity: Normal/Mild/Moderate/Severe

### 3. Diagnostic Assessment
- Provide primary diagnosis with confidence level
- List differential diagnoses in order of likelihood
- Support each diagnosis with observed evidence from the patient's imaging
- Note any critical or urgent findings

### 4. Patient-Friendly Explanation
- Explain the findings in simple, clear language that the patient can understand
- Avoid medical jargon or provide clear definitions
- Include visual analogies if helpful
- Address common patient concerns related to these findings

### 5. Research Context
IMPORTANT: Use the DuckDuckGo search tool to:
- Find recent medical literature about similar cases
- Search for standard treatment protocols
- Provide a list of relevant medical links of them too
- Research any relevant technological advances
- Include 2-3 key references to support your analysis

Format your response using clear markdown headers and bullet points. Be concise yet thorough.
"""

# Image analysis function
def analyze_medical_image(api_key, image_np):
    if not api_key:
        return " Please provide a valid Google API key."

    try:
        # Initialize the agent
        agent = Agent(
            model=Gemini(id="gemini-2.0-flash", api_key=api_key),
            tools=[DuckDuckGoTools()],
            markdown=True
        )

        # Resize image
        img = PILImage.fromarray(image_np)
        img = img.resize((500, int(500 / img.width * img.height)))
        temp_path = "temp_image.png"
        img.save(temp_path)

        # Analyze with Gemini + DuckDuckGo
        agno_img = AgnoImage(filepath=temp_path)
        result = agent.run(query, images=[agno_img])

        return result.content

    except Exception as e:
        return f" Analysis error: {e}"

# Gradio UI
with gr.Blocks() as demo:
    gr.Markdown("##  Medical Imaging Diagnosis Agent")
    gr.Markdown("Upload a medical image to receive an AI-generated analysis report.\n\n **Disclaimer:** Educational use only. Not a clinical diagnosis tool.")

    api_input = gr.Textbox(label=" Google API Key", type="password", placeholder="Paste your API key")
    image_input = gr.Image(label="Upload Medical Image", type="numpy")
    analyze_button = gr.Button(" Analyze")
    output_md = gr.Markdown()

    analyze_button.click(analyze_medical_image, inputs=[api_input, image_input], outputs=output_md)

demo.launch()


```
