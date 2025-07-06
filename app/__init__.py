from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint

from .blueprints.customer import customer_bp
from .blueprints.inventory import inventory_bp
from .blueprints.mechanics import mechanics_bp
from .blueprints.service_tickets import service_tickets_bp
from .extensions import cache, limiter, ma
from .models import db

SWAGGER_URL = "/api/docs"
API_URL = "/static/swagger.yaml"

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={"app_name": "Repair Shop Database"},
)


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(f"config.{config_name}")

    # initialize extensions
    ma.init_app(app)
    db.init_app(app)
    limiter.init_app(app)
    cache.init_app(app)

    # register blueprints
    app.register_blueprint(customer_bp, url_prefix="/customers")
    app.register_blueprint(inventory_bp, url_prefix="/inventory")
    app.register_blueprint(mechanics_bp, url_prefix="/mechanics")
    app.register_blueprint(service_tickets_bp, url_prefix="/service_tickets")
    # app.register_blueprint(
    #     archived_service_tickets_bp,
    #     url_prefix="/archived_service_tickets",
    # )
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

    return app
