import json
import redis
from flask import jsonify


class Comments:

    def storeCommentsInRedis(self, newComment, comments):
        comments = None
        commentsStr = redis.get("comments")
        if commentsStr != None:
            comments = json.loads(commentsStr)

        if comments != None:
            comments.append(newComment)
        else:
            comments = []
            comments.append(newComment)

        redis.set("comments", json.dumps(comments))
        return jsonify(comments)


    def getCommentDatas(self, redis):
        redis.get("comments")


    def formCommnent(self, name, comment):
        return {"name": name, "comments": comment}
