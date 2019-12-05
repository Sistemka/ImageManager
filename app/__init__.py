from app.app import api
from app.handlers import (
    errors,
    image
)

image.register(api)
errors.register()
