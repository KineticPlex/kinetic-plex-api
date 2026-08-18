import spacy

nlp = spacy.load("es_core_news_lg")

class NlpService:
  
  @staticmethod
  def text_to_gloss(text):
    doc = nlp(text.lower())
    
    time_words = []
    subjects = []
    objects = []
    verbs = []
    others = []
    interrogatives = []
    
    has_past_verb = False
    has_future_verb = False
    
    is_question = '?' in text or '¿' in text
    question_words = ['qué', 'quién', 'quiénes', 'cuál', 'cuáles', 'dónde', 'cuándo', 'cómo', 'cuánto']
    
    for token in doc:
      if token.text in question_words:
        interrogatives.append(token.text)
        is_question = True
        continue
        
      if token.is_punct or token.is_space or token.pos_ in ['DET', 'ADP', 'CCONJ', 'PRON', 'SCONJ']:
        continue
        
      if token.pos_ in ['VERB', 'AUX']:
        tense = token.morph.get("Tense")
        if tense:
            if "Fut" in tense:
                has_future_verb = True
            elif "Past" in tense:
                has_past_verb = True
        
        verbs.append(token.lemma_)
        continue
      
      if token.dep_ == 'advmod' or token.dep_ == 'obl:tmod':
        time_words.append(token.text)
      elif 'subj' in token.dep_:
        subjects.append(token.text)
      elif 'obj' in token.dep_ or token.dep_ == 'obl':
        objects.append(token.text)
      else:
        others.append(token.text)
        
    if len(time_words) == 0:
        if has_future_verb:
            time_words.append("futuro")
        elif has_past_verb:
            time_words.append("pasado")
            
    ordered_sentence = time_words + subjects + others + objects + verbs
    
    if is_question and interrogatives:
        ordered_sentence.extend(interrogatives)
    
    return ordered_sentence