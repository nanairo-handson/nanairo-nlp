# テストデータをロードする

import pandas as pd
import codecs as cd
import pyknp as pk

def main():
    with cd.open("./test/sample_data.csv", "r", "Shift-JIS", "ignore") as file:
        df = pd.read_table(file,header=None)
        juman = pk.Juman(jumanpp=False)
        result = juman.analysis(df[0][0])
        for morph in result.mrph_list():
            if morph.hinsi in ['名詞','動詞','形容詞','形容動詞']:
                print("見出し:{0}, 品詞:{1} 原型:{2}".format(morph.midasi,morph.hinsi,morph.genkei))

# main関数呼び出し
if __name__ == "__main__":
    main()

