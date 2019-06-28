#!/usr/bin/env python3
# This program is an insecure password storage

import sys, pyperclip

if len(sys.argv) != 2:
	print('Incorrect number of arguments')
	print('Usage: python password-project.py [account]')
	sys.exit()

passwords = {
	'email': 'ds54ds5d4s5d4ds',
	'lugage': '56874',
	'facebook': 'R5fd4qd587d',
	'blog': 'i54fd54#@fdkgG'
}

account = sys.argv[1]

if account not in passwords:
	print('Account named ' + account + ' not registered.')
	sys.exit()
else:
	pyperclip.copy(passwords[account])
	print('Password for ' + account + ' copied to clipboard.')
	