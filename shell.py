from practice import create_app, db, cli
from practice.models import User, Post

app = create_app()
cli.register(app)

@app.shell_context_processor
def make_shell_context():
    return {'db':db, 'User':User, 'Post':Post}