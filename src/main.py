import json
import os
from datetime import datetime
from pdf_parser import extract_text_and_structure, identify_sections
from ranking import rank_sections
from summarizer import summarize_section

def process_documents(input_path, output_path):
    with open(input_path, 'r') as f:
        input_data = json.load(f)

    persona = input_data["persona"]["role"]
    job_to_be_done = input_data["job_to_be_done"]["task"]
    
    all_sections = []
    for doc_info in input_data["documents"]:
        pdf_path = os.path.join(os.path.dirname(input_path), "PDFs", doc_info["filename"])
        
        if not os.path.exists(pdf_path):
            print(f"Warning: PDF file not found at {pdf_path}")
            continue

        structure = extract_text_and_structure(pdf_path)
        sections = identify_sections(structure)
        
        for section in sections:
            section["document"] = doc_info["filename"]
        
        all_sections.extend(sections)

    ranked_sections = rank_sections(persona, job_to_be_done, all_sections)
    
    top_sections = ranked_sections[:15]

    subsection_analysis = []
    for section in top_sections:
        refined_text = summarize_section(section["title"], section["content"])
        subsection_analysis.append({
            "document": section["document"],
            "refined_text": refined_text,
            "page_number": section["page"]
        })

    output_data = {
        "metadata": {
            "input_documents": [doc["filename"] for doc in input_data["documents"]],
            "persona": persona,
            "job_to_be_done": job_to_be_done,
            "processing_timestamp": datetime.now().isoformat()
        },
        "extracted_sections": [{
            "document": s["document"],
            "section_title": s["title"],
            "importance_rank": s["importance_rank"],
            "page_number": s["page"]
        } for s in top_sections],
        "subsection_analysis": subsection_analysis
    }

    with open(output_path, 'w') as f:
        json.dump(output_data, f, indent=4)

if __name__ == "__main__":
    base_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "Challenge_1b")
    for collection_dir in os.listdir(base_path):
        collection_path = os.path.join(base_path, collection_dir)
        if os.path.isdir(collection_path):
            input_json_path = os.path.join(collection_path, "challenge1b_input.json")
            output_json_path = os.path.join(collection_path, "challenge1b_output.json")
            
            if os.path.exists(input_json_path):
                print(f"Processing {input_json_path}...")
                process_documents(input_json_path, output_json_path)
                print(f"Output saved to {output_json_path}")
