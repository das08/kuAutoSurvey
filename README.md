# kuAutoSurvey

kuAutoSurvey is a survey automation tool for Kyodai.

## Description

京大の授業アンケートを自動化します。本ツールを実行し、自動回答を行いたい講義番号を入力すると最終確定画面まで自動で回答します。

***DEMO:***
```bash
$ python main.py

講義名:地域地理学 -> 1
講義名:線形代数学 -> 2
講義名:Logic-E2 -> 3
講義名:iPS研究概論 -> 4
...

Type in ID (02 for 2): 

```
![Demo](/img/submit.png)

## Features

- Auto survey completion


## Requirement

- Python 3 or more


- selenium 3.141.0
- chromedriver_binary 79.0


## Installation

```bash
pip install selenium
pip install chromedriver_binary
```

＊Google Chromeとchromedriver_binaryのバージョンが一致するように適宜アップ・ダウングレードしてください。



