from flask import jsonify
from flask_restplus import Resource, Namespace

from app.app import basic_args
from models import Items

ns = Namespace(
    'url',
    description=(
        'Handlers to get urls for images'
    ),
    validate=True
)


@ns.route('/all')
@ns.expect(basic_args)
class Predict(Resource):
    def get(self):
        basic_args.parse_args()
        record = Items.select()
        urls = [r.url for r in record]
        return jsonify({
            'error': False,
            'result': urls
        })


def register(main_api):
    main_api.add_namespace(ns)
