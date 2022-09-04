import json

def get_posts_all(): #возвращает посты
    with open("data/data.json", "r", encoding="utf-8") as f:
        return json.load(f)


def get_posts_by_user(user_name): #возвращает посты определенного пользователя. Функция должна вызывать ошибку `ValueError` если такого пользователя нет и пустой список, если у пользователя нет постов.
    posts = get_posts_all()
    users_posts = []
    #if user_name in _index_user():
    for i in range(len(posts)):
        if posts[i]["poster_name"] == user_name:
            users_posts.append(posts[i])
    return users_posts
 #   raise ValueError('User not found')

def get_comments_by_post_id(post_id): #возвращает комментарии определенного поста. Функция должна вызывать ошибку `ValueError` если такого поста нет и пустой список, если у поста нет комментов.
    file_with_comments = get_all_comments()
    comments = []
    for i in range(len(file_with_comments)):
        if file_with_comments[i]['post_id'] == post_id:
            comments.append(file_with_comments[i])
    return comments


def search_for_posts(query): #возвращает список постов по ключевому слову
    posts = []
    query = (str(query)).lower()
    for i in range(len(get_posts_all())):
        if query in get_posts_all()[i]["content"].lower():
            posts.append(get_posts_all()[i])
    return posts


def get_all_comments():
    with open("data/comments.json", "r", encoding="utf-8") as f:
        return json.load(f)

def get_post_by_pk(pk): #возвращает один пост по его идентификатору
    temp = get_posts_all()
    for i in range(len(temp)):
        if pk == temp[i]['pk']:
            return temp[i]


def get_comments_by_pk(pk): #возвращает все комментарии поста
    coments = get_all_comments()
    res = []
    for i in range(len(coments)):
        if pk == coments[i]['pk']:
            res.append(coments[i])
    return res


#print(get_posts_all())
#print(get_all_comments())
#print(get_post_by_pk())
#print(get_comments_by_pk(1))