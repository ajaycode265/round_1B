# Adobe India Hackathon 2025

## Welcome to the "Connecting the Dots" Challenge

This repository contains the solution for the Adobe India Hackathon 2025, including the persona-driven document intelligence system for Challenge 1b.

## Challenge 1b: Persona-Driven Document Intelligence

This solution is a Python-based application that analyzes a collection of PDF documents and extracts the most relevant sections based on a given persona and job-to-be-done.

### Features

- **Persona-Based Analysis:** Ranks document sections based on their relevance to a user's persona and task.
- **Extractive Summarization:** Provides concise summaries of the most important sections.
- **Dockerized Solution:** The application is containerized for optional deployment and execution.

### Project Structure

```
.
├── Dockerfile
├── README.md
├── approach_explanation.md
├── requirements.txt
├── src/
│ ├── main.py
│ ├── pdf_parser.py
│ ├── ranking.py
│ └── summarizer.py
└── Challenge_1b/
    └── [Collection Name]/
        ├── PDFs/
        │   ├── document1.pdf
        │   └── ...
        └── challenge1b_input.json
```

### ⚙️ How to Run the Solution

You can run the solution **with or without Docker**.

---

#### ✅ Recommended: Run Locally Without Docker (CPU + Offline Compatible)

> **This solution is fully functional on CPU and does not require an internet connection once dependencies are installed.**

1. **Install Dependencies (Manually):**

   **Important:** Installing `spacy` inside Docker can be time-consuming. To avoid long build times, it is **highly recommended to install all packages separately on your system before execution.**

   Run the following command in the root directory:

   ```bash
   pip install -r requirements.txt
   ```

2. **Download Required Spacy Model (only once):**

   If you're online during setup, run:

   ```bash
   python -m spacy download en_core_web_sm
   ```
   💡 Skip this if the model is already downloaded or if running offline.

3. **Prepare Input Data:**

   - Inside the `Challenge_1b` directory, create a new folder for your collection (e.g., `My_Collection`).
   - Add a `PDFs/` subdirectory with all your input PDFs.
   - Add a `challenge1b_input.json` file at the root of that collection folder (use examples as reference).

4. **Run the Application:**

   From the root project directory:

   ```bash
   python src/main.py
   ```
   This will process all collections under the `Challenge_1b` directory and generate corresponding `challenge1b_output.json` files inside each collection folder.

---

#### 🐳 Optional: Run with Docker (if needed)

1. **Build Docker Image:**

   ⚠️ Note: Building the Docker image may take time due to Spacy installation.

   ```bash
   docker build --platform linux/amd64 -t document-intelligence .
   ```

2. **Run the Docker Container:**

   ```bash
   docker run --rm -v "%cd%/Challenge_1b":/app/Challenge_1b document-intelligence
   ```
   This will process all collections and generate the output files in the same directory.

---

#### 📄 For More Details
Refer to `approach_explanation.md` for a full explanation of the methodology, design, and component structure.
