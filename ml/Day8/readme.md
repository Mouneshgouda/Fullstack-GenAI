## PDfChat


```python



!pip install -q PyPDF2 langchain faiss-cpu spacy transformers langchain-community
!python -m spacy download en_core_web_sm

from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings.spacy_embeddings import SpacyEmbeddings
from langchain_community.vectorstores import FAISS
from transformers import pipeline
from google.colab import files
import os, tempfile

uploaded = files.upload()
pdf_path = next(iter(uploaded))
file_path = os.path.join(tempfile.gettempdir(), pdf_path)
with open(file_path, 'wb') as f: f.write(uploaded[pdf_path])

reader = PdfReader(file_path)
text = "".join([page.extract_text() or "" for page in reader.pages])
print("📄 Extracted text preview:\n", text[:1000]) 
chunks = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200).split_text(text)

embedder = SpacyEmbeddings(model_name="en_core_web_sm")
db = FAISS.from_texts(chunks, embedder)
retriever = db.as_retriever()

qa = pipeline("question-answering", model="deepset/roberta-base-squad2")

def ask(q):
    docs = retriever.get_relevant_documents(q)

    print("\n Top Retrieved Chunks:")
    for i, doc in enumerate(docs[:2]):
        print(f"\n--- Chunk {i+1} ---\n{doc.page_content[:500]}\n")

    context = " ".join([doc.page_content for doc in docs[:2]])[:1000]
    result = qa(question=q, context=context)
    print(f"\n Question: {q}\n Answer: {result['answer']}")
```
    
