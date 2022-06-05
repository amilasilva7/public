
import pickle

import pandas as pd
from flask import Flask, request
from flask_cors import CORS, cross_origin
from flask_restful import Api, Resource

app = Flask(__name__)
CORS(app, support_credentials=True)
api = Api(app)

class HelloWorld(Resource):
    @app.route('/check-user-information', methods=['POST'])
    @cross_origin(support_credentials=True)
    def helloWorld():
        data = request.get_json()
        profilePic = data.get('profile pic', '')
        usernameLength = data.get('nums/length username', '')
        processedFullname = data.get('fullname words', '')
        fullnameLength = data.get("nums/length fullname", '')

        print(profilePic)
        print(usernameLength)
        print(processedFullname)
        print(fullnameLength)

        executable_model = pickle.load( open('genuneProfile.h5', 'rb'))
        newData = [[profilePic, usernameLength, processedFullname, fullnameLength]]
        inputDataSet = pd.DataFrame(newData, columns=['profile pic', 'nums/length username', 'fullname words', 'nums/length fullname'])
        isFake = executable_model.predict(inputDataSet)
        print(isFake)
        if(isFake=='[1]'):
            result = "GenuineProfile"
        else:
            result = "FakeProfile"

        return result


if __name__ == "__main__":
    api.add_resource(HelloWorld)
    app.run()