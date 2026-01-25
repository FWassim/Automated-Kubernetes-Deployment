from flask import Flask, render_template
import socket

app=Flask(__name__)

PIRATES=[
	{"name":"Monkey D. Luffy", "Bounty":"3.000.000.000","img":"luffy.jpg","crew":"Straw Hat Pirates"},
	{"name":"Roronoa Zoro", "Bounty":"1.111.000.000","img":"zoro.jpg","crew":"Straw Hat Pirates"},
	{"name":"Brook", "Bounty":"83.000.000","img":"brook.jpg","crew":"Straw Hat Pirates"},
	{"name":"Marshall D. Teach", "Bounty":"2.247.000.000","img":"teach.jpg","crew":"Blackbeard Pirates"},
	{"name":"Buggy Clown", "Bounty":"3.189.000.000","img":"baggy.jpg","crew":"Cross Guild"}]
@app.route('/')
def home():
	return render_template('index.html',pirates=PIRATES, server_name=socket.gethostname())
if __name__ == '__main__':
	app.run(host='0.0.0.0', port = 5000)
