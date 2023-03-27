import spacy  # importing spacy
nlp = spacy.load('en_core_web_sm') # specifying the model we want to use. 

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# Comparing a series to words
tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# Comparing sentences
sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)


#********* NOTES **********#
# I see that the model is able to identify words that refer to similar entities. Cat and Apple have a similarity of
# approximately 0.6 because they are both animals. Apple and banana have a similarity of approximately 0.7 because 
# they are both fruits. However, objects of different entities have a low similarity e.g apple and monkey
# More examples could be the comparison of airport, football and stadium. Airport and stadium will have a higher
# similarity as they are both facilities whereas airport and football will have have a low similarity as they are
# different entitities. Football and stadium are different entities but the similarity could be significant as they are
# somewhat related.

# When the file is run with the simpler en_core_web_sm, the word and sentence similarities produced makes no sense.
# For example, it gives monkey and banana a similarity of 0.4, and apple and monkey a similarity of 0.7. According to
# the user warning, this is because the model does not use preloaded word vectors.