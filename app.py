import gradio as gr
import pandas as pd
import matplotlib.pyplot as plt
from pydantic import BaseModel
import ollama

# Global variable to store CSV data
df = None

# Define Pydantic Model for structured query processing
class Query(BaseModel):
    question: str

# Function to handle CSV upload
def upload_csv(file):
    global df
    try:
        df = pd.read_csv(file.name)
        return "CSV uploaded successfully! You can now ask questions."
    except Exception as e:
        return f"Error uploading CSV: {str(e)}"

# Function to answer queries using Ollama LLM
def answer_question(question):
    if df is None:
        return "Please upload a CSV file first."
    
    query = Query(question=question)
    response = ollama.chat(model="llama3.1-8b", messages=[{"role": "user", "content": query.question}])
    return response['message']['content']

# Function to generate graphs
def plot_graph(column_x, column_y):
    if df is None:
        return "Please upload a CSV file first."
    
    if column_x not in df.columns or column_y not in df.columns:
        return f"Invalid columns. Available columns: {', '.join(df.columns)}"
    
    plt.figure(figsize=(8, 5))
    plt.scatter(df[column_x], df[column_y], alpha=0.5)
    plt.xlabel(column_x)
    plt.ylabel(column_y)
    plt.title(f"{column_y} vs {column_x}")
    plt.grid(True)
    
    graph_path = "graph.png"
    plt.savefig(graph_path)
    return graph_path

# Build Gradio interface
with gr.Blocks() as app:
    gr.Markdown("# CSV Question Answering & Visualization App")
    file_input = gr.File(label="Upload CSV File", type="filepath")

    file_output = gr.Textbox(label="Upload Status")
    
    file_input.change(upload_csv, inputs=file_input, outputs=file_output)
    
    question_input = gr.Textbox(label="Ask a question about the data")
    answer_output = gr.Textbox(label="Answer")
    
    question_input.submit(answer_question, inputs=question_input, outputs=answer_output)
    
    column_x = gr.Textbox(label="X-axis Column")
    column_y = gr.Textbox(label="Y-axis Column")
    plot_button = gr.Button("Plot Graph")
    graph_output = gr.Image()
    
    plot_button.click(plot_graph, inputs=[column_x, column_y], outputs=graph_output)

# Launch Gradio app
app.launch()
