import app as myApp
from config.app_factory import MyAPP
if __name__ == "__main__":
    myApp.app.run(host=MyAPP.HOST(), port=MyAPP.PORT(), debug=True)