import spacy
nlp = spacy.load('pt_core_news_sm')
print('Digite uma frase')
frase = input()
doc = nlp(frase)
print([(w.text, w.pos_) for w in doc])

#print ([(w.text) for w in doc])
#print ([(w.pos_) for w in doc])

for w in doc:
    if (w.pos_ == 'VERB'):
        print ("Palavra: " + w.text + " Tipo: " + w.pos_)
        