from turtle import Turtle
TOP_Y = 270
ALIGN = "center"
FONT = ("Courier", 24, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt",mode="r") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,TOP_Y)
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score} High Score: {self.high_score}", False, align=ALIGN, font=FONT)


    def reset(self):
        if self.score > self.high_score:
            with open("data.txt",mode="w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()


    #def game_over(self):
        #self.home()
        #self.write("Game Over...", False, align=ALIGN, font=FONT)

    def score_counter(self):
            self.score+=1
            self.update_scoreboard()