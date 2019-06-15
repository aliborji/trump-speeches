# Trump's speeches here: https://github.com/ryanmcdermott/trump-speeches
import numpy as np
import sys

n_words = 100

def remove_punc(input_str):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~–’'''
    no_punct = ""
    for char in input_str:
        if char not in punctuations:
            no_punct = no_punct + char

    return no_punct

def make_prefix(corpus, n):
    for i in range(len(corpus) - n - 1):
        yield (corpus[i:i + n], corpus[i + n + 1])

def generate_text(corpus, n, m):
    prefixes = make_prefix(corpus, n)

    word_dict = {}
    for prefix, suffix in prefixes:
        prefix = ' '.join(prefix)
        if prefix in word_dict.keys():
            word_dict[prefix].append(suffix)
        else:
            word_dict[prefix] = [suffix]

    sentences = []
    for k in range(m):
        idx = np.random.randint(len(corpus) - n - 1)

        first_n_words = []
        for i in range(n):
            first_n_words.append(corpus[idx + i])

        chain = first_n_words
        for i in range(n_words):
            ss = ' '.join(chain[-2:])
            # import ipdb; ipdb.set_trace()
            d = word_dict.get(ss, [])
            if d:
                chain.append(np.random.choice(d))

        sentence = ' '.join(chain)
        sentences.append(sentence)

    return sentences

    # TODO
    # print('number of unique prefix phrases', str(14))

if __name__ == "__main__":
    input_file = sys.argv[1]
    length = sys.argv[2]
    num_sentences = sys.argv[3]

    my_text = open(input_file, encoding='utf8').read()
    corpus = my_text.split()
    corpus_new = []

    for i in range(len(corpus)):
        corpus_new.append(remove_punc(corpus[i]))

    del corpus
    sentences = generate_text(corpus_new, int(length), int(num_sentences))
    for j in sentences:
        print(j + '.')