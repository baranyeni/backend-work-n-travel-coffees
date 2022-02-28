from flask import Flask
from app.routes.ShopRouter import ShopRouter

app = Flask(__name__)


# TODO: Create view and render rich content
@app.route('/')
def index():
    return "Only to make sure that server is up n running"


app.register_blueprint(ShopRouter, url_prefix='/shops')

if __name__ == '__main__':
    app.debug = True
    app.run()
