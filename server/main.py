from flask import Flask,render_template,request
 
import argparse
from pyphonetics import RefinedSoundex
import pronouncing as pr

def modify_sentence(sentence):
    rs = RefinedSoundex()
    phrase = sentence

    def find_best_word(words, target):

        min_backup_distance = 5
        backup = target
        for word in words:
            distance = rs.distance(word, target)
            if distance < 1:
                return word
            elif distance < min_backup_distance:
                backup = word
                min_backup_distance = distance
        return backup

    sf = [find_best_word(pr.rhymes(word), word) for word in phrase.split(" ")]
    return " ".join(sf)



app = Flask(__name__)

@app.route('/form')
def form():
    return """<form action="/data" method = "POST">
    <p>Message: <input type = "text" name = "Message" /></p>
    <p><input type = "submit" value = "Submit" /></p>
</form>"""
 
@app.route('/data', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = request.form
        return modify_sentence(form_data["Message"])
