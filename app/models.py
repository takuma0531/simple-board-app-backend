from app import db, ma
import datetime


# model for post
class Post(db.Model):
  __tablename__ = 'post'

  id = db.Column(db.Integer, primary_key=True)
  post_content = db.Column(db.String(100), nullable=False)
  posted_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
  replies = db.relationship('Reply', cascade='all,delete', backref='post', lazy='dynamic')

  def __init__(self, post_content):
    self.post_content = post_content

# model for reply
class Reply(db.Model):
  __tablename__ = 'reply'

  id = db.Column(db.Integer, primary_key=True)
  reply_content = db.Column(db.String(100), nullable=False)
  replied_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
  post_id = db.Column(db.Integer, db.ForeignKey('post.id'))

  def __init__(self, reply_content, post_id):
    self.reply_content = reply_content
    self.post_id = post_id


# post schema
class PostSchema(ma.Schema):
  class Meta:
    fields = ('id', 'post_content', 'posted_date')

# reply schema
class ReplySchema(ma.Schema):
  class Meta:
    fields = ('id', 'reply_content', 'replied_date')