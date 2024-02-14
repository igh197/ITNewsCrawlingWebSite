from app import db


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(1000), nullable=True)
    content = db.Column(db.Text(), nullable=True)
    copyright = db.Column(db.String(100), nullable=True)

    def __init__(self, title, content, copyright):
        self.title = title
        self.content = content
        self.copyright = copyright
