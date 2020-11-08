

import re

def most_common_words(text):
	punctuation_re = r'[.,;!\"\'\(\)]'
	sanitization = re.sub(punctuation_re,' ',text).lower()
	print(sanitization)


print(most_common_words("I am Vaibhavi."))