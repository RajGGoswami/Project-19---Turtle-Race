# Day 19 – Turtle Race
# This project simulates a simple racing game where multiple turtles
# move forward at random speeds until one reaches the finish line.

from turtle import Turtle, Screen
import random

# Controls whether the race loop should keep running
is_race_on = False

# Screen setup for the race track
# Defines the size of the window where the race will be displayed
screen = Screen()
screen.setup(width=500, height=400)

# Prompt the user to place a bet on which turtle will win
# This creates player interaction and determines the final result message
user_bet = screen.textinput(
    title="Make your bet",
    prompt="Which turtle will win the race? Enter a color: "
)

# Predefined turtle colors (each turtle represents a racer)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Stores all turtle objects so they can be controlled as a group
all_turtles = []

# Starting y-axis position for the first turtle
# Each turtle is vertically spaced so they appear in separate lanes
y_axis = -90

# Create and position each turtle racer
for color in colors:
    # Create a turtle object with a turtle shape
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(color)
    new_turtle.penup()  # Prevents drawing lines while moving to start position
    new_turtle.goto(x=-230, y=y_axis)

    # Move the next turtle slightly higher to form a race lineup
    y_axis += 30

    # Store the turtle so it can participate in the race loop
    all_turtles.append(new_turtle)

# Start the race only if the user placed a bet
if user_bet:
    is_race_on = True

# Main race loop
# Each turtle moves forward by a random distance on every iteration
while is_race_on:
    for turtle in all_turtles:

        # Check if the turtle has crossed the finish line
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()

            # Compare the winning turtle with the user's bet
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        # Move the turtle forward by a random amount
        # This randomness simulates different speeds in the race
        rand_distance = random.randint(1, 10)
        turtle.forward(rand_distance)

# Keeps the window open until the user clicks
screen.exitonclick()
