# -*- coding:utf-8 -*
import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
import math


def jstage_auto_search(this_csv_path, this_search_word):
    ''' jstageで保存するcsvのパス・名前と検索語を入力して
        seleniumによる自動検索、保存を行う'''

    def get_loop_number(browser)->int:
        '''検索ヒット数と位置ページ表示数から「次へ」を押す回数を設定'''
        # search wordでの検索件数の取得
        this_header = browser.find_element_by_class_name(
                'search-resultsinfo-leftsection')

        # 取得できたelementからヒット件数を取得する
        ## 空白で区切られている前半に'xx件数'が取得できる
        this_text = this_header.text.split()
        searchHitNum = int(this_text[0][:-2])

        return searchHitNum

    def get_article_info(browser,csvWriter):
        '''論文の情報の取得'''
        # 著者の情報を取得
        titles = browser.find_elements_by_class_name('searchlist-title')
        authors = browser.find_elements_by_class_name(
                'searchlist-authortags')
        additionalInfos = browser.find_elements_by_class_name(
                'searchlist-additional-info')
        dois = browser.find_elements_by_class_name(
                'result-doi-wrap')
                #'doi-icn')
        abst_links = browser.find_elements_by_class_name(
                #'inner-content')
                'lft')
        try:
            abst = abst_link.find_elements_by_class_name('inner-content\ abstract').text
        except:
            abst = "None"

        for title, author, additionalInfo, doi, abst_link in \
                zip(titles, authors, additionalInfos, dois, abst_links):

            res_title = title.text.strip()
            res_author = author.text.strip()
            res_additionalInfo = additionalInfo.text.strip()
            res_doi_link = doi.text.strip()

            #for i in [res_title, res_author, res_additionalInfo, res_doi_link]:
            #    i = i.encode('cp932','ignore').decode('cp932')

            resList = [ i.encode('cp932','ignore').decode('cp932') for i in
                [res_title, res_author, res_additionalInfo, res_doi_link] ]

            csvWriter.writerow(resList)

        return 


    # Open Chrome
    options = Options()
    options.add_argument('--headless')
    options.binary_location = '/usr/bin/google-chrome'
    browser = webdriver.Chrome(chrome_options = options)

    # Browse target URL
    target_URL = 'https://www.jstage.jst.go.jp/search/global/_search/-char/ja'
    browser.get(target_URL)

    # phase 1 : enter search word
    ## Enter Search Text
    search_word = this_search_word
    browser.find_element_by_id('EnterSearchTerm1').send_keys(
            search_word + '\n')

    # phase 2 : ページループの取得
    searchHitNum = get_loop_number(browser)
    loopNum = math.ceil(searchHitNum / 20)

    # 変数設定
    this_page = 0 # 表示ページ。0始まり
    total_index = 0 # 検索articleの通し番号。表示は1始まり

    with open(this_csv_path,"w",newline="\n") as f:
        csvWriter = csv.writer(f,lineterminator='\n')
        #csvWriter.writerow(["論文名","著者","追加情報","DOIリンク","抄録リンク"])
        csvWriter.writerow(["論文名","著者","追加情報","DOIリンク"])

        for i in range(0, loopNum):
            
            get_article_info(browser, csvWriter)
            
            # 進むボタンを押す
            if i != loopNum - 1:
                browser.find_element_by_link_text(">").click()

        browser.close()
        print("無事終了しました")

if __name__ == '__main__':

    # 検索ワード
    search_word = ''
    while search_word == '':
        search_word = input('J-stageで検索したい言葉を入力してください\n')


    saveFile = ''
    # ファイル名
    while saveFile == '':

        saveFile = input('保存するファイル名を入力して下さい(拡張子はcsv)\n')




    jstage_auto_search(this_csv_path = saveFile, 
            this_search_word = search_word)
