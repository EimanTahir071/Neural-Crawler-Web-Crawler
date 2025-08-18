from flask import Flask, render_template, request
from crawler_runner import run_crawl

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/crawl', methods=['POST'])
def crawl():
    results = run_crawl()
    return render_template('index.html', results=results)

# ✅ Required to start the server
if __name__ == '__main__':
    app.run(debug=True)
