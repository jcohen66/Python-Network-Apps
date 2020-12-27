import matplotlib.pyplot as pyp
import matplotlib.animation as animation

# Create a new figure
figure = pyp.figure()

# Create a subplot with 1 row, 1 column and index 1
# This means a single subplot in our figure
subplot = figure.add_subplot(1, 1, 1)

# Create the function that reads the data from cpu.txt and feeds it to our subplot
def animation_function(i):
    # Open the file and read each cpu utilization
    cpu_data = open("C:\\temp\\cpu.txt", "r").readlines()

    # Load the CPU utilizations into the x-axis
    x = []
    for each_value in cpu_data:
        # Exclude blank lines.
        if len(each_value) > 1:
            cpu = each_value.replace('\n','').split(',')[1]
            x.append(float(cpu))

    subplot.clear()

    subplot.plot(x)


# Set the update figure, function and update interval to animation.
graph_animation = animation.FuncAnimation(figure, animation_function, interval = 10000)

# Display the graph to the screen
pyp.show()
