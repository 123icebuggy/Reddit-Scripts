#JC Bot
import praw
import sqlite3
import obotjc
import warnings
from time import sleep


warnings.simplefilter("ignore", ResourceWarning)

SETPHRASES = ['ram', 'crash', 'glitch', 'freeze', 'freezes', 'load', 'mess', 'crashed', 'bug', 'memory', 'frame rate','fixed','issue', 'fps', 'unplayable', 'stutter', 'performance']
CONSOLE = ['console', 'ps4', 'xbox', 'xbone', 'xbox one', 'playstation', 'play station']

RESPONSE = '''Hi there! I am leaving this comment here as I believe you may be mentioning bugs or performance issues in the game. \n \n Here are some articles that may help:\n \n
1.[Advanced Performance Tips](https://www.reddit.com/r/JustCause/comments/3vg025/some_advanced_jc3_performance_tweakstips/?st=is1vsb8w&sh=a79acceb)\n
2.[FPS Boost Ultimate Guide](https://steamcommunity.com/app/225540/discussions/0/485624149156176665/)\n
3.[Offical Just Cause 3 Forums Thread](https://steamcommunity.com/app/225540/discussions/0/485624040227751780/)
___
I am a bot, this reply was automatic. If you have any questions or concerns, please message /u/JustCauseHelper
'''

print('Opening Database...')
sql = sqlite3.connect('jc.db')
cur = sql.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS oldposts(ID TEXT)')
sql.commit()

print('Logging in...')
r = obotjc.login()

def check():
	print('Getting Submissions...')
	submissions = r.get_subreddit('justcause').get_new(limit=5)
	print('Processing Submissions...')
	for x in submissions:
		if x.stickied == False:
			title = x.title.lower()
			cid = x.id
			cur.execute('SELECT * FROM oldposts WHERE ID=?', [cid])
			
			if not cur.fetchone():
				if not any(ext in title for ext in CONSOLE):
					if any(key.lower() in title for key in SETPHRASES):
						print('Found Match', x.title)
						x.add_comment(RESPONSE)
						cur.execute('INSERT INTO oldposts VALUES(?)', [cid])
						sql.commit()
				if any(ext in title for ext in CONSOLE):
					print('Found post but it was related to console')

while True:
	try:
		check()
	except Exception as e:
		raise e
		with open ('errors.txt', 'wb') as f:
			try:
				f.write(str(e))
				f.close
			except:
				pass
		pass
	sleep(60)
