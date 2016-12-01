#!/usr/bin/python

import xml.sax
import time
start_time = time.time()
import sys
from collections import defaultdict
import nltk
import pickle
global dtn
# dtn = {}
global adjectives 
adjectives = []
#global all_sentence
all_sentence = {}

def processing(content, id,):
	temp = content.strip()
	if temp == "":
		return
	#print temp		
	#print content	
	global dtn
	global adjectives
	# global all_sentence
	temp_dict = {}
	
	sentnc_list = []
	sentnc_list_NN = []
	sentnc_list_JJ = []

	# Get the id and sentence content
	sentence_info = []	#['id','content']
	sentence_info.append(id)
	
	 
	sentence_info.append(content.strip())
	#print sentence_info[0]
	# print content.strip()
	x  = sentence_info[1]
	#print str(x)
	

	temp_dict[id]=content.strip()
	
	#print all_sentence
	all_sentence.update(temp_dict)
	#print all_sentence

	# print sentence_info[0]

	#print "--->", content
	#all_sentence.append(sentence_info)	#[['id1','content1'],['id2','content2']...]
	sentence_info = []

	tokenized = nltk.word_tokenize(content)
	tagged_list = nltk.pos_tag(tokenized)
	#print tagged_list

	# get all the nous in a sentence and their corresponding adjective
	for entry in tagged_list:
		if "JJ" in entry:
			sentnc_list_JJ.append(entry[0])
		elif "NN" in entry or "NNS" in entry or "NNP" in entry or "NNPS" in entry:
			sentnc_list_NN.append(entry[0])


	sentnc_list.append(sentnc_list_NN)
	sentnc_list.append(sentnc_list_JJ)

	# returns a list of nouns and adjectives in a sentence
	# it is a list of lists -> 1st list: nouns, 2nd list: adjectives
	adjectives.append(sentnc_list)

class DocHandler( xml.sax.ContentHandler ):
	def __init__(self):
		self.CurrentData = ""
		self.count = 0
		self.id = 0
		#self.all_sentence = {}

	# Call when an element starts
	def startElement(self, tag, attributes):
		self.CurrentData = tag
		if tag == "sentence":
			self.count += 1
			self.id = attributes["id"]
			# print self.id

	# Call when an elements ends
	def endElement(self, tag):
		pass
	# Call when a character is read
	def characters(self, content):
	    if self.CurrentData == "text":
	    	data_len = len(content)
		if "\n" in content : # or data_len == 8:
			pass
		else :
			processing(content, self.id)

def getAspectTermsDict(fileName):
	# create an XMLReader
	parser = xml.sax.make_parser()# turn off namepsaces
	parser.setFeature(xml.sax.handler.feature_namespaces, 0)
	# override the default ContextHandler
	Handler = DocHandler()
	parser.setContentHandler(Handler)
	parser.parse(fileName)
	# print "\n\n\n"
	# print dtn
	# print len(dtn)
	# print("--- %s seconds ---" % (time.time() - start_time))
	fp = open('parser_adjectives.txt','w')
	for each_adjective in adjectives:
		fp.write(str(each_adjective) + '\n')
	fp.close()
	
	return adjectives

def getSentences(fileName):
	global all_sentence
	# parses and returns all the sentences
	parser = xml.sax.make_parser()# turn off namepsaces
	parser.setFeature(xml.sax.handler.feature_namespaces, 0)
	# override the default ContextHandler
	Handler = DocHandler()
	parser.setContentHandler(Handler)
	parser.parse(fileName)
	print all_sentence
	#fp = open('parser_sentences.txt','w')
	pickle.dump(all_sentence,open('parser_sentences.p','wb'))

	return all_sentence 

def main():
	x = getSentences(sys.argv[1])
	y = getAspectTermsDict(sys.argv[1])
	#print all_sentence
	#for each_sentence in all_sentence:
	#	print each_sentence
if __name__ == '__main__':
	main()

