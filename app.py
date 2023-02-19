from flask import Flask, render_template

app = Flask(__name__)

YouTubeURLS = [
    {
        'id': 1,
        'title': 'YouTube URL 1'
    },
    {
        'id': 2,
        'title': 'YouTube URL 2'
    }
]

@app.route("/")
def hello_world():
    return render_template('home.html', urls=YouTubeURLS)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)