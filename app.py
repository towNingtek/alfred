import flask
from flask import request
from flask_cors import CORS
import dotenv
import json
import os

from pkg.iota import IOTA
from utils.code import hex_to_string, str_to_hex

app = flask.Flask(__name__)
CORS(app)

if os.path.exists('.env'):
    dotenv.load_dotenv('.env')

iota_instance = IOTA()
node = iota_instance.get_node()

@app.route('/iota/info')
def node_info():
  # Get the node info
  node_info = node.get_info()
  response = app.response_class(
    response = json.dumps(node_info),
    status = 200,
    mimetype = "application/json"
  )
  return response

@app.route("/iota/message", methods = ["POST"])
def data_block_write():
  data = request.json

  options = {
    "tag": str_to_hex(os.getenv("IOTA_DATA_BLOCK_TAG")),
    "data": str_to_hex(data["message"]),
  }

  # Create and post a block with a tagged data payload
  block = node.build_and_post_block(None, options)

  response = app.response_class(
    response = json.dumps(block),
    status = 200,
    mimetype = "application/json"
  )
  return response

@app.route("/iota/message/", methods = ["GET"])
def data_block_read():
  output = node.get_block_data(request.args.get("messageID"))
  message_str = hex_to_string(output["payload"]["data"])

  res = {"msg":message_str}
  response = app.response_class(
    response = json.dumps(res),
    status = 200,
    mimetype = "application/json"
  )

  return response

if __name__ == "__main__":
    app.run("0.0.0.0", os.getenv("SERVICE_PORT"))
