from flask import Flask
from hyper import HTTPConnection


app = Flask(__name__)


@app.route('/')
def test_http2():
    conn = HTTPConnection('api.development.push.apple.com:443')
    conn.request('POST', '/3/device/123')
    resp = conn.get_response()
    return resp.read()


if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='0.0.0.0', port=8080, debug=True)

