#!/usr/bin/python3

a, b = map(int, input().split())

if a > b :
	print('>')
elif a < b :
	print('<')
else :
	print('==')
