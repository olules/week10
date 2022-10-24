from news import db
from datetime import datetime


class ExtraMixin(object):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()


class CbsNews(db.Model, ExtraMixin):
    __tablename__ = 'cbs_news'
    title = db.Column(db.String(255), nullable=False)
    link = db.Column(db.String(255), nullable=False)
    image = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'link': self.link,
            'image': self.image,
            'description' : self.description, 
        }

    

    @classmethod
    def get_all_news(cls):
        return cls.query.all()