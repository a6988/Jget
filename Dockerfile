From python:3.8-buster

run apt update
# 日本語フォントのインストール
run apt install -y unzip git fonts-takao fonts-ipafont fonts-ipaexfont \
	& fc-cache -fv

# google-chromeのインストール
# NOTE! バージョンが現在(21/09/12)では93がインストールされるが将来変わる

run wget https://dl.google.com/linux/linux_signing_key.pub \
    & apt-key add linux_signing_key.pub \
	& echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | sudo tee /etc/apt/sources.list.d/google-chrome.list \
	& sudo apt-get update \
	& sudo apt-get install google-chrome-stable

# chromedriverのインストール
# note! google-chromeとのバージョン違いが将来発生する
run wget https://chromedriver.storage.googleapis.com/93.0.4577.63/chromedriver_linux64.zip \
	& unzip chromedriver_linux64.zip \
	& mv chromedriver /usr/local/bin

# seleniumのインストール
run pip install seleinum

# 本J-stageダウンロードツールの取得
run git clone
