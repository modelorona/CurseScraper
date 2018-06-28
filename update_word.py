# for changing the word everyday
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('firebase.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()

# make a reference to the collection
words_ref = db.collection(u'words')

# see the total amount of words
totalNumber = words_ref.document(u'numberOfWords').get().to_dict().get(u'numberOfWords')

# get the counter
counter = words_ref.document(u'wordOfTheDayCounter').get().to_dict().get(u'wordOfTheDayCounter')

# check to see if the counter is over the limit
if counter == totalNumber:
    counter = -1

# now get the word that the counter is pointing to in the form { word : definition }
word_dict = words_ref.document(str(counter)).get().to_dict()

# now separate the dictionary. there will always be one pair. no more. no less.
word = None
definition = None
for key, value in word_dict.items():
    word = key
    definition = value

# now save the word and its definition into a separate entry in the database. this is to prevent the app from making more than 1 call
words_ref.document(u'wordOfTheDay').set({
    'word': word,
    'definition': definition
})

# finally update the counter to point to the new word for the following day
words_ref.document(u'wordOfTheDayCounter').set({
    'wordOfTheDayCounter': counter + 1
})
