# Importing required packages
import re 	
from nltk.stem.snowball import SnowballStemmer 

# nltk library stemmer algorithm for English language
stem_eng = SnowballStemmer('english')

list_of_specialCharacters = ['  ',',','$','-','//','..',' / ',' \\ ','.']


def string_stemmer(s):
	stem_resultList = []
	for word in s.lower().split(): 
		stem_resultList.append(stem_eng.stem(word))
	return " ".join(stem_resultList)


def find_common_words(string1, string2): 
	count = 0
	for word in string1.split():
		if string2.find(word) >= 0:
			count += 1
	return count 


def freq_of_words(word, string, i):
    count = 0
    while i < len(string):
        i = string.find(word, i)
        if i == -1:
            break
        else:
            count += 1
            i += 1
    return count



def replace_extraChars(word):
	for char in list_of_specialCharacters:
		if char in word:
			if char == '//':
				word = word.replace(char,'/')
			elif char == '..':
				word = word.replace(char,' . ')
			elif char == '.':
				word = word.replace(char,' . ')
			else:
				word = word.replace(char, ' ')
	return word


def make_changes_to_query(word):
	x = re.search("([0-9]+)( *)\.?",word)

	if None != x:

		regex_term = 'inches|inch|in|\''
		if re.x(regex_term,word) is not None:
			word = re.sub(regex_term,"\1in. ", word)

		regex_term = 'foot|feet|ft|\'\''
		if re.x(regex_term,word) is not None:
			word = re.sub(regex_term,"\1ft. ", word)	

		regex_term = 'pounds|pound|lbs|lb'
		if re.x(regex_term,word) is not None:
			word = re.sub(regex_term,"\1lb. ", word)

		regex_term = '(square|sq) ?\.?(feet|foot|ft)'
		if re.x(regex_term,word) is not None:
			word = re.sub(regex_term,"\1sq.ft. ", word)

		regex_term = '(cubic|cu) ?\.?(feet|foot|ft)'
		if re.x(regex_term,word) is not None:
			word = re.sub(regex_term,"\1cu.ft. ", word)

		regex_term = 'gallons|gallon|gal'
		if re.x(regex_term,word) is not None:
			word = re.sub(regex_term,"\1gal. ", word)

		regex_term = 'ounces|ounce|oz'
		if re.x(regex_term,word) is not None:
			word = re.sub(regex_term,"\1oz. ", word)

		regex_term = 'centimeters|cm'
		if re.x(regex_term,word) is not None:
			word = re.sub(regex_term,"\1cm. ", word)

		regex_term = 'milimeters|mm'
		if re.x(regex_term,word) is not None:
			word = re.sub(regex_term,"\1mm. ", word)

		regex_term = 'degrees|degree'
		if re.x(regex_term,word) is not None:
			word = re.sub(regex_term,"\1deg. ", word)

		word = word.replace(" v "," volts ")
		regex_term = 'volts|volt'
		if re.x(regex_term,word) is not None:
			word = re.sub(regex_term,"\1volt. ", word)

		regex_term = 'watts|watt'
		if re.x(regex_term,word) is not None:
			word = re.sub(regex_term,"\1watt. ", word)

		regex_term = 'amperes|ampere|amps|amp'
		if re.x(regex_term,word) is not None:
			word = re.sub(regex_term,"\1amp. ", word)

	return word


def check_word_is_string(w):
	return isinstance(w,str)

def split_two_words(string):
	string = re.sub(r"(\w)\.([A-Z])", r"\1 \2", string)	
	string = string.lower()
	return string


def preprocess_word(word):
	temp = check_word_is_string(word)
	if temp == True:
		word = string_stemmer(word)
		word = split_two_words(word)
		word = replace_extraChars(word)
		word = make_changes_to_query(word)
	else:
		word =  "null"
	return word
