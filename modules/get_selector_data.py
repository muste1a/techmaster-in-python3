# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

# detailページに入って授業名と成績評価方法をとってくる関数
def scraping_data(link):
    url = requests.get(link)
    soup = BeautifulSoup(url.content, 'html.parser')
    # 学科を取得する
    tbody = soup.select('tr')
    department = tbody[1].td.text

    # 授業名を取得する
    tbody = soup.select('tr')
    subject_name = tbody[0].td.text

    # 担当教員を取得する
    teacher_name = tbody[2].td.text


    # 成績評価方法を取得
    table= soup.select('table')
    table = table[1]

    try:
        #成績評価はエラーでるから例外処理してある
        subject_eval = table.select('tr')[7].td.text
        return (department, subject_name, teacher_name, subject_eval)
    except:
        return (department, subject_name, teacher_name, None)
