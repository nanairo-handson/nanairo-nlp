# nanairo-nlp
NANAIRO HANDS-ON NLP TOOL

## HOW TO SETUP
1. JUMAN, KNPをインストールする(インストーラーを利用する)
1. pyknpをインストールする(ディレクトリ内で`python setup.py install`)
1. jmespath.pyをインストールする(ディレクトリ内で`python setup.py install`)
1. botocoreをインストールする(ディレクトリ内で`python setup.py install`)
1. s3transferをインストールする(ディレクトリ内で`python setup.py install`)
1. boto3をインストールする(ディレクトリ内で`python setup.py install`)
1. smart_openをインストールする(ディレクトリ内で`python setup.py install`)
1. gensimをインストールする(ディレクトリ内で`python setup.py install`)
1. test.pyが動くかを試す。
1. analyze.pyでLDAとTFIDF分析を実行する

## test.pyが動作するかを試す
1. `test`フォルダに`sample_data.csv`と命名しなおしたテストデータを入れる
1. `python test.py`をコマンドラインで実行する
1. 実行結果が表示されればOK!

## analyze.pyで実行する
1. `input`フォルダに`dataset.csv`と命名したデータセットを入れる
1. `python analyze.py`をコマンドラインで実行する
1. 実行結果を`output`フォルダ内で確認する

## もし動かない場合
* `test.py`もしくは`analyze.py`のファイル読み込みパス設定が違っている可能性がある
* その場合には適宜パスを書き換えて下さい
