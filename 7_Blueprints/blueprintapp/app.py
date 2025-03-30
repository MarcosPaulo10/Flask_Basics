from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blueprints.db'

    db.init_app(app)
    
    # import and register all blueprints -------------------------i
    from blueprintapp.blueprints.core.routes import core
    app.register_blueprint(core, url_prefix='/')
    
    from blueprintapp.blueprints.todos.routes import todos
    app.register_blueprint(todos, url_prefix='/todos')
    
    from blueprintapp.blueprints.people.routes import people
    app.register_blueprint(people, url_prefix='/people')
    # ------------------------------------------------------------f
    
    migrate = Migrate(app, db)

    return app