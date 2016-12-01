import pickle
sentence=pickle.load(open('sentence_dump.p','rb'))
all_sentence = pickle.load(open('parser_sentences.p','rb'))
aspect=pickle.load(open('final_aspect_dump.p', 'rb'))
#print all_sentence
print sentence['2311']
#for sid in aspect.keys():
#	if 'fish' in aspect[sid]:
#		print all_sentence[sid]