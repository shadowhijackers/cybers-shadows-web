from flask import Flask, request, url_for, render_template, jsonify, Markup
from redis import Redis, RedisError

from handlers.comments.comments import Comments
from handlers.login.login import Login
from services.errorHandler.errorHandler import ErrorHandler
from config.deeplinks import DeepLinks
app = Flask(__name__, template_folder='views', static_url_path='')

@app.route(DeepLinks.INDEX(), methods=['GET', 'POST'])
def login():

    try:

        loginHandlerInstanse = Login()
        return loginHandlerInstanse.handleLogin(request)

    except RedisError:

        ErrorHandler.handle(RedisError)
        return  "<div style='text-align:center'><h1> !OOOPS</h1></div>"


@app.route(DeepLinks.COMMENTS(), methods=['GET', 'POST'])
def comments():
    try:

        commentsHandlerInstanse = Comments()
        return commentsHandlerInstanse.handleComments(request)

    except RedisError, Argument:

        ErrorHandler.handle(RedisError)
        return "<div style='text-align:center'><h1> !OOOPS</h1></div>"

