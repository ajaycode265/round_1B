import fitz  # PyMuPDF
import statistics

def extract_text_and_structure(pdf_path):
    doc = fitz.open(pdf_path)
    structure = []
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            if block["type"] == 0:  # Text block
                for line in block["lines"]:
                    for span in line["spans"]:
                        structure.append({
                            "text": span["text"],
                            "size": span["size"],
                            "font": span["font"],
                            "page": page_num + 1,
                            "flags": span["flags"]
                        })
    return structure

def identify_sections(structure):
    if not structure:
        return []

    font_sizes = [s['size'] for s in structure if s['text'].strip()]
    if not font_sizes:
        return []
        
    median_size = statistics.median(font_sizes)
    
    sections = []
    current_section = None
    content_buffer = []

    for item in structure:
        text = item['text'].strip()
        if not text:
            continue

        is_bold = item["flags"] & 16
        is_heading = (is_bold or item['size'] > median_size * 1.15) and len(text) > 2 and not text.isnumeric()

        if is_heading:
            if current_section:
                current_section['content'] = " ".join(content_buffer)
                sections.append(current_section)
            
            current_section = {
                "title": text,
                "page": item["page"],
                "content": ""
            }
            content_buffer = []
        elif current_section:
            content_buffer.append(text)

    if current_section:
        current_section['content'] = " ".join(content_buffer)
        sections.append(current_section)
        
    return sections
