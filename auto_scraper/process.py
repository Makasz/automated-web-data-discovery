import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import conlltags2tree, tree2conlltags, ne_chunk
import spacy
from pprint import pprint

ex = 'Golden Diner is a little spot in Two Bridges that serves modern diner classics. It’s worth planning lunch here a week in advance.'
ex = 'Troubled burger group Byron will launch a new brand concept and menu on November 21. The 53-strong restaurant chain, which launched 12 years ago to much fanfare, narrowly escaped collapse amid the casual dining crunch, but has come out fighting with a bold new strategy. As much as £15m will be invested in the brand […]'

def preprocess(sent):
    sent = nltk.word_tokenize(sent)
    sent = nltk.pos_tag(sent)
    return sent

sent = preprocess(ex)
# print(sent)

pattern = 'NP: {<DT>?<JJ>*<NN>}'
cp = nltk.RegexpParser(pattern)
cs = cp.parse(sent)

iob_tagged = tree2conlltags(cs)
pprint(iob_tagged)

ne_tree = ne_chunk(pos_tag(word_tokenize(ex)))
print(ne_tree)
