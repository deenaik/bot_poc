# dummy_rest/app.py

from flask import Flask, request
from flask_restplus import Resource, Api, fields
import random
from schema import Tickets

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

status_fields = ["assigned", "under analysis", "under resolution", "waiting for procurement", "waiting for approval", "blocked"]


@name_space.route('/ticket')
class InfraTicket(Resource):
    @app.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' }, 
			 params={ 'name': 'Ticket Subject',
                      'category': 'Ticket Category',
                      'priority': 'Ticket Priority',
                      'loggedBy': 'Ticket Owner'})
    @app.expect(model1)
    def post(self, **kwargs):
        result = Tickets(
            TiketID = 'TKT' + str(random.randrange(100, 500, 1)),
            TicketName = request.args.get('name'),
            Category = request.args.get('category'),
            Priority = request.args.get('priority'),
            LoggedBy = request.args.get('loggedBy'),
            Status = random.choice(status_fields)
        ).save()
        print(result)
        return {'ticketID': 'TKT' + str(random.randrange(100, 300, 1))}, 200
    

    @app.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' }, 
			 params={ 'ticketID': 'Ticket ID'})
    def get(self, **kwargs):
        ticketid = request.args.get('ticketID')
        if ticketid == None:
            return { 'TKT' + str(random.randrange(100, 300, 1)): random.choice(status_fields),
                     'TKT' + str(random.randrange(100, 300, 1)): random.choice(status_fields) }, 200
        if int(ticketid[3:]) < 300:
            return {'status': random.choice(status_fields)}, 200
        else:
            return {'status': 'Invalid Ticket Number'}, 200


if __name__ == '__main__':
    flask_app.run(debug=True, host='0.0.0.0', port=80)
