import json
from flask import Flask, request, Response
from dragnet import content_extractor, content_comments_extractor

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
  print request.method
  if request.method == 'POST':
    webpage = request.files['webpage'].read()
    content_comments = content_comments_extractor.analyze(webpage)
    data = {
      'content': content_comments,
    }
    js = json.dumps(data)
    resp = Response(js, status=200, mimetype='application/json')
    print content_comments
  return resp