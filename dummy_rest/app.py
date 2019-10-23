# dummy_rest/app.py

from flask import Flask
from flask_restplus import Resource, Api, fields

flask_app = Flask(__name__)
app = Api(app = flask_app,
          version = "1.0",
          title = "Ticket API",
          description = "Create Tickets and Get Status of ticket")

name_space = app.namespace('Tickets', description='Dummy Sharepoint API')

model1 = app.model('Tickets_put', {
    'name': fields.String(description='Ticket Subject', required=True),
    'category': fields.String(description='Ticket Category', required=True, enum=['Hardware', 'Software', 'Network', 'Security']),
    'priority': fields.String(description='Ticket Priority', required=True, enum=['Critical', 'High', 'Medium', 'Low']),
    'loggedBy': fields.String(description='Ticket Owner', required=True),
})

model2 = app.model('Tickets_get', {
    'ticketID': fields.String(description='Ticket ID', required=True)
})


@name_space.route('/ticket')
class InfraTicket(Resource):
    @app.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' }, 
			 params={ 'name': 'Ticket Subject',
                      'category': 'Ticket Category',
                      'priority': 'Ticket Priority',
                      'loggedBy': 'Ticket Owner'})
    @app.expect(model1)
    def post(self, **kwargs):
        return {'ticketID': 'TKT007'}, 200
    
    @app.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' }, 
			 params={ 'ticketID': 'Ticket ID'})
    def get(self, ticketID):
        return { 'status': 'InProgress'}, 200


if __name__ == '__main__':
    flask_app.run(debug=True, host='0.0.0.0', port=80)
