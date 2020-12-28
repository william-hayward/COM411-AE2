import matplotlib.pyplot as plt


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

