import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import noswearing_parser

cred = None
words_ref = None
index = 0


# save the key with its value
def save(key, value):
    # todo: split this into a function to save words and a function to save numberOfWords
    global index
    if key == 'numberOfWords':
        words_ref.document(key).set({
            key: value
        })
    else:
        words_ref.document(str(index)).set({
            key: value
        })
    index += 1


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
    save('numberOfWords', index)

    print("The End")
