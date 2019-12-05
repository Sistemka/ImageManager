from app.app import api
from app.handlers import (
    errors,
    image,
    url
)

image.register(api)
url.register(api)
errors.register()
