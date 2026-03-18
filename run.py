from app.routes import app
from database.db import init_db

if __name__ == "__main__":
    init_db()
    app.run(debug=False, use_reloader=False)
