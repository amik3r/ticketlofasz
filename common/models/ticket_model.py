class TicketModel:
    def __init__(self, id, type, short_description, description, created_at, created_by):
        self.id = id
        self.type = type
        self.short_description = short_description
        self.description = description
        self.created_at = created_at
        self.updated_at = None
        self.closed_at = None
        self.created_by = created_by
        self.updated_by = None
        self.closed_by = None
        self.closed = False

        if self.closed_at is not None and self.closed_by is not None:
            self.closed = True
        
    def to_dict(self):
        return self.__dict__
