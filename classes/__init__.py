import os
from dotenv import load_dotenv
from flask import Flask


def create_app(test_config=None):
    load_dotenv()
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="os.environ.get(DEV_KEY)",
        DATABASE=os.path.join(app.instance_path, 'class-db.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    
    from .data import db
    db.init_app(app)

    
    from . import createClasses
    app.register_blueprint(createClasses.bp)

    from . import accessClasses
    app.register_blueprint(accessClasses.bp)

    
    return app