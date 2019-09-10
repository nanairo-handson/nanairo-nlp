# 形態素解析を行いLDAでトピックモデルを構成する。

import pandas as pd
import codecs as cd
import pyknp as pk
import gensim as gs
import collections as cl
import datetime as dt

def main():
    with cd.open("./input/dataset.csv", "r", "Shift-JIS", "ignore") as file:
        df = pd.read_table(file,header=None)
    juman = pk.Juman(jumanpp=False)
    morph_df = []
    for i in range(len(df)):
        morph_df.append([morph.genkei for morph in juman.analysis(df[0][i]).mrph_list() if morph.hinsi in ['動詞','形容詞','名詞']])
    freq_morph = cl.defaultdict(int)
    for one_morph in morph_df:
        for token in one_morph:
            freq_morph[token] += 1
    texts = [[token for token in text if freq_morph[token] > 1] for text in morph_df]
    nowdt = dt.datetime.today().strftime("%Y%m%d%H%M")
    dictionary = gs.corpora.Dictionary(texts)
    dictionary.save_as_text('./output/result_sum_'+nowdt+'.txt')
    corpus = [dictionary.doc2bow(text) for text in texts]
    lda = gs.models.LdaModel(corpus=corpus, id2word=dictionary, num_topics=5, minimum_probability=0.001, passes=20, update_every=0, chunksize=10000)
    print('=================  LDA RESULTS  =================')
    print('=================  TOPIC STATS  =================')
    for one_topic in lda.show_topics():
        print('topic '+str(one_topic[0])+' : '+one_topic[1])
    print('=================PREDICTED TOPIC=================')
    tfidf = gs.models.TfidfModel(corpus)
    tpds = []
    for tpd in lda[corpus]:
        tpds.append(tpd)
        print(tpd)
    pd.DataFrame(tpds).to_csv('./output/result_topic_'+nowdt+'.csv')
    print('================= TFIDF RESULTS =================')
    print('=================TFIDF CALCULATE=================')
    texts_tfidf = []
    for doc in tfidf[corpus]:
        text_tfidf = []
        for word in doc:
            text_tfidf.append([dictionary[word[0]],word[1]])
        texts_tfidf.append(text_tfidf)
    for text in texts_tfidf:
        print(text)
    pd.DataFrame(texts_tfidf).to_csv('./output/result_tfidf_'+nowdt+'.csv')
# main関数呼び出し
if __name__ == "__main__":
    main()

