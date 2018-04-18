import pt_core_news_sm
nlp = pt_core_news_sm.load()
print('Digite uma frase')
frase = input()
doc = nlp(frase)
print([(w.text, w.pos_) for w in doc])
print(doc[1])
