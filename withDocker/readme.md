# pythonによるJ-Stage巡回の自動化(docker使用)

## 必要なもの

* dockerを使えるように準備
* `pip install selenium`
* google chromeのインストールやバージョン確認は必要ない

## 実行方法

1. dockerコンテナの起動

	* `selenium/standalone`のイメージを取得、起動

		* `docker run -d -p 4444:4444 --shm-size="2g" selenium/standalone-chrome:4.0.0-rc-2-prerelease-20210908`

1. プログラムを実行

	* `python Jstage_getDocker.py`

