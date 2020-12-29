import matplotlib.pyplot as plt
import matplotlib.animation as animation


def entities_pie(categories):
    """
    Task 24: Display a single subplot that shows a pie chart for categories.

    The function should display a pie chart with the number of planets and the number of non-planets from categories.

    :param categories: A dictionary with planets and non-planets
    :return: Does not return anything
    """
    labels = 'Planets', 'Non Planets'
    sizes = [len(categories['Planets']), len(categories['Non Planets'])]
    colours = ['yellowgreen', 'lightcoral']
    outline = {"linewidth": 1, "edgecolor": "black"}
    plt.pie(sizes, labels=labels, autopct="%1.1f%%", colors=colours, wedgeprops=outline)
    plt.title("A Pie Chart To Show Planets vs Non Planets")
    plt.tight_layout()
    plt.show()


def entities_bar(categories):
    """
    Task 25: Display a single subplot that shows a bar chart for categories.

    The function should display a bar chart for the number of 'low', 'medium' and 'high' gravity entities.

    :param categories: A dictionary with entities categorised into 'low', 'medium' and 'high' gravity
    :return: Does not return anything
    """
    labels = ['Lower', 'Medium', 'Higher']
    sizes = [len(categories['Low']), len(categories['Medium']), len(categories['High'])]
    colours = ['palegreen', 'lightcoral', 'lightskyblue']

    plt.bar(labels, sizes, width=0.5, color=colours, edgecolor='black')

    plt.ylabel("Number of entities", fontsize=14, fontweight='bold')
    plt.xlabel("Gravity Range", fontsize=14, fontweight='bold')
    plt.title("A Bar Chart To Show The Range of Gravity", fontsize=14, fontweight='bold')

    plt.tight_layout()
    plt.show()


def visualise_orbits(summary):
    """
    Task 26: Display subplots where each subplot shows the "small" and "large" entities that orbit the planet.

    Summary is a nested dictionary of the form:
    summary = {
        "orbited planet": {
            "small": [entity, entity, entity],
            "large": [entity, entity]
        }
    }

    The function should display for each orbited planet in summary. Each subplot should show a bar chart with the
    number of "small" and "large" orbiting entities.

    :param summary: A dictionary containing the "small" and "large" entities for each orbited planet.
    :return: Does not return anything
    """


def gravity_animation(categories):
    """
    Task 27: Display an animation of "low", "medium" and "high" gravities.

    The function should display a suitable animation for the "low", "medium" and "high" gravity entities.
    E.g. an animated line plot

    :param categories: A dictionary containing "low", "medium" and "high" gravity entities
    :return: Does not return anything
    """
    # code attempted - code does not work as intended
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3)

    def animate(frame):
        plt.suptitle("Animation of Low, Medium and High Gravities")
        for i in categories['Low']:
            ax1.set_xlabel("Low")
            ax1.set_yticks([])
            ax1.set_xticks([])
            ax1.plot(i, i, 'g--o', markersize=2)
        for i in categories['Medium']:
            ax2.set_xlabel("Medium")
            ax2.set_yticks([])
            ax2.set_xticks([])
            ax2.plot(i, i, 'r--o', markersize=2)
        for i in categories['High']:
            ax3.set_xlabel("High")
            ax3.set_yticks([])
            ax3.set_xticks([])
            ax3.plot(i, i, 'b--o', markersize=2)

    some_animation = animation.FuncAnimation(fig, animate, frames=10, interval=1000)
    plt.show()
