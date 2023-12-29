import turtle

class AdvancedShape():

    def __init__(self, sides: int, size: int, color: str, start_x: int, start_y: int, start_angle: int = 0):
        self.sides = sides
        self.size = size
        self.color = color
        self.x = start_x
        self.y = start_y
        self.speed = 1
        self.t = turtle.Turtle(shape="classic", visible=False)
        self.t.shape("triangle")
        self.t.resizemode("user")
        self.t.shapesize(self.size, self.size, 5)
        self.current_tilt = start_angle
        self.tilt_direction = 1
        self.max_tilt = 5
        
        # self.t.hideturtle()

    def get_and_change_tilt(self) -> float:

        if self.tilt_direction > 0:
            self.current_tilt += 0.1
            if self.current_tilt >= self.max_tilt:
                self.tilt_direction = 0

        if self.tilt_direction < 1:
            self.current_tilt -= 0.1
            if self.current_tilt <= -self.max_tilt:
                self.tilt_direction = 1
        return self.current_tilt


    def draw(self):
        self.t.up()
        self.t.tilt(self.get_and_change_tilt())
        self.t.showturtle()
        self.t.goto(self.x, self.y)
        # self.t.down()
        self.t.fillcolor(self.color)
        # self.t.begin_fill()
        # for i in range(self.sides):
        #     self.t.forward(self.size)
        #     self.t.left(360 / self.sides)
        # self.t.end_fill()
        pass

    def move_down(self):
        self.y = self.y - self.speed
    
    
        