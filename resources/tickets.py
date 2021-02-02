from flask_restful import Resource, fields, reqparse
from flask import jsonify
from ticketing.common.models.ticket_model import TicketModel
import random
import datetime

parser = reqparse.RequestParser()
parser.add_argument(
    'id', dest='id', location='args', type=int
)
parser.add_argument(
    'user_id', dest='user_id', location='args', type=int
)

temp_tickets = []

temp_users = [
    {
        'id': 1,
        'name': 'miki'
    },
        {
        'id': 2,
        'name': 'Miklós'
    },
    {
        'id': 3,
        'name': 'azott'
    }
]

for x in range(1,101):
    user = random.randint(0,3)
    t = TicketModel(x,'inc', f'{x} -- SD',f'{x} -- LD',datetime.datetime.now(), user)
    temp_tickets.append(t)


def get_ticket_by_id(id, dataset):
    """
    @todo   Implement error
    """
    for i in range(len(dataset)):
        if dataset[i].id == id:
            return dataset[i]
    raise NotImplementedError

def get_ticket_by_creator(id, dataset):
    """
    @todo   Implement error
    """
    tickets = []
    for i in range(len(dataset)):
        if dataset[i].created_by == id:
            tickets.append(dataset[i].to_dict())
    if len(tickets) == 0:
        raise NotImplementedError
    return tickets


def get_all_tickets(dataset):
    tickets = []
    for x in dataset:
        tickets.append(x.to_dict())
    return tickets


def get_handler(args):
    if args['user_id'] is not None and args['id'] is not None:
        return jsonify('Very bad')

    if args['id'] is not None:
        try:
            ticket = get_ticket_by_id(args['id'], temp_tickets)
            return jsonify(ticket.to_dict())
        except Exception as e:
            return(jsonify('no bueno'))

    if args['user_id'] is not None:
        try:
            tickets = get_ticket_by_creator(args['user_id'], temp_tickets)
            return jsonify({'length': len(tickets), 'tickets': tickets})
        except Exception as e:
            return(jsonify('no bueno userfronton'))
            print(e)
    return jsonify({'length': len(temp_tickets), 'tickets': get_all_tickets(temp_tickets)})


def post_handler(data):
    """Creates a new ticket"""
    def validate_data(data):
        pass


class Tickets(Resource):
    def get(self):
        args = parser.parse_args()
        return(get_handler(args))

    def post(self):
        pass
