import spacy
nlp = spacy.load('pt')
print('Digite uma frase')
frase = input()
doc = nlp(frase)
print([(w.text, w.pos_) for w in doc])
print(doc[1])
