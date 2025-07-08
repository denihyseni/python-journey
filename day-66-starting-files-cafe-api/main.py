from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from pandas.core.computation.expressions import where
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean , select
import random


'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)
    #
    def to_dict(self):
    #     # Method 1.
    #     dictionary = {}
    #     # Loop through each column in the data record
    #     for column in self.__table__.columns:
    #         # Create a new dictionary entry;
    #         # where the key is the name of the column
    #         # and the value is the value of the column
    #         dictionary[column.name] = getattr(self, column.name)
    #     return dictionary
    #
        # Method 2. Altenatively use Dictionary Comprehension to do the same thing.
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


    # @app.route("/random")
    # def get_random_cafe():
    #     result = db.session.execute(db.select(Cafe))
    #     all_cafes = result.scalars().all()
    #     random_cafe = random.choice(all_cafes)
    #     # Simply convert the random_cafe data record to a dictionary of key-value pairs.
    #     return jsonify(cafe=random_cafe.to_dict())


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random",methods=["GET"])
def get_random_caffe():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    random_cafe = random.choice(all_cafes)
    return jsonify(cafe={
        "id": random_cafe.id,
        "name": random_cafe.name,
        "map_url": random_cafe.map_url,
        "img_url": random_cafe.img_url,
        "location": random_cafe.location,
        "seats": random_cafe.seats,
        "has_toilet": random_cafe.has_toilet,
        "has_wifi": random_cafe.has_wifi,
        "has_sockets": random_cafe.has_sockets,
        "can_take_calls": random_cafe.can_take_calls,
        "coffee_price": random_cafe.coffee_price,
    }
    )

@app.route("/all",methods=["GET"])
def get_all_caffe():
    result = db.session.execute(db.select(Cafe))
    db_cafe = result.scalars().all()
    all_cafes=[]
    for n in db_cafe:
        i = {column.name: getattr(n, column.name) for column in n.__table__.columns}
        all_cafes.append(i)

    return jsonify(cafe=all_cafes)

@app.route("/search",methods=["GET"])
def search_all_cafes():
    loc = request.args.get("loc")
    cafe_location = []

    if not loc:
        return jsonify(error={
            "Not Found":"Sorry , We Dont have a cafe at that location"
        })
    else:
        cl = select(Cafe).where(Cafe.location == loc)
        cafe = db.session.execute(cl).scalars().all()

        cafe_location = [
            {column.name: getattr(n, column.name) for column in n.__table__.columns}
            for n in cafe
        ]

        return  jsonify(cafes=cafe_location)






# HTTP POST - Create Record

@app.route("/add", methods=["POST"])
def post_new_cafe():
    # Validate required fields
    name = request.form.get("name")
    if not name:
        return jsonify(error="Cafe name is required."), 400

    # Parse booleans carefully
    def str_to_bool(val):
        return str(val).lower() in ("true", "1", "yes")

    try:
        seats = int(request.form.get("seats", 0))
    except ValueError:
        return jsonify(error="Seats must be a valid integer."), 400

    new_cafe = Cafe(
        name=name,
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=str_to_bool(request.form.get("sockets")),
        has_toilet=str_to_bool(request.form.get("toilet")),
        has_wifi=str_to_bool(request.form.get("wifi")),
        can_take_calls=str_to_bool(request.form.get("calls")),
        seats=seats,
        coffee_price=request.form.get("coffee_price"),
    )

    try:
        db.session.add(new_cafe)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify(error="Failed to add cafe. " + str(e)), 500

    return jsonify(response={"success": "Successfully added the new cafe."})


# HTTP PUT/PATCH - Update Record

@app.route("/update-price/<cafe_id>",methods=["PATCH"])
def patch_all_cafes(cafe_id):
    cafe = db.session.get(Cafe, cafe_id)
    new_price= request.args.get("new_price")

    if cafe is None:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    else:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."}), 200


# HTTP DELETE - Delete Record
@app.route("/report-closed/<cafe_id>",methods=["DELETE"])
def delete_cafe(cafe_id):
    cafe = db.session.get(Cafe,cafe_id)
    password = "TopSecretAPIKey"
    api_key = request.args.get("api_key")

    if cafe is None:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    else:
        if password == api_key:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(success={"Success":"Cafe was successfully deleted"}),200
        else:
            return jsonify(error={"Incorrect Key":"You dont have the correct key"}),403



if __name__ == '__main__':
    app.run(debug=True)
