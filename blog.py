import datetime
from flask import Flask, render_template
from data import db_session
from data.news import News
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init('db/blogs.db')
    app.run(port=8000, host='127.0.0.1')
    # user = User()
    # user.name = "Пользователь 3"
    # user.about = "биография пользователя 3"
    # user.email = "email3@email.ru"
    db_sess = db_session.create_session()
    #db_sess.add(user)
    #db_sess.commit()
    # users = db_sess.query(User).all()
    # # for user in users:
    # #     print(user.name)
    # # user.name = "Changed username"
    # # user.created_date = datetime.datetime.now()
    # # db_sess.commit()
    user = db_sess.query(User).filter(User.id == 1).first()
    news = News(title="Вторая новость", content="Уже вторая запись!",
                user=user, is_private=False)
    db_sess.add(news)
    db_sess.commit()
@app.route("/")
def index():
    db_sess = db_session.create_session()
    news = db_sess.query(News).filter(News.is_private != True)
    return render_template("index.html", news=news)
if __name__ == '__main__':
    main()
