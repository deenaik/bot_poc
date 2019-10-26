from mongoengine import connect, Document, StringField, DateTimeField

connect('dummy_rest', host='mongo')


class Tickets(Document):
    TiketID = StringField(max_length=50)
    TicketName = StringField(max_length=255)
    Category = StringField(max_length=50)
    Priority = StringField(max_length=50)
    LoggedBy = StringField(max_length=50)
    DateCreated = DateTimeField()
    DueDate = DateTimeField()
    Status = StringField(max_length=50)

    meta = {
        'allow_inheritance': True,
        'indexes': [
            '$TiketID',
        ]
    }
