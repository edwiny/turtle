import turtle
import random
import time

from shape import AdvancedShape

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500



def on_click_handler(x: int, y: int):
    global done
    global screen
    done = True

def spawn_shape():
    global SCREEN_HEIGHT, SCREEN_HEIGHT
    global shapes
    shapes.append(AdvancedShape(sides=random.randint(3, 16), 
                              size=random.randint(1, 10),
                              color=random.choice(["red", "yellow", "green", "blue"]),
                              start_x=random.randint(-SCREEN_WIDTH, SCREEN_WIDTH),
                              start_y=SCREEN_HEIGHT,
                              start_angle=random.randint(-10, 10)
                              )
    )


screen = turtle.Screen()

screen.screensize(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.onclick(on_click_handler)
#screen.ontimer(spawn_shape, 10)

# setup shapes

shapes: list[AdvancedShape] = []


done = False

next_draw_time  = 0
next_spawn_time = 0
while not done:
    current_time = time.perf_counter_ns()


    if current_time > next_spawn_time:

        next_spawn_time = current_time + 100000000

        if len(shapes) < 100:
            spawn_shape()
        

    if current_time >= next_draw_time:
        next_draw_time = current_time + 60000

        
        screen.tracer(0)
        for shape in shapes:
            shape.draw()
            shape.move_down()
            if shape.y < -(SCREEN_HEIGHT + 20):
                shapes.remove(shape)

        screen.update()

                              
    #turtle_lib.draw_shape(turtle, random.randint(20, 100), random.randint(-SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2), random.randint(-SCREEN_HEIGHT / 2, SCREEN_HEIGHT / 2), random.randint(3,10))


#for i in range(10):
#    turtle_lib.snowflake(turtle, random.randint(20, 100), random.randint(-SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2), random.randint(-SCREEN_HEIGHT / 2, SCREEN_HEIGHT / 2))


#screen.mainloop()


