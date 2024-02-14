from flask import Blueprint, render_template, redirect, url_for
from crawling import crawling
from models.models import News

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
def itNews():
    crawling()
    news_list = News.query.order_by(News.id.asc())
    return render_template('/news.html', news_list=news_list)
