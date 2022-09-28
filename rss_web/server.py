import feedparser
from flask import Flask, request, render_template, redirect, session

app = Flask(__name__)
app.secret_key = 'some super secret key'

@app.route('/')
def index():
    session.clear()
    return render_template('index.html')


@app.route('/rss_read', methods=['POST'])
def rss_read():
    url = request.form['url']
    if 'data' in session:
        print(f'{session.data} exists already')
    else:
        session['data'] = None
    data = feedparser.parse(url)
    new_data = []
    for item in range(len(data['entries'])-30):
        new_data.append(data['entries'][item])
    session['data'] = new_data
    return redirect('/result')


@app.route('/result')
def result():
    print(session)
    return render_template('result.html', all_data=session['data'])






if __name__ == '__main__':
    app.run(debug=True)