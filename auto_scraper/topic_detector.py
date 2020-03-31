from nltk.corpus import stopwords
import csv


NUM_TOPICS = 10

data = []
new_file = open('auto_scraper/results/resuluts_balanced.csv', 'r', encoding='utf8', newline='')
reader = csv.reader(new_file, delimiter='|')
for line in reader:
    data.append(line[-1].replace('\n', ''))

stop_words = stopwords.words('english')
stop_words.extend(['come', 'order', 'try', 'go', 'get', 'make', 'drink', 'plate', 'dish', 'restaurant', 'place',
                   'would', 'really', 'like', 'great', 'service', 'came', 'got'])


def remove_stopwords(texts):
    return [[word for word in simple_preprocess(str(doc)) if word not in stop_words] for doc in texts]


def bigrams(words, bi_min=15, tri_min=10):
    bigram = gensim.models.Phrases(words, min_count=bi_min)
    bigram_mod = gensim.models.phrases.Phraser(bigram)
    return bigram_mod


def get_corpus(df):
    df['text'] = strip_newline(df.text)
    words = list(sent_to_words(df.text))
    words = remove_stopwords(words)
    bigram_mod = bigrams(words)
    bigram = [bigram_mod[review] for review in words]
    id2word = gensim.corpora.Dictionary(bigram)
    id2word.filter_extremes(no_below=10, no_above=0.35)
    id2word.compactify()
    corpus = [id2word.doc2bow(text) for text in bigram]
    return corpus, id2word, bigram


train_corpus, train_id2word, bigram_train = get_corpus(rev_train)

print("LDA Model:")
print_topics(lda_model, vectorizer)
print("=" * 20)

print("NMF Model:")
print_topics(nmf_model, vectorizer)
print("=" * 20)

print("LSI Model:")
print_topics(lsi_model, vectorizer)
print("=" * 20)

text = "The economy is working better than ever"
x = nmf_model.transform(vectorizer.transform([text]))[0]
print(x)