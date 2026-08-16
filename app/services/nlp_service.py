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
    
    is_question = '?' in text or '¿' in text

    question_words = ['qué', 'quién', 'quiénes', 'cuál', 'cuáles', 'dónde', 'cuándo', 'cómo', 'cuánto']
    
    for token in doc:
      if token.is_punct or token.is_space or token.pos_ in ['DET', 'ADP', 'CCONJ']:
        continue
        
      if token.text in question_words:
        word = token.text
      else:
        word = token.lemma_ if token.pos_ in ['VERB', 'AUX'] else token.text
      
      if word in question_words:
        interrogatives.append(word)
        is_question = True
      elif token.dep_ == 'advmod' or token.dep_ == 'obl:tmod':
        time_words.append(word)
      elif 'subj' in token.dep_:
        subjects.append(word)
      elif 'obj' in token.dep_ or token.dep_ == 'obl':
        objects.append(word)
      elif token.pos_ in ['VERB', 'AUX']:
        verbs.append(word)
      else:
        others.append(word)
        
    ordered_sentence = time_words + subjects + others + objects + verbs
    
    if is_question and interrogatives:
        ordered_sentence.extend(interrogatives)
    
    return ordered_sentence