from flask import Flask
from flask import render_template
from flask import request
from app.watsonapi import text2speech

app = Flask(__name__)


@app.route('/')
def hello_world():
    template_name = 'text.html'
    return render_template(template_name)

@app.route('/dotext', methods=['GET'])
def doText():
    if request.method == 'GET':
        text = request.args.get('text')
        path = '/Users/wzy/Documents/PycharmProjects/FirstDemo/static/'
        filename = 'text.wav'
        text2speech(text=text, filename=path + filename)
        template_name = 'show.html'
        return render_template(template_name, filename=filename)


if __name__ == '__main__':
    app.run()
