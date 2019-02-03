from flask import jsonify, Markup, render_template
from services.DB import db
from config.storeNames import DBStoreNames


class Comments:

    def __init__(self):

        print "COMMENTS MODULE LOADED"


    def __storeCommentsInRedis(self,  newComment):

        comments = self.__getCommentDatas()
        if comments is not None:
            comments.append(newComment)
        else:
            comments = [newComment]
        self.__setComments(comments)
        return jsonify(comments)


    def __getCommentDatas(self):

        return db.instanse.getJSONItem(DBStoreNames.COMENTS_STORE_NAME())


    def __setComments(self, comments):

        db.instanse.setJSONItem(DBStoreNames.COMENTS_STORE_NAME(), comments)


    def __formCommnent(self, name, comment):

        return {"name": name, "comment": comment}


    def handleComments(self, request):

        if request.method == 'POST':

            commentor = Markup(request.form['name']).striptags()
            comment = Markup(request.form['comment']).striptags()
            newComment = self.__formCommnent(commentor, comment)
            return self.__storeCommentsInRedis(newComment)

        comments = self.__getCommentDatas()
        return render_template('comments.html', comments=comments)
