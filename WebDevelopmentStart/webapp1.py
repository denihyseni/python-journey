from flask import Flask
import random


app = Flask(__name__)
random_number = random.randint(0,9)


@app.route("/")
def hello_world():
    return ("<h1 style='text-align: left'>Guess a number between 0-9</h1>"
            "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' >"
            )

@app.route("/<int:number>")
def guess_number(number):
        if random_number == number:
            return ("<h1 style='color:green;'>Correct guess!</h1>"
                    "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExaTBxZ2NydzVzbnBuY3d2d3J2NmIwYTRmM3hsa3B2a2pwOTEzcnFiMCZlcD12MV9naWZzX3RyZW5kaW5nJmN0PWc/kyLYXonQYYfwYDIeZl/giphy.gif'>")
        elif random_number < number:
            return ("<h1 style='color:purple;'>Too high!</h1>"
                    "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExN2NqdTRtazBpbzVybWJpdGtqenVsamV2cXl1ODV0ODRlaGx0d3doMSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/19gjcpEUzbIRJ5OpcQ/giphy.gif'>")
        else:
            return ("<h1 style='color:red;'>Too low!</h1>"
                    "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExeXpqemJ3cDZmY3FraHZicmgwOTBuNXhtZjR5Z3ZzcXk0MjRjZG40ZSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/PR3585ZZSvcHO9pa76/giphy.gif'>")
















if __name__ == "__main__":
    app.run(debug=True)