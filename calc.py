from __future__ import division
import pickle

my_algo=pickle.load(open('polarities.p', 'rb'))
actual = pickle.load(open('actual_id_aspects_pol_dump.p', 'rb'))


total_aspect = 0
aspect_recalled = 0
aspect_precised = 0
polarity_precision  = 0

for key in actual.keys():
	temp_algo = my_algo[key]
	temp_actual = actual[key]
	
	for key1 in temp_actual.keys():
		total_aspect = total_aspect + 1
		if key1 in temp_algo.keys() : 
			aspect_precised = aspect_precised + 1
			#recall = recall + 1
			if temp_algo[key1] == temp_actual[key1] :
				polarity_precision = polarity_precision + 1
			
				#print precision
		
		#print total_aspect

	for key1 in temp_algo.keys():
		aspect_recalled = aspect_recalled + 1


print total_aspect,aspect_recalled,aspect_precised,polarity_precision
		
		#print final_precision
print total_aspect,aspect_recalled / total_aspect , aspect_precised / total_aspect , polarity_precision / aspect_precised
#print final_recall , total_aspect , final_precision_r		
#print aspect_recalled/total_aspect, final_recall / total_aspect , final_precision_r/total_aspect			