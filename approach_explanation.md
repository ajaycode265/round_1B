# Approach Explanation

This document outlines the methodology and architecture of the persona-driven document intelligence system developed for the Adobe India Hackathon 2025.

## 1. Core Architecture

The solution is a Python-based application designed to be modular, efficient, and compliant with the specified constraints. The architecture is composed of four main components:

- **PDF Parser (`pdf_parser.py`):** This module is responsible for extracting text and identifying potential section titles from the input PDF documents. It uses the `PyMuPDF` library for its high performance and accuracy. The parser analyzes the document's structure, identifying headings based on font size, style, and layout cues.

- **Relevance Ranking (`ranking.py`):** This is the core of the system. It uses the `spaCy` library to perform natural language processing on the persona, job-to-be-done, and each extracted section. By extracting keywords and comparing them, the module ranks sections based on their contextual relevance to the user's query.

- **Subsection Summarizer (`summarizer.py`):** For the top-ranked sections, this module performs a more detailed analysis. It employs an extractive summarization technique based on keyword matching with the section title to identify and extract the most salient sentences from each section, providing a concise summary of the key information.

- **Main Orchestrator (`main.py`):** This script serves as the central controller, managing the overall workflow. It reads the input JSON, orchestrates the calls to the other modules, and generates the final output JSON in the specified format.

## 2. Workflow

The processing pipeline is as follows:

1.  **Input Processing:** The `main.py` script reads the input `challenge1b_input.json` file to get the persona, job-to-be-done, and the list of documents to be analyzed.

2.  **PDF Parsing:** For each document, the `pdf_parser.py` module is invoked to extract the text and identify potential section titles.

3.  **Relevance Ranking:** The `ranking.py` module takes the persona, job-to-be-done, and the extracted sections as input. It then extracts keywords and calculates a relevance score to rank the sections by importance.

4.  **Subsection Analysis:** The `summarizer.py` module processes the top-ranked sections to generate extractive summaries, which are included in the final output.

5.  **Output Generation:** The `main.py` script compiles the results into the final `challenge1b_output.json` file, including metadata, extracted sections, and subsection analysis.

## 3. Design Choices and Justification

- **spaCy:** The use of `spaCy` for keyword extraction allows for a more nuanced and context-aware analysis than simple keyword matching, resulting in more accurate and relevant section ranking.

- **PyMuPDF:** This library was selected for its speed and efficiency in parsing PDF documents, which is crucial for meeting the processing time constraints of the challenge.

- **Modular Architecture:** The modular design of the application makes it easy to maintain, test, and extend. Each component has a single responsibility, which improves code clarity and reduces complexity.
