from flask import Flask, request, url_for, render_template, jsonify
from redis import Redis, RedisError
import json
import os
import socket

# Connect to Redis
from handlers.comments.comments import Comments

redis = Redis(host="0.0.0.0", db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__, template_folder='views', static_url_path='')


@app.route("/", methods=['GET', 'POST'])
def index():

    global comments
    comments = []
    commentsIns = Comments()
    try:

        if request.method == 'POST':
            commentor = request.form['name']
            comment = request.form['comments']
            newComment = commentsIns.formCommnent(commentor, comment)
            return commentsIns.storeCommentsInRedis(newComment)

    except RedisError, Argument:
        error = "<i>cannot connect to Redis, counter disabled</i> {Argument}"
        return error

    return render_template('comments.html')



