# encoding: utf-8
import os
import dbhelper
from flask import Flask, render_template, session

from model.movie import movie_blu
from model.movie_info import movie_info_blu

app = Flask(__name__)
app.config["SECRET_KEY"] = os.urandom(24)

app.register_blueprint(movie_blu)
app.register_blueprint(movie_info_blu)


@app.route('/', methods=["GET", "POST"])
def index():
    """
    主页函数，显示全部电影
    :return: 主页信息和问题参数
    """
    context = {
        'movies': dbhelper.fetch_all_movies()
    }
    return render_template('index.html', **context)


@app.route('/firstpage', methods=["GET", "POST"])
def firstpage():
    """
    首页函数，显示网页主页
    :return: 返回首页网页
    """
    return render_template('firstpage.html')

'''
# 钩子函数(注销)
@app.context_processor
def my_context_processor():
    """
    定义钩子函数，各页面间传递movie信息
    :return: 电影信息
    """
    movie_id = session.get('movie_id')
    if movie_id:
        movie = dbhelper.fetch_movie_by_id(movie_id)
        if movie:
            if movie.get("MovieStatus") == '2':
                session.clear()
                return {}
            return {'movie': movie}
    return {}
'''

if __name__ == '__main__':
    '''
    from werkzeug.contrib.fixers import ProxyFix
    app.wsgi_app = ProxyFix(app.wsgi_app)
    '''
    app.run(debug=True)
