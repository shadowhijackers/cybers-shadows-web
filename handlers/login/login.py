from flask import jsonify, render_template

from services.DB import db
from config.storeNames import DBStoreNames


class Login:

    def __init__(self):
        print "LOGIN HANDLE MODULE LOADED"

    def __validateLoginDetails(self, email, password):

        user_datas = db.instanse.getJSONItem(DBStoreNames.USERS_STORE_NAME())
        if user_datas is None: return None

        for data in user_datas:
            if data["email"] ==  email and data["password"] == password:
                return data

        return None

    def handleLogin(self, request):

        if request.method == 'POST':
            email = request.form["email"]
            password = request.form["pass"]
            res = self.__validateLoginDetails(email, password)
            if res:
                return jsonify(res)

        return render_template('login.html')
