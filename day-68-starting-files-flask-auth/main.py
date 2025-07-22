from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

# CREATE DATABASE


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

# CREATE TABLE IN DB


class User(db.Model,UserMixin):

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))

with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html")

@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User,user_id)


@app.route('/register',methods=["GET","POST"])
def register():

        email_exists = User.query.filter_by(email=request.form.get('email')).first()
        if request.method == "POST":
            if email_exists:
                flash("User already exists", 'error')
                return redirect(url_for("login"))
            else:
                hash_salt_pass = generate_password_hash(
                    request.form.get('password'),
                        method='pbkdf2:sha256',
                        salt_length=8
                )
                new_user = User(
                        email=request.form.get('email'),
                        name=request.form.get('name'),
                        password=hash_salt_pass
                )

                db.session.add(new_user)
                db.session.commit()
                login_user(new_user)

                return redirect(url_for("secrets"))


        return render_template("register.html")

@app.route('/login',methods=["GET","POST"])
def login():

    form_password = request.form.get('password')
    email_from_form = request.form.get('email')
    user = User.query.filter_by(email=email_from_form).first()

    if request.method == "POST":
        if user is None:
            flash("User doesnt exist",'error')
            return redirect(url_for("login"))
        elif not check_password_hash(user.password,form_password):
            flash("Wrong password",'error')
            return redirect(url_for("login"))
        else:
            flash("Successful login!",'success')
            login_user(user)
            return redirect(url_for('secrets'))
    else:
        return render_template("login.html")


@app.route('/secrets',methods=["GET"])
@login_required
def secrets():
    print(current_user.is_authenticated)
    return render_template("secrets.html")


@app.route('/logout',methods=["GET"])
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/download/<filename>')
@login_required
def download(filename):
    return send_from_directory(
        "static/files",filename
    )


if __name__ == "__main__":
    app.run(debug=True)