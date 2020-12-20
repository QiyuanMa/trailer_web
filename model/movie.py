# encoding: utf-8

import time
from flask import Blueprint, request, render_template, session, url_for, redirect
import dbhelper

movie_blu = Blueprint('movie', __name__)


@movie_blu.route('/search/', methods=['GET', 'POST'])
def search():
    """
    关键词搜索函数，返回带关键词的所有电影
    :return:
    """
    if request.method == "GET":
        return render_template('index.html')
    else:
        search_key = request.form.get('search_key')
        # title, content
        # 或 查找方式（通过标题和内容来查找）
        movies = dbhelper.search_by_key(search_key)
        return render_template('index.html', movies=movies, search_key=search_key)
