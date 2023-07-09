import nltk
import random
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.tag import pos_tag
import record
import alarm

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

def preprocess(sentence):
    lemmatizer = WordNetLemmatizer()
    tokens = word_tokenize(sentence)
    tags = pos_tag(tokens)
    processed = []
    for word, tag in tags:
        if tag.startswith('NN'):
            processed.append(lemmatizer.lemmatize(word, pos='n'))
        elif tag.startswith('VB'):
            processed.append(lemmatizer.lemmatize(word, pos='v'))
        elif tag.startswith('JJ'):
            processed.append(lemmatizer.lemmatize(word, pos='a'))
        elif tag.startswith('R'):
            processed.append(lemmatizer.lemmatize(word, pos='r'))
        else:
            processed.append(word)
    return ' '.join(processed)

from nltk.corpus import wordnet
from nltk.tokenize import sent_tokenize

def generate_response(sentence):
    sentence = preprocess(sentence)
    tokens = word_tokenize(sentence)
    for token in tokens:
        synsets = wordnet.synsets(token)
        if synsets:
            definition = synsets[0].definition()
            example = synsets[0].examples()
            if example:
                return definition + ' ' + example[0]
            else:
                return definition
    return None
import random

def quiz():
    synset = random.choice(list(wordnet.all_synsets()))
    word = synset.name().split('.')[0]
    definition = synset.definition()
    print(f"Definition: {definition}")
    while True:
        answer = input(f"What is the word for '{definition}'? (Type 'quit' to exit) ").strip().lower()
        if answer == 'quit':
            return None, None
        elif answer == word.lower():
            print("Correct!")
            synset = random.choice(list(wordnet.all_synsets()))
            word = synset.name().split('.')[0]
            definition = synset.definition()
            print(f"Definition: {definition}")
        else:
            print(f"Sorry, the answer was {word}")
            word = synset.lemmas()[0].name()
            return definition, word


print("Hello! I'm a chatbot. What can I help you with today?")
while True:
    user_input = input('> ')
    if user_input.lower() in ['bye', 'goodbye', 'exit']:
        print("Goodbye!")
        break
    elif user_input.lower() == 'quiz':
        question, answer = quiz()
        if question is not None:
            print(question)
            while True:
                user_answer = input('> ')
                if user_answer.lower() == answer.lower():
                    print("Correct!")
                    break
                else:
                    print("Incorrect, try again.")
    else:
        response = generate_response(user_input)
        if response:
            print(response)
        else:
            print("I'm sorry, I don't understand.")
