import decimal
import flask.json

class CustomJsonEncoder(flask.json.JSONEncoder):

  def default(self, obj):
      if isinstance(obj, decimal.Decimal):
          # Convert decimal instances to strings.
          return str(obj)
      return super(CustomJsonEncoder, self).default(obj)