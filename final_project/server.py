from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask(__name__,template_folder='templates')

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    fr_translated = translator.english_to_french(textToTranslate)
    return fr_translated

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    en_translated = translator.french_to_english(textToTranslate)
    return en_translated

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)