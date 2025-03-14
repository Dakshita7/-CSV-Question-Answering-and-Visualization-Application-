# -CSV-Question-Answering-and-Visualization-Application-
This project is a Gradio-based web application that allows users to:

Upload a CSV file.

Ask questions (textual & numerical) about the data using a local Large Language Model (LLM).

Generate visualizations (scatter plots) from the CSV data.

View all outputs within the Gradio UI.

Features
- CSV File Upload & Validation
- LLM-powered Question Answering (Ollama + Pydantic AI)
-  Graph Generation & Visualization (Matplotlib)
-  Local Execution (No external API calls required)
-   Modular Code Structure for easy modifications

Installation & Setup

Step 1: Install Python & Dependencies

pip install gradio pandas matplotlib ollama pydantic

Step 2: Install & Run Ollama

Download and install Ollama from ollama.com.

Start the Ollama server:

ollama serve

Pull the Llama 3.1 8B model (or a smaller one):

ollama pull llama3.1-8b

Step 3: Run the Application

Save the Python script as app.py and execute:

python app.py

Step 4: Access the Gradio UI

Once running, open http://127.0.0.1:7860/ in your browser.

Usage

Upload a CSV file (max size: 25MB).

Ask questions about the data in the text box.

Generate visualizations by entering column names for the X & Y axes.

View answers & graphs inside the Gradio interface.
