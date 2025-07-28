# Adobe India Hackathon 2025

## Welcome to the "Connecting the Dots" Challenge

This repository contains the solution for the Adobe India Hackathon 2025, including the persona-driven document intelligence system for Challenge 1b.

## Challenge 1b: Persona-Driven Document Intelligence

This solution is a Python-based application that analyzes a collection of PDF documents and extracts the most relevant sections based on a given persona and job-to-be-done.

### Features

-   **Persona-Based Analysis:** Ranks document sections based on their relevance to a user's persona and task.
-   **Extractive Summarization:** Provides concise summaries of the most important sections.
-   **Dockerized Solution:** The application is containerized for easy deployment and execution.

### Project Structure

```
.
├── Dockerfile
├── README.md
├── approach_explanation.md
├── requirements.txt
├── src/
│   ├── main.py
│   ├── pdf_parser.py
│   ├── ranking.py
│   └── summarizer.py
└── Challenge_1b/
    └── [Collection Name]/
        ├── PDFs/
        │   ├── document1.pdf
        │   └── ...
        └── challenge1b_input.json
```

### How to Run the Solution

1.  **Prepare Your Data:**

    -   Inside the `Challenge_1b` directory, create a new folder for each collection of documents (e.g., `My_Collection`).
    -   Inside each collection folder, create a `PDFs` directory and place all your PDF files there.
    -   In the root of the collection folder, create a `challenge1b_input.json` file. This file must contain the persona, job-to-be-done, and a list of the PDF filenames to be processed. You can use the existing collections as a template.

2.  **Build the Docker Image:**

    ```bash
    docker build --platform linux/amd64 -t document-intelligence .
    ```

    **Note:** If you encounter any issues during the Docker build process, it may be due to package installation failures. As a workaround, you can manually install the required packages using `pip`:

    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Docker Container:**

    The container is configured to process all collections within the `Challenge_1b` directory and generate the output in the same directory.

    To run the solution, use the following command, which mounts the `Challenge_1b` directory into the container:

    ```bash
    docker run --rm -v "%cd%/Challenge_1b":/app/Challenge_1b document-intelligence
    ```

    The application will process the `challenge1b_input.json` file in each collection directory and generate a corresponding `challenge1b_output.json` file.

---

**Note**: For a detailed explanation of the methodology and architecture, please refer to the `approach_explanation.md` file.
