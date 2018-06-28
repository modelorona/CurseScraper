import firebase_admin
import random
from firebase_admin import credentials
from firebase_admin import firestore
import noswearing_parser

cred = None
words_ref = None
index = 0


# save the key with its value
def save(key, value):
    global index
    words_ref.document(str(index)).set({
        key: value
    })
    index += 1


def save_other(key, value):
    words_ref.document(key).set({
        key: value
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

    # finally save the amount of words read in
    save_other('numberOfWords', index)

    print("The End")
