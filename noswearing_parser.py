# this is to download all the swear words from https://www.noswearing.com/dictionary. this will be the starting

from bs4 import BeautifulSoup
from requests import get
import string

base_url = 'https://www.noswearing.com/dictionary/'
letters = string.ascii_lowercase


def get_words():
    words = dict()
    for letter in letters:
        # get the html for each page
        # go through each link
        # save it
        page = get(base_url + letter).content
        soup = BeautifulSoup(page, 'html.parser')

        b_tags = soup.find_all('b')

        # letter a skips first 5 <a> tags, letters b and after skip 4 <a> tags, all of them go up to the 2nd to last <a> tag
        b_tags = b_tags[5:-1] if letter == 'a' else b_tags[4:-1]
        # since the word definition isn't in a tag but is right after its respective <b> tag, we can get it using bs4 next_sibling
        word_definitions = [b.next_sibling.replace('-', '').strip(' ') for b in b_tags]

        for index, t in enumerate(b_tags):
            current_word = t.text.replace(' ', '')
            # if the current word is not already in the dictionary, add it to it
            if words.get(current_word) is None:
                words[current_word] = word_definitions[index]
    return words


# if __name__ == '__main__':
#     print(get_words())
