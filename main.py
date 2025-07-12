from flask import Flask, request, render_template
from pytubefix import YouTube

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        url = request.form['url']
        yt = YouTube(url)
        ys = yt.streams.get_highest_resolution()
        ys.download(output_path='static')
        output_path = f'static/{yt.title}.mp4'
        return render_template('index.html', video=output_path)
    
    return render_template('index.html')






if __name__ == '__main__':
    app.run(debug=True)