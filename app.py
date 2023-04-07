from flask import Flask, render_template
from api.views import api_blueprint
from get.views import get_blueprint
from bookmarks.views import bookmarks_blueprint


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config.from_pyfile("default_config.py")
app.config.from_envvar("APP_SETTINGS", silent=True)

app.register_blueprint(get_blueprint)

app.register_blueprint(api_blueprint, url_prefix='/api')

app.register_blueprint(bookmarks_blueprint, url_prefix='/bookmarks')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def page_server_error(error):
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run()
