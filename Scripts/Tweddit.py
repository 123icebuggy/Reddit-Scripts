import praw
import obot
import sqlite3
import time
import importlib
import twitter
import datetime
import praw

SUBREDDIT = 'titlegore'

WAIT = 1800
print('Opening database')
sql = sqlite3.connect('ids.db')
cur = sql.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS oldposts(ID TEXT)')
sql.commit()

print('Logging in to Twitter')
t = twitter.login()
print('Logging in to Reddit')
r = praw.Reddit(user_agent='/u/123icebuggy\'s twitter script for scraping twitter')

whatl = 50
def tweeter():
	what = whatl + 1
	print('Fetching subreddit /r/%s' % SUBREDDIT)
	subreddit = r.get_subreddit(SUBREDDIT)
	print('Fetching subreddit posts')
	subs = subreddit.get_hot(limit=whatl)
	for x in subs:
		sid = x.id
		cur.execute('SELECT * FROM oldposts WHERE ID=?', [sid])
		if not cur.fetchone():
			try:
				sauthor = x.author.name
				stitle = x.title
				
				if len(stitle) < 115:
					try:
						if x.score > 4:
							try:
								print('here')
								tweet = stitle + ' redd.it/%s' % sid
								print(len(tweet))
								print(tweet)
								twitter.poststatus(tweet)
								print('her')
								cur.execute('INSERT INTO oldposts VALUES(?)', [sid])
								sql.commit()
								break
							except Exception as e:
								print(e)
					except:
						pass

				if len(stitle) > 144:
					pass
			except AttributeError:
				pass
			


while True:
	try:
		tweeter()
		print('Waiting %s minutes at %s' % (str(WAIT / 60), datetime.datetime.now().time()))
	except:
		print('Error, trying in 30 minutes')
		pass

	time.sleep(WAIT)
	
