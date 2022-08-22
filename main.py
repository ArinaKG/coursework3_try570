from flask import Flask, render_template

import logging

from utils import get_posts_all, get_post_by_pk, get_comments_by_pk


app = Flask(__name__)

logging.basicConfig(filename='logs/api.log', level=logging.INFO)
logger = logging.getLogger(__name__)

#делаем экземпляр класса блюпринт
main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route('/')
def main_page():
    """
    вьюшка блюпринт на главную страницу
    :return:
    """
    posters = get_posts_all()

    return render_template('index.html', posters=posters)


@main_blueprint.route('/posts/<int:postid>')
def post_page(postid):
    post_pk = get_post_by_pk(postid)
    post_comms = get_comments_by_post_id(postid)
    com_len = len(post_comms)
    return render_template('post.html', post_pk=post_pk, post_comms=post_comms, com_len=com_len)


@app.route('/')
def page_get_posts_all():
    posts = get_posts_all()
    return render_template('index.html', posts=posts)

#возвращает посты определенного пользователя. Функция должна вызывать ошибку `ValueError` если такого пользователя нет и пустой список, если у пользователя нет постов.
#@app.route('/search/<name>/')
#     def get_posts_by_user():
#         posts = get_posts_by_user()
#         count_posts = len(posts)
#         return render_template('post.html', posts=posts, count_posts=count_posts)


#def get_comments_by_post_id(post_id) #возвращает комментарии определенного поста. Функция должна вызывать ошибку `ValueError` если такого поста нет и пустой список, если у поста нет комментов.

#def search_for_posts(query) #возвращает список постов по ключевому слову

@app.route('/posts/<int:pk>')
def page_get_post_by_pk(pk): #возвращает один пост по его идентификатору
    post_by_pk = get_post_by_pk(pk)
    coments_by_pk = get_comments_by_pk(pk)
    return render_template('post.html', post_by_pk=post_by_pk, coments_by_pk=coments_by_pk)


@main_blueprint.route('/results/', methods=['POST', 'GET'])
def page_search_results():
    answer = request.values.get('query')
    post_results = search_for_posts(answer)
    len_post_results = len(post_results)
    return render_template('search-results.html', post_results=post_results, len_post_results=len_post_results)


@main_blueprint.route('/users/<username>')
def users_page(username):
    post_for_usernames = get_posts_by_user(username)
    return render_template('user-feed.html', post_for_usernames=post_for_usernames)


@main_blueprint.route('/api/posts')
def api_posts_page():
    logging.info("запрос на все посты")
    with open('data/data.json', "r", encoding="utf-8") as f:
        post_data = json.load(f)
    return jsonify(post_data)


@main_blueprint.route('/api/posts/<int:post_id>')
def api_get_posts_by_user(post_id):
    logging.info("запрос на один пост")
    with open('data/data.json', 'r', encoding="utf-8") as f:
        post_data = json.load(f)
    post_for_pk = []
    for post in post_data:
        if post_id == post['pk']:
            post_for_pk.append(post)
    return jsonify(post_for_pk)


if __name__ == '__main__':
    app.run(debug=True)

#http://127.0.0.1:5000/posts/2