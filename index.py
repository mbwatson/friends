from flask import Flask, render_template
import friends

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/season/<num>')
def season(num):
	episodes = friends.get_episodes_in_season(num)
	hits = friends.get_season_hits(num)
	return render_template('season.html', seasonNumber=num, episodes=episodes, hits=hits)

if __name__ == '__main__':
	app.run(debug=True)
