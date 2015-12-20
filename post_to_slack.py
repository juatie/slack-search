#!/usr/bin/env python3
# curl -X POST --data-urlencode 'payload={"channel": "#general", "username": "squirrelbot", "text": "This is posted to #general and comes from a bot named webhookbot.", "icon_emoji": ":squirrel:"}' https://hooks.slack.com/services/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


import requests
import sys


with open("incoming_webhook_url.txt") as f:
	url = f.read()


def post_to_slack(text):
	payload = {
		"channel": "#general",
		"username": "julia",
		"text": text,
		"icon_emoji": ":squirrel:",
	}
	requests.post(url, json=payload)

