# encoding: utf-8

import time
from flask import Blueprint, render_template, request, url_for, session, redirect
import dbhelper
import json

movie_info_blu = Blueprint('movie_info', __name__)

'''
@movie_info_blu.route('/detail/<movie_id>/')
def trailer_detail(movie_id):
    """
    电影细节函数，返回问题，该电影的所有信息
    :param movie_id:
    :return:
    """
    trailer = dbhelper.fetch_trailer_info_by_movieid(movie_id)
    movie = dbhelper.fetch_movie_info_by_movieid(movie_id)
    #print(movie)
    return render_template('detail.html', movie=movie, trailer=trailer)
'''
@movie_info_blu.route('/detail/<movie_id>/')
def detail(movie_id):
    """
    电影细节函数，返回问题，该电影的所有信息
    :param movie_id:
    :return:
    """
    trailer = dbhelper.fetch_trailer_info_by_movieid(movie_id)
    movie = dbhelper.fetch_movie_info_by_movieid(movie_id)
    #print(movie)
    return render_template('detail.html', movie=movie, trailer=trailer)

@movie_info_blu.route('/movie_detail/<movie_id>/')
def movie_detail(movie_id):
    """
    电影细节函数，返回问题，该电影的所有信息
    :param movie_id:
    :return:
    """
    trailer = dbhelper.fetch_trailer_info_by_movieid(movie_id)
    movie = dbhelper.fetch_movie_info_by_movieid(movie_id)
    #print(movie)
    return render_template('movie_detail.html', trailer=trailer, movie=movie)

@movie_info_blu.route('/movie_income/<movie_id>/')
def movie_income(movie_id):
    """
    电影细节函数，返回问题，该电影的所有信息
    :param movie_id:
    :return:
    """
    trailer = dbhelper.fetch_trailer_info_by_movieid(movie_id)
    movie = dbhelper.fetch_movie_info_by_movieid(movie_id)
    #print(movie)
    return render_template('movie_income.html', trailer=trailer, movie=movie)

@movie_info_blu.route('/movie_AI/<movie_id>/')
def movie_AI(movie_id):
    """
    电影细节函数，返回问题，该电影的所有信息
    :param movie_id:
    :return:
    """
    trailer = dbhelper.fetch_trailer_info_by_movieid(movie_id)
    movie = dbhelper.fetch_movie_info_by_movieid(movie_id)
    #print(movie)
    return render_template('movie_AI.html', trailer=trailer, movie=movie)

@movie_info_blu.route('/movie_AI_view/<movie_id>/')
def movie_AI_view(movie_id):
    """
    电影细节函数，返回问题，该电影的所有信息
    :param movie_id:
    :return:
    """
    trailer = dbhelper.fetch_trailer_info_by_movieid(movie_id)
    movie = dbhelper.fetch_movie_info_by_movieid(movie_id)
    #print(movie)
    return render_template('movie_AI_view.html', trailer=trailer, movie=movie)

@movie_info_blu.route('/movie_AI_predict/<movie_id>/')
def movie_AI_predict(movie_id):
    """
    电影细节函数，返回问题，该电影的所有信息
    :param movie_id:
    :return:
    """
    trailer = dbhelper.fetch_trailer_info_by_movieid(movie_id)
    movie = dbhelper.fetch_movie_info_by_movieid(movie_id)
    #print(movie)
    return render_template('movie_AI_predict.html', trailer=trailer, movie=movie)

@movie_info_blu.route('/movie_AI_recommand/<movie_id>/<Movie_genre>', methods=['GET', 'POST'])
def movie_AI_recommand(movie_id, Movie_genre):
    """
    关键词搜索函数，返回带关键词的所有电影
    :return:
    """
    # title, content
    # 或 查找方式（通过标题和内容来查找）
    trailer = dbhelper.fetch_trailer_info_by_movieid(movie_id)
    movie = dbhelper.fetch_movie_info_by_movieid(movie_id)
    movies = dbhelper.fetch_recommand_movies_by_moviegenre(Movie_genre)
    print(movies)
    return render_template('movie_AI_recommand.html', trailer=trailer, movie=movie, movies=movies)


@movie_info_blu.route('/movie_other/<movie_id>/')
def movie_other(movie_id):
    """
    电影细节函数，返回问题，该电影的所有信息
    :param movie_id:
    :return:
    """
    trailer = dbhelper.fetch_trailer_info_by_movieid(movie_id)
    movie = dbhelper.fetch_movie_info_by_movieid(movie_id)
    #print(movie)
    return render_template('movie_other.html', trailer=trailer, movie=movie)