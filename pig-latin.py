# GET SENTENCE FROM USER
sentence = input('Please provide a sentence to convert: ').strip().lower()

# SPLIT SENTENCE INTO WORDS
words = sentence.split()

# LOOP THROUGH WORDS AND CONVERT THEM INTO PIG-LATIN
new_words = []

## if starts with a vowel, just add "yay"
for word in words:
	if word[0] in 'aeiou':
		new_words.append(word + 'yay')

	## otherwise move the first consonant to end and add 'ay'
	else: 
		temp_word = ''

		for i in range(0, len(word)) :

			if word[i] not in 'aeiou':
				
				temp_word = temp_word + word[i]

			else:

				new_words.append(word[i:] + temp_word + 'ay')
				break

# STICK THE WORDS BACK TOGETHER INTO SENTENCE
new_string = ' '.join(new_words)

# OUTPUT THE FINAL STRING
print(new_string)