import uuid
from pathlib import Path

from flask import jsonify, send_from_directory
from flask_restx import Resource, Namespace

from app.app import basic_args, image_args, info_args
from models import Items
from settings.paths import IMAGES_DIR

ns = Namespace(
    'image',
    description=(
        'Handlers to upload images in fs and they urls in database'
    ),
    validate=True
)


@ns.route('/upload')
@ns.expect(basic_args)
class Upload(Resource):
    @ns.expect(image_args)
    def post(self):
        basic_args.parse_args()
        args = image_args.parse_args()

        image = args['image']
        image.filename = f"{uuid.uuid4()}.png"
        image_path = Path(IMAGES_DIR, args['type'])
        image_path.mkdir(parents=True, exist_ok=True)
        image_path_with_name = Path(
            image_path, image.filename
        ).as_posix()
        image.save(image_path_with_name)

        args.pop('image')
        args['path'] = Path(
            args['type'], image.filename
        ).as_posix()
        Items.insert(args)

        return jsonify({
            'error': False,
            'message': 'saved'
        })


@ns.route('/download/<path:url>')
@ns.expect(basic_args)
class Download(Resource):
    def get(self, url):
        basic_args.parse_args()
        splitted_path = url.split('/')
        image_directory = Path(IMAGES_DIR, *splitted_path[: -1]).as_posix()
        image_name = splitted_path[-1]
        return send_from_directory(
            directory=image_directory,
            filename=image_name
        )

@ns.route('/get-info')
@ns.expect(basic_args)
class GetInfo(Resource):
    @ns.expect(info_args)
    def post(self):
        basic_args.parse_args()
        args = info_args.parse_args()
        response = Items.find_one(args)
        response.pop('_id')

        return jsonify({
            'error': False,
            'result': dict(response)
        })

def register(main_api):
    main_api.add_namespace(ns)
