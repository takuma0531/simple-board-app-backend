from app import app, db, ma
from app.models import Post, Reply, PostSchema, ReplySchema
from flask import jsonify, request


# init PostSchema
post_schema = PostSchema()
posts_schema = PostSchema(many=True)

reply_schema = ReplySchema()
replies_schema = ReplySchema(many=True)

# home page in which the users can post messages and explore
@app.route('/board-app', methods=['GET', 'POST'])
def homePage():
  # add new post content into the database
  if request.method == 'POST':
    post_content = request.json['post_content']

    new_post = Post(post_content)

    db.session.add(new_post)
    db.session.commit()

    return post_schema.jsonify(new_post)

  else:
    all_posts = Post.query.all()
    posts = posts_schema.dump(all_posts)
    return jsonify(posts)

# thread page in which the users can check a post and the replies and can delete the post or any reply
@app.route('/board-app/<id>', methods=['GET', 'POST', 'DELETE'])
def threadPage(id):
  
  post = Post.query.get(id)
  replies = replies_schema.dump(post.replies)

  # collect all the data to convert them to json format
  thread_info = [{
    'id': post.id,
    'post_content': post.post_content,
    'posted_date': post.posted_date,
    'replies': replies
  }]

  if request.method == 'POST':
    reply_content = request.json['reply_content']

    new_reply = Reply(reply_content, id)

    db.session.add(new_reply)
    db.session.commit()

    return reply_schema.jsonify(new_reply)

  elif request.method == 'DELETE':
    post = Post.query.get(id)
    db.session.delete(post)
    db.session.commit()
    
    return post_schema.jsonify(post)

  return jsonify(thread_info)

@app.route('/board-app/<id>/<reply_id>', methods=['DELETE'])
def deleteReply(id, reply_id):
  reply = Reply.query.get(reply_id)
  db.session.delete(reply)
  db.session.commit()

  return reply_schema.jsonify(reply)
