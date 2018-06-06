import json
from bottle import (Bottle, run)
from bottle.ext import sqlalchemy
from models import engine, Base, User

app = Bottle()
plugin = sqlalchemy.Plugin(
    engine,
    Base.metadata,
    keyword='db',
    create=True,
    commit=True,
    use_kwargs=False,
)
app.install(plugin)


@app.get('/')
def index(db):
    """Example of how to return json from sqlalchemy"""
    comments = db.query(User).all()
    json_data = [{'comment_id': comment.comment_id, 'author': comment.author} for
                 comment in comments]
    # for comment in comments:
    #     comment_obj = {
    #         'comment_id': comment.comment_id,
    #         'author': comment.author,
    #         'created_utc': str(comment.created_utc),
    #     }
    #     json_data.append(comment_obj)
    return json.dumps(json_data)


run(app=app, host='localhost', port=8080, reloader=True, debug=True)
