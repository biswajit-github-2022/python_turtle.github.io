from turtle import Screen, Turtle
from random import randint, choice
from functools import partial
from time import sleep

INFECTION_DISTANCE = 30
PERSON_RADIUS = 8
WIDTH, HEIGHT = 500, 500
CURSOR_SIZE = 20

possessed = 0

class Person(Turtle):
    population = []

    def __init__(self):
        super().__init__(shape='circle')

        self.shapesize(PERSON_RADIUS / CURSOR_SIZE)
        self.penup()
        self.setpos(randint(-WIDTH/2, WIDTH/2), randint(-HEIGHT/2, HEIGHT/2))

        Person.population.append(self)

    @classmethod
    def all_infected(cls):
        return [person for person in cls.population if person.infected()]

    def infect(self):
        self.color('red')

    def infected(self):
        return self.pencolor() == 'red'

    @classmethod
    def all_healthy(cls):
        return [person for person in cls.population if not person.infected()]

    def possess(self):
        self.color('green')

    def possessed(self):
        return self.pencolor() == 'green'

    def random_move(self):
        self.right(randint(-90, 90))
        self.forward(randint(0, 10))

        x, y = self.position()

        if not (PERSON_RADIUS - WIDTH/2 < x < WIDTH/2 - PERSON_RADIUS and PERSON_RADIUS - HEIGHT/2 < y < HEIGHT/2 - PERSON_RADIUS):
            self.undo()  # this will undo forward()

def make_population(amount):
    for _ in range(amount):
        Person()

def possess_random():
    possessed = None

    healthy = Person.all_healthy()

    if healthy:
        possessed = choice(healthy)
        possessed.possess()

        screen.onkey(partial(move_up, possessed), 'Up')
        screen.onkey(partial(move_down, possessed), 'Down')
        screen.onkey(partial(move_right, possessed), 'Right')
        screen.onkey(partial(move_left, possessed), 'Left')

    return possessed

def infect_random():
    person = None

    healthy = Person.all_healthy()

    if healthy:
        person = choice(healthy)
        person.infect()

    return person

def check_infection(person):
    for infected in Person.all_infected():
        if person.distance(infected) < INFECTION_DISTANCE:
            is_possessed = person.possessed()

            person.infect()

            if is_possessed:
                possess_random()

def simulation(amount, moves):
    """ This will simulate the virus outbreak scenarios (quarantine, or not quarantine) """
    make_population(amount)

    infect_random()
    possess_random()
    screen.update()

    for _ in range(moves):
        for person in Person.population:
            if not person.possessed():
                person.random_move()

            if not person.infected():
                check_infection(person)

        screen.update()
        sleep(0.1)

def move_up(possessed):
    y = possessed.ycor() + 10

    if y < HEIGHT/2 - PERSON_RADIUS:
        possessed.sety(y)
        check_infection(possessed)

def move_down(possessed):
    y = possessed.ycor() - 10

    if y > PERSON_RADIUS - HEIGHT/2:
        possessed.sety(y)
        check_infection(possessed)

def move_right(possessed):
    x = possessed.xcor() + 10

    if x < WIDTH/2 - PERSON_RADIUS:
        possessed.setx(x)
        check_infection(possessed)

def move_left(possessed):
    x = possessed.xcor() - 10

    if x > PERSON_RADIUS - WIDTH/2:
        possessed.setx(x)
        check_infection(possessed)

amount = int(input("Enter amount of people within the area: "))
moves = int(input("Enter the amount of moves these people will do: "))

screen = Screen()
screen.setup(WIDTH, HEIGHT)

screen.listen()
screen.tracer(False)

simulation(amount, moves)

screen.tracer(True)
screen.exitonclick()