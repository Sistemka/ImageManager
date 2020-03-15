from flask import jsonify
from flask_restx import Resource, Namespace

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
class GetUrls(Resource):
    def get(self):
        basic_args.parse_args()
        record = Items.find()
        urls = [r.get('path') for r in record]
        return jsonify({
            'error': False,
            'result': urls
        })


def register(main_api):
    main_api.add_namespace(ns)
