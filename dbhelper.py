# encoding: utf-8
import logging

import pymysql


# 数据库连接
def connect():
    """
    设置连接数据库的参数和连接数据库的因素
    :return:连接数据库的连接和游标
    """
    config = {
        'host': 'localhost',
        'port': 3306,
        'user': 'root',
        'passwd': '000000',
        'charset': 'utf8mb4',
        'cursorclass': pymysql.cursors.DictCursor
    }
    conn = pymysql.connect(**config)
    conn.autocommit(1)
    cursor = conn.cursor()
    conn.select_db("grad_design")
    return conn, cursor



def sql_required(func):
    """
    装饰器，在操作数据库之前对于连接和关闭数据库
    :param func: 函数形式
    :return:装饰器
    """
    def decorate(*args, **kwargs):
        try:
            conn, cursor = connect()
            result = func(*args, **kwargs, conn=conn, cursor=cursor)
        except Exception as e:
            result = None
            logging.error(str(e))
            print(str(e))
        finally:
            cursor.close()
            conn.close()
            return result
    return decorate

@sql_required
def fetch_all_movies(conn, cursor):
    """
    取到所有电影
    :return:电影列表，列表每一项是一个字典，对应movie表中的属性
    """
    # sql = "select * from question order by create_time"
    # sql = "select a.`id`, a.`title`, a.`create_time`, a.`content`, b.`username` from question a " \
    #       "left join user b on a.`author_id`=b.`id` order by a.`create_time` desc"
    sql = "select `id`, `time`, `title`, `Trailer_series`, `description`, " \
          "`duration`, `viewCount`, `likeCount`, `dislikeCount`, `favoriteCount`, " \
          "`commentCount`, `Stars` " \
          "from filmselecttrailer order by `id`"
    cursor.execute(sql)
    rows = cursor.fetchall()
    return rows

'''
@sql_required
def fetch_movie_by_id(movie_id, conn, cursor):
    """
    根据id取得对应的movie
    :param movie_id:
    :return:
    """
    sql = "select * from filmselecttrailer where id=%s"
    args = (movie_id)
    cursor.execute(sql, args)
    movie = cursor.fetchone()
    return movie
'''

@sql_required
def search_by_key(search_key, conn, cursor):
    """
    根据key查找包含该key的movie
    :param search_key:
    :return:
    """
    # sql = "select * from user_question WHERE QuestionContent like %s or QuestionTitle like %s order by QuestionTime desc"
    sql = "select `id`, `time`, `title`, `Trailer_series`, `description`, " \
          "`duration`, `viewCount`, `likeCount`, `dislikeCount`, `favoriteCount`, " \
          "`commentCount`, `Stars` " \
          "from filmselecttrailer WHERE description " \
          "like %s or title like %s order by `id`"
    # 匹配格式为 %key%  即包含key的
    arg = "%" + search_key + "%"
    args = (arg, arg)
    cursor.execute(sql, args)
    movies = cursor.fetchall()
    return movies

@sql_required
def fetch_trailer_info_by_movieid(movie_id, conn, cursor):
    """
    通过movie_id取得对应的电影信息
    :param question_id:
    :return: 回答列表，列表中每一项是一个字典，对应answer表中的属性
    """
    # sql = "select * from answer where question_id=%s"
    # sql = "select a.`content`, a.`question_id`, a.`author_id`, a.`create_time`, b.`username` from answer a " \
    #       "left join user b on a.`author_id`=b.`id` where a.`question_id`=%s order by a.`create_time` desc"
    sql = "select `id`, `time`, `title`, `Trailer_series`, `description`, " \
          "`duration`, `viewCount`, `likeCount`, `dislikeCount`, `favoriteCount`, " \
          "`commentCount`, `Stars` " \
          "from filmselecttrailer where `id`=%s order by `id`"
    args = movie_id
    cursor.execute(sql, args)
    trailer = cursor.fetchone()
    # print(movie)
    return trailer

@sql_required
def fetch_movie_info_by_movieid(movie_id, conn, cursor):
    """
    通过movie_id取得对应的电影信息
    :param question_id:
    :return: 回答列表，列表中每一项是一个字典，对应answer表中的属性
    """
    # sql = "select * from answer where question_id=%s"
    # sql = "select a.`content`, a.`question_id`, a.`author_id`, a.`create_time`, b.`username` from answer a " \
    #       "left join user b on a.`author_id`=b.`id` where a.`question_id`=%s order by a.`create_time` desc"
    sql = "select `id`, `Movie_Title`, `Movie_Title_link`, `Movie_certificate`, `Movie_content`, " \
          "`Movie_star_rating`, `Movie_runtime`, `Movie_content1`, `Movie_genre`, `Movie_inline_block`, " \
          "`Movie_Gross`, `Movie_Headline`, `Movie_Director`, `Movie_Writers`, `Movie_Stars`, `Movie_Plot_Keywords`, " \
          "`Movie_Genres`, `Movie_Parents_Guide`, `Movie_Official_Sites`, `Movie_Country`, `Movie_Language`, `Movie_Filming_Locations`, " \
          "`Movie_Gross_USA`, `Movie_Cumulative_Worldwide_Gross`, `Movie_Production_Co`, `Movie_Sound_Mix`, " \
          "`Movie_Color`, `Movie_Aspect_Ratio`, `Movie_Description`,`Movie_Trailer`,`Movie_UK_Release_Time`, " \
          "`Movie_Budget`, `Movie_US`, `Movie_Writers_2`, `Movie_Stars_2`, `Movie_Stars_3`, `Movie_Plot_Keywords_2`, " \
          "`Movie_Plot_Keywords_3`, `Movie_Plot_Keywords_4`, `Movie_Plot_Keywords_5`, `Movie_Storyline`, " \
          "`predicted_rating`, `predicted_ranking` " \
          "from filmselecttrailer where `id`=%s order by `id`"
    args = movie_id
    cursor.execute(sql, args)
    movie = cursor.fetchone()
    # print(movie)
    return movie

@sql_required
def fetch_recommand_movies_by_moviegenre(Movie_genre, conn, cursor):
    sql = "select `id`, `time`, `title`, `Trailer_series`, `description`, " \
          "`duration`, `viewCount`, `likeCount`, `dislikeCount`, `favoriteCount`, " \
          "`commentCount`, `Stars`, `Movie_genre`, `predicted_ranking` " \
          "from filmselecttrailer where `Movie_genre`like %s order by `predicted_ranking` "
    args = Movie_genre
    cursor.execute(sql, args)
    rows = cursor.fetchall()
    return rows