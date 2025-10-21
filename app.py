import os
from flask import Flask, redirect, url_for, session
from db import init_db
from auth import bp as auth_bp

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "change-me")
    init_db()
    app.register_blueprint(auth_bp, url_prefix="")

    @app.route("/")
    def index():
        if "user_id" not in session:
            return redirect(url_for("auth.login"))
        return f"Olá, {session.get('username')}! Papel: {session.get('role')}."
    return app

app = create_app()

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
