# kuAutoSurvey

kuAutoSurvey is a survey automation tool for Kyodai.

## Description

京大の授業アンケートの回答を自動化します。本ツールを実行し、自動回答を行いたい講義番号を入力すると最終確定画面まで自動で回答します。

***DEMO:***
```
$ python main.py

講義名:地域地理学 -> 1
講義名:線形代数学 -> 2
講義名:Logic-E2 -> 3
講義名:iPS研究概論 -> 4
...

Type in ID (02 for 2): 

```
↓実行後最終画面↓
![Demo](/img/submit.png)
コメントアウトを解除することで完全自動にもできます。

## Features

- Auto survey completion
For only 16question-survey for now.

## Requirement

- Python 3 or more


- selenium 3.141.0
- chromedriver_binary 79.0


## How to use
1. Install required libraries
```bash
pip install selenium
pip install chromedriver_binary
pip install dotenv (optional)
```

＊Google Chromeとchromedriver_binaryのバージョンが一致するように適宜アップ・ダウングレードしてください。

2. Preparing .env file

setting.pyで.envファイルからECS-IDとpasswordを読み込みます。.envファイルを作成し、以下のように記述してください。
面倒ならソースコードにべた書きしてください。
```
ID   = a0000000
PASS = *************
```

3. Run
```
$ python main.py
```

なお、本ツールは自己責任で使用してください。
