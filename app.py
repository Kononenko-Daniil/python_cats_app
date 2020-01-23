from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def home():
    catsArray = [
        [{
            'name': "Cat",
            'url': "https://storage.cloud.google.com/kan-daniil/1453127166_selfi-kot-1_xaxa-net.ru.jpg"
        },
        {
            'name': "Cat",
            'url': "https://storage.cloud.google.com/kan-daniil/1494592816133830021.jpg"
        },
        {
            'name': "Cat",
            'url': "https://storage.cloud.google.com/kan-daniil/a6bd9504c3c282a19c108276797b5e03.jpg"
        }],
        [{
            'name': "Cat",
            'url': "https://storage.cloud.google.com/kan-daniil/1453127166_selfi-kot-1_xaxa-net.ru.jpg"
        },
        {
            'name': "Cat",
            'url': "https://storage.cloud.google.com/kan-daniil/1494592816133830021.jpg"
        },
        {
            'name': "Cat",
            'url': "https://storage.cloud.google.com/kan-daniil/a6bd9504c3c282a19c108276797b5e03.jpg"
        }]
    ]
    return render_template('index.html', title='Home', catsArray=catsArray)