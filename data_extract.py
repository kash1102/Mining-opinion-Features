import json
import pickle
import xml.sax
import os
import sys
import re

input_file=open('apyori_aspect.json', 'r')
sentence=pickle.load(open('sentence_dump.p','rb'))
all_sentence = pickle.load(open('parser_sentences.p','rb'))
#output_file=open('test.json', 'w')
#json_decode=json.load(input_file)
aspects = []
tweets = []
for line in input_file:
    tweets.append(json.loads(line))
#print tweets[25]['items'][1]
for line in tweets:
	terms = line['items']
	term = ""
	for i in terms:
		term = term+ i+ " "
	term=term.strip()
	#print term
	aspects.append(term)
#print aspects
#print aspects[600]
input_file.close()

text=[]      # all the text sentences.
sentence_dict = {}
txt = open('Restaurants_Train_v2.xml', 'r')
#txt = open('absa-test_new.xml', 'r')
sent=[]
for line in txt:
	if '<sentence id' in line:
		#print '\n'+line	
		#print "going to sent:",line
		#print line
		line = line.strip()
		#print line
		sent.append(line)
txt = open('Restaurants_Train_v2.xml', 'r')

for line in txt:
	if '<text>' in line:
		#print line
		line = line.replace('</text>', '')
		line = line.replace('<text>','')
		line = line.replace('pound', 'kilo')
		line = line.replace('#','')
		#print "going to text::",line
		line=line.strip()
		text.append(line)
#print text

for word in aspects:
	list_of_words = word.split(' ')
	#print list_of_words
	if(len(list_of_words) > 1):
		count = 0
		m_sentence = 0
		temp = []
		for value in text:
			#print value
			value = value.replace('.','')
			
			temp = value.split(' ')
			#print temp
			index = []
			for w in list_of_words:
				if w in temp:
					#print w
					#print temp.index(w)
					index.append(temp.index(w))
			
			if(len(index) == 2 and len(list_of_words)==2):
				
				index1 = index[0]
				index2 = index[1]
				m_sentence = m_sentence + 1
				if(abs(index2-index1) <= 3 ):
					count = count+1
				#else:
					#print word
					#print temp		

			if(len(index) == 3 and len(list_of_words) == 3):
				#print temp
				#print index
				index1 = index[0]
				index2 = index[1]
				index3 = index[2]
				m_sentence = m_sentence + 1
				if(abs(index2-index1) <=3 and abs(index3-index2) <= 3 ):
					count = count + 1

		if(count < 2 and m_sentence > 2):
			#print word
			#print temp
			aspects = filter(lambda z: z != word, aspects)

	else:
		psupport = 0
		for value in text:
			value = value.replace('.','')
			flag=0
			if word in value:
				#temp = [s for s in features if word in s and s != word]
				for s in aspects:
					if word in s and s != word:
						if s in value:
							flag=0
							break
						else:
							flag=1
							break
				if flag==1:
					psupport = psupport + 1

		if psupport < 3:
			#print word
			aspects = filter(lambda z: z != word, aspects)

aspects = filter(lambda z: z != "", aspects)
#print aspects
aspect_dict={}
for sid in all_sentence.keys():
	#print sid,all_sentence[sid]
	all_sentence[sid] = all_sentence[sid].replace('.','')
	for asp in aspects:
		#asp = asp + " "
		if '-' in all_sentence[sid]:
			#print all_sentence[sid]
			all_sentence[sid] = all_sentence[sid].replace('-','')
		tmp_asp = r'\b' + asp + r'\b'
		#print tmp_asp,all_sentence[sid]
		regex = re.compile(tmp_asp)
		if bool(regex.search(all_sentence[sid])):
			#print asp," ",all_sentence[sid]
			if sid in aspect_dict:
				aspect_dict[sid].append(asp.strip())
			else:
				temp = []
				#print asp
				temp.append(asp.strip())
				aspect_dict[sid]=temp
				#print aspect_dict
for sid in all_sentence.keys():
	if sid in aspect_dict.keys():
		print " "
	else:
		temp = []
		aspect_dict[sid]=temp

pickle.dump(aspect_dict,open('final_aspect_dump.p','wb'))
print aspect_dict['2311']
#    print sid
#    print sentence[sid]
            #subNoun = isNounSubject(sentence[sid])
        #aspects=extractor(sentence[sid], sid)
    #print "asp:",sid, " ",aspects
        #asdict[sid]=aspects
#print forpol
    #aspectdict=dict((x[0],(x[1:])) for x in forpol[0:])
    #print "asd",asdict
    #
    #pickle.dump(asdict,open('aspect_dump_new.p','wb'))