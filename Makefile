run-bot:
	(make clear-session && python3 main.py) || python3 main.py
clear-session:
	rm english_bot.session english_bot.session-journal
release:
	nohup python3 -u main.py > main.log 2>&1 &