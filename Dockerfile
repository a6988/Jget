From python:3.6

run apt update
# 日本語フォントのインストール
run apt install -y unzip git fonts-takao fonts-ipafont fonts-ipaexfont \
	& fc-cache -fv

# google-chromeのインストール
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
run	apt-get update
run apt-get install -y google-chrome-stable

# chromedriverのインストール
WORKDIR /home
RUN wget -O chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip 
RUN	unzip chromedriver.zip \
	& mv chromedriver /usr/local/bin

# seleniumのインストール
run apt install -y python3-selenium
run pip install -U pip
run pip install -U selenium

# 本J-stageダウンロードツールの取得
run git clone https://github.com/a6988/Jget.git Jget

# 実行
#ENTRYPOINT python Jget/Jstage_get.py
