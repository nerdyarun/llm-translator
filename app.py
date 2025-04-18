from flask import Flask, render_template, request
from translator import translate_text


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    translations = {}
    input_text = ''
    if request.method == 'POST':
        input_text = request.form['text']
        translations = translate_text(input_text)
    return render_template('index.html', translations=translations, input_text=input_text)

if __name__ == '__main__':
    app.run(debug=True)
