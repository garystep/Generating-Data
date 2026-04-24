import plotly.express as px

from die import Die
import die

# Create a D6
die_1 = Die()
die_2 = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results.
frequencies = []
for value in range(2, 2 * die_1.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)


# Visualize the results.
title = "Results of rolling two D6 1000 times"
labels = {"x": "Result", "y": "Frequency"}
fig = px.bar(x=range(2, 2 * die_1.num_sides + 1), y=frequencies, title=title, labels=labels)
fig.show()