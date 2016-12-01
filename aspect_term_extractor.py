import sys
from sys import exit
import pickle
import xml.sax
from apyori import apriori


sentic=pickle.load(open('sentic_dump.p','rb'))
sentence=pickle.load(open('sentence_dump.p','rb'))
#polarity_dict=pickle.load(open('polarities.p','rb'))
f = open('aspect.txt','a')


point1 = ["VBD", "VB", "VBG", "VBN","VBP", "VBZ", "JJ", "JJR", "JJS", "RB", "RBR", "RBS"]
point2 = ["JJ", "JJR", "JJS", "RB", "RBR", "RBS"]
verb = ["VBD", "VB", "VBG", "VBN","VBP", "VBZ"]
noun = ["NN", "NNS", "NNP", "NNPS"]
adverb =["RB", "RBR", "RBS"]
adjective = ["JJ", "JJR", "JJS"]
auxiliary_verb = ["be" , "am" , "are", "is", "was", "being", "can", "could", "do", "did", "does", "doing", "have", "had",
         "has", "having", "may", "might", "might", "must", "shall", "should", "will", "'ve", "n't", "were"]
asdict={}
forpol=[]

def extractor(words = {}, sid=0):
    pol=[sid]
    aspect_terms=[]
        #has_auiliary = set(words.keys()).intersection(auxiliary_verb)
        
    for word in words.keys():
                    #if words[word].has_key("nsubj"):
                    #Point 1
        if (words[word]["pos_tag"] in noun ):
            print "In 1"
            print word
            f.write(word)
            f.write("\t")
            aspect_terms.append(word)
    pol.append(word)
    f.write("\n")
                    
                        #Point 3
    
              
    print pol
    print aspect_terms 
             
    forpol.append(pol)
    pol=[]
    return aspect_terms


if __name__ == "__main__":
    #words = {}
#    words = {"word" : {"pos_tag" : "verb"},}   
    # Myaspect=extractor({u'and': {'pos_tag': u'CC'}, u'atmosphere': {'pos_tag': u'NN', u'advmod': u'pretty', u'det': u'a'}, u'it': {'pos_tag': u'PRP'}, u'an': {'pos_tag': u'DT'}, u'even': {'pos_tag': u'RB'}, u'$': {'pos_tag': u'$'}, u'service': {'pos_tag': u'NN', u'amod': u'excellent'}, u'make': {'pos_tag': u'VB', u'dobj': u'this', u'nsubj': u'food'}, u',': {'pos_tag': u','}, u'better': {'pos_tag': u'JJR', u'advmod': u'even'}, u'pretty': {'pos_tag': u'RB'}, u'!': {'pos_tag': u'.'}, u'5.99': {'pos_tag': u'CD'}, u'food': {'pos_tag': u'NN', u'conj_and': u'atmosphere', u'nn': u'Delicious'}, u'buffet': {'pos_tag': u'NN', u'dep': u'$', u'num': u'5.99', u'det': u'the', u'nn': u'lunch'}, u'choice': {'pos_tag': u'NN', u'prep_for': u'lunch', u'nsubj': u'it', u'det': u'an', u'amod': u'better'}, u'lunch': {'pos_tag': u'NN'}, u'excellent': {'pos_tag': u'JJ'}, u'a': {'pos_tag': u'DT'}, u'great': {'pos_tag': u'JJ'}, u'for': {'pos_tag': u'IN'}, u'this': {'pos_tag': u'DT', u'rcmod': u'makes'}, u'dinner': {'pos_tag': u'NN', u'conj_and': u'buffet'}, u'Delicious': {'pos_tag': u'NNP'}, u'the': {'pos_tag': u'DT'}, u'makes': {'pos_tag': u'VBZ', u'xcomp': u'choice', u'nsubj': u'choice'}},"1398")
    # print Myaspect
    for sid in sentence.keys():
    #get words as dictionary #graph
        print sid
            #subNoun = isNounSubject(sentence[sid])
        aspects=extractor(sentence[sid], sid)
        print "asp:",sid, " ",aspects
        asdict[sid]=aspects
#print forpol

    aspectdict=dict((x[0],(x[1:])) for x in forpol[0:])
    print "asd",asdict
    pickle.dump(aspectdict,open('aspect_dump.p','wb'))
    pickle.dump(asdict,open('aspect_dump_new.p','wb'))
    f.close()
    
