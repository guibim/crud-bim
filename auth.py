from flask import Blueprint, render_template_string, request, redirect, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from db import get_conn

bp = Blueprint("auth", __name__)

LOGIN_HTML = """
<!doctype html>
<title>Login</title>
<h2>Login</h2>
<form method="post">
  <label>Username</label><input name="username" required>
  <label>Password</label><input type="password" name="password" required>
  <button type="submit">Entrar</button>
</form>
<p style="color:red;">{{ msg }}</p>
"""

@bp.route("/login", methods=["GET","POST"])
def login():
    msg = ""
    if request.method == "POST":
        u = request.form.get("username","").strip()
        p = request.form.get("password","")
        conn = get_conn()
        row = conn.execute(
            "SELECT id, username, password_hash, role FROM users WHERE username = ?",
            (u,)
        ).fetchone()
        conn.close()
        if row and check_password_hash(row["password_hash"], p):
            session["user_id"] = row["id"]
            session["username"] = row["username"]
            session["role"] = row["role"]
            return redirect(url_for("index"))
        msg = "Credenciais inválidas."
    return render_template_string(LOGIN_HTML, msg=msg)

@bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.login"))

def create_user(username, email, password, role="MEMBRO"):
    conn = get_conn()
    conn.execute(
        "INSERT INTO users(username,email,password_hash,role) VALUES(?,?,?,?)",
        (username, email, generate_password_hash(password), role),
    )
    conn.commit()
    conn.close()
