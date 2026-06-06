import gradio as gr
from groq_api import ask_groq
gr.ChatInterface(
    fn=ask_groq,
    title="Groq API Chat Interface",
    description="Ask questions and get responses from the Groq API. The conversation history is maintained for context."
).launch(share=True)   # share=True → a public link you can post! 🎉