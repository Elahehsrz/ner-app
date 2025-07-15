
# Named Entity Recognition (NER) App

This Flask-based web application extracts named entities from text fetched from a URL and saves them to a JSON file.

## Project Structure

* **app.py**: Main Flask application file handling URL input, entity extraction, and JSON output.
* **fetcher.py**: Module to fetch content from a given URL using `requests`.
* **extractor.py**: Module using SpaCy (`en_core_web_sm` model) to extract named entities from text.
* **saver.py**: Module to save extracted entities to a JSON file.
* **/templates/index.html**: HTML template for user interface, allowing users to input a URL and retrieve entities.

## Installation

1. Clone the repository:

   ```
   git clone <repository_url>
   cd ner-app
   ```

2. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Run the application:

   ```
   python app.py
   ```

   The application will run on `http://localhost:5000` by default.

## Usage

1. Access the application through a web browser.
2. Enter a valid URL in the provided form and submit.
3. The application will fetch the URL content, extract entities, and offer a download of the extracted entities in JSON format.

## Dependencies

* Flask: Web framework for Python.
* requests: HTTP library for Python.
* spaCy: Natural Language Processing library for Python.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

