import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import noswearing_parser

cred = None
words_ref = None


# save the word with its definition
def save(w, d):
    words_ref.document().set({
        w: d
    })


if __name__ == '__main__':
    # init firebase and firestore
    cred = credentials.Certificate('firebase.json')
    app = firebase_admin.initialize_app(cred)
    db = firestore.client()

    # reference to the words collection
    words_ref = db.collection(u'words')

    # now begin scraping the noswearing site
    words = noswearing_parser.get_words()
    for word, definition in words.items():
        save(word, definition)

    print("The End")
