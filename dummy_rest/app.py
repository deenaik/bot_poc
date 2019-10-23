# dummy_rest/app.py

from flask import Flask
from flask_restplus import Resource, Api

app = Flask(__name__)
api = Api(app)


@api.route('/ticket')
class InfraTicket(Resource):
    def put(self, name, category, priority, loggedBy):
        return {'ticketID': 'TKT007'}
        
    def get(self, ticketID):
        return { 'status': 'InProgress'}


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
