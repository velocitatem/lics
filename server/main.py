from flask import Flask,render_template,request
 
import argparse
from pyphonetics import RefinedSoundex
import pronouncing as pr




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
