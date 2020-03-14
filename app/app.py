from werkzeug.datastructures import FileStorage
from werkzeug.middleware.proxy_fix import ProxyFix
from flask_restplus import Api, reqparse
from flask import Flask
import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property

app = Flask(__name__)

app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)


api = Api(
    app=app,
    doc='/swagger-ui',
    title='ImageManager',
    description='Service to manage images for search engine'
)


basic_args = reqparse.RequestParser(bundle_errors=True, trim=True)
basic_args.add_argument(
    'X-SERVICE-NAME', location='headers', required=True, nullable=False)

image_args = reqparse.RequestParser(bundle_errors=True, trim=True)
image_args.add_argument('image', type=FileStorage,
                        location='files', required=True)
image_args.add_argument('type', type=str, required=True)
image_args.add_argument('цена', type=int, required=True)
image_args.add_argument('пол', type=str, required=False)
image_args.add_argument('цвет', type=str, required=True)
image_args.add_argument('бренд', type=str, required=True)
image_args.add_argument('link', type=str, required=True)
