from flask import Flask, request, render_template, send_file
import os
from fetcher import fetch_url_content
from extractor import extract_entities
from saver import save_entities_to_json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    url = request.form['url']
    content = fetch_url_content(url)
    if content is None:
        return "Error fetching the URL", 500

    entities = extract_entities(content)
    json_filename = 'entities.json'
    save_entities_to_json(entities, json_filename)
    
    return send_file(json_filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)

