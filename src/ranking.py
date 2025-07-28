import spacy
from collections import Counter

nlp = spacy.load("en_core_web_sm")

def extract_keywords(text):
    if not text or text.isspace():
        return []
    doc = nlp(text.lower())
    keywords = [token.lemma_ for token in doc if token.pos_ in ["NOUN", "PROPN", "VERB"] and not token.is_stop]
    return keywords

def rank_sections(persona, job_to_be_done, sections):
    query_text = f"{persona} {job_to_be_done}"
    query_keywords = extract_keywords(query_text)
    
    ranked_sections = []
    for section in sections:
        section_text = f"{section['title']} {section['content']}"
        section_keywords = extract_keywords(section_text)
        
        # Score based on keyword overlap
        score = len(set(query_keywords) & set(section_keywords))
        
        ranked_sections.append({
            "section": section,
            "score": score
        })
        
    ranked_sections.sort(key=lambda x: x["score"], reverse=True)
    
    # Filter out duplicate or highly similar titles
    unique_sections = []
    seen_titles = set()
    for item in ranked_sections:
        title = item["section"]["title"].strip().lower()
        if title not in seen_titles:
            unique_sections.append(item["section"])
            seen_titles.add(title)
            
    for i, section in enumerate(unique_sections):
        section["importance_rank"] = i + 1
        
    return unique_sections
