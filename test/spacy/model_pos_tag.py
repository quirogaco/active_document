import pprint
import math
import spacy
from spacy.lookups import load_lookups


nlp = spacy.load('en_core_web_lg')
lookups = load_lookups("en", ["lexeme_prob"])
nlp.vocab.lookups.add_table("lexeme_prob", lookups.get_table("lexeme_prob"))

model_tag_pos = "NOUNA NOUNB NOUNC NOUND ADJA"
doc_tag_pos = nlp(model_tag_pos)

value_tag_pos = [
    "NOUNA",
    "ADJA",
    "NOUNA ADJA",    
    "NOUNA NOUNB",
    "NOUNA ADJA NOUNB",
    "NOUNA NOUNB ADJA",
    "NOUNA NOUNB NOUNC ADJA",
    "NOUNA NOUNB NOUNC NOUND ADJA",    
    "NOUNA ADJA NOUNB NOUNC NOUND",
    "PROPNA NOUNA"
]

result = [
    {
        "similarity": round(doc_tag_pos.similarity( nlp(value) )*1000.0, 2), 
        "doc_tag_pos": doc_tag_pos,
        "value": value
    }
    for value in value_tag_pos
]

result = sorted(result, key=lambda x: x['similarity'], reverse=True)

for doc in result:
    print(doc['similarity'], doc['doc_tag_pos'], " -> ", doc['value'] )