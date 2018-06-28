# for changing the word everyday
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('firebase.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()

words_ref = db.collection(u'words')

totalNumber = words_ref.document(u'numberOfWords').get().to_dict().get(u'numberOfWords')

previousWord = words_ref.document(u'wordOfTheDay').get().to_dict().get(u'wordOfTheDay')

if previousWord == totalNumber:
    previousWord = -1

words_ref.document(u'wordOfTheDay').set({
    'wordOfTheDay': previousWord + 1
})
