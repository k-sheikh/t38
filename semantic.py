# Compulsory Task 1

import spacy

nlp = spacy.load('en_core_web_md')

# Snippet 1
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# Cat and monkey are animals, so makes sense it would have a higher similarity
# Monkeys eat bananas, cats don't eat fruit
# It would make sense that a monkey would have a higher similarity with fruit

word4 = nlp("gorilla")
word5 = nlp("cow")
word6 = nlp("bull")

print(word4.similarity(word2))
print(word5.similarity(word6))
print(word4.similarity(word3))

# Monkey and gorilla are extremely similar
# Cow and bull aren't as similar as I thought they'd be
# Gorilla and banana, same similarity as monkey and banana


# ANALYSIS OF EXAMPLE.PY
# When running the 'example.py' file with the 'en_core_web_sm' model, the similarity
# was significantly lower than when I ran it with the original 'en_core_web_md' model
# The 'md' model is clearly a more advanced model