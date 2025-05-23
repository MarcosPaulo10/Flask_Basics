from blueprintapp.app import db

class Todo(db.Model):
    __tablename__ = 'todos'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    done = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<TODO {self.title} - {self.done}>'
    
    def get_id(self):
        return self.id
    
    