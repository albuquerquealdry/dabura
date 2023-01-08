from flask import Flask
from flask import request
from router import router
from flask import request
app = Flask(__name__)

class main():
    @app.route("/initS3")
    def initS3():
        return router.Router.initS3Router()
    
    app.run()
main()