#!/usr/local/bin/python3.7

import os, sys, io, cgi
sys.stdin =  open(sys.stdin.fileno(),  'r', encoding='UTF-8')
sys.stdout = open(sys.stdout.fileno(), 'w', encoding='UTF-8')
sys.stderr = open(sys.stderr.fileno(), 'w', encoding='UTF-8')

out = lambda msg: print(msg, end="\r\n")

out("Content-Type: text/html; charset=utf-8")
out("")

out("<html><meta charset='utf-8'><body>")
out("<h1>テスト</h1>")
out("</body></html>")
