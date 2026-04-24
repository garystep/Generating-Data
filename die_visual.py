import plotly.express as px

from die import Die

# Create a D6
die = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# Analyze the results.
frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)


# Visualize the results.
title = "Results of rolling a D6 1000 times"
labels = {"x": "Result", "y": "Frequency"}
fig = px.bar(x=range(1, die.num_sides + 1), y=frequencies, title=title, labels=labels)
fig.show()