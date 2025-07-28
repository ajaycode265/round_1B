import spacy
from collections import Counter

nlp = spacy.load("en_core_web_sm")

def summarize_section(section_title, section_content):
    if not section_content or section_content.isspace():
        return ""

    doc = nlp(section_content)
    sentences = [sent.text for sent in doc.sents]
    
    if not sentences:
        return ""

    # Extract keywords from the title
    if not section_title or section_title.isspace():
        title_keywords = []
    else:
        title_keywords = [token.lemma_ for token in nlp(section_title.lower()) if token.pos_ in ["NOUN", "PROPN", "VERB"] and not token.is_stop]

    sentence_scores = []
    for sentence in sentences:
        if not sentence or sentence.isspace():
            continue
        sentence_keywords = [token.lemma_ for token in nlp(sentence.lower()) if token.pos_ in ["NOUN", "PROPN", "VERB"] and not token.is_stop]
        score = len(set(title_keywords) & set(sentence_keywords))
        sentence_scores.append((score, sentence))

    sentence_scores.sort(key=lambda x: x[0], reverse=True)
    
    num_sentences = min(3, len(sentence_scores))
    
    # Return the top sentences in their original order
    top_sentences = sorted(sentence_scores[:num_sentences], key=lambda x: section_content.find(x[1]))
    
    return ". ".join([s[1] for s in top_sentences])
