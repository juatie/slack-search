#!/usr/bin/env python3

import sys
from post_to_slack import post_to_slack

for line in sys.stdin:
	post_to_slack(line)