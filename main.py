# Task 17: Import the modules csv, tui and visual
# TODO: Your code here
import csv
from re import search
from tui import *
from visual import *

# Task 18: Create an empty list named 'records'.
# This will be used to store the date read from the source data file.
# TODO: Your code here
records = []


def run():
    # Task 19: Call the function welcome of the module tui.
    # This will display our welcome message when the program is executed.
    # TODO: Your code here
    welcome()

    while True:
        pass
        # Task 20: Using the appropriate function in the module tui, display a menu of options
        # for the different operations that can be performed on the data.
        # Assign the selected option to a suitable local variable
        # TODO: Your code here
        choice = menu()

        # Task 21: Check if the user selected the option for loading data.  If so, then do the following:
        # - Use the appropriate function in the module tui to display a message to indicate that the data loading
        # operation has started.
        # - Load the data (see below).
        # - Use the appropriate function in the module tui to display a message to indicate that the data loading
        # operation has completed.
        #
        # To load the data, it is recommended that you create and call one or more separate functions that do the
        # following:
        # - Use the appropriate function in the module tui to retrieve a file path for the CSV data file.  You
        # should appropriately handle the case where this is None.
        # - Read each line from the CSV file and add it to the list 'records'. You should appropriately handle the case
        # where the file cannot be found
        # TODO: Your code here
        if choice == 1:
            started("[Load Data]")
            file_path = source_data_path()
            if file_path is None:
                pass
            else:
                try:
                    with open(file_path) as file:
                        csv_reader = csv.reader(file)
                        next(csv_reader)
                        for line in csv_reader:
                            records.append(line)
                        completed("[Load Data]")
                except FileNotFoundError:
                    error("The specified file does not exist.")

        # Task 22: Check if the user selected the option for processing data.  If so, then do the following:
        # - Use the appropriate function in the module tui to display a message to indicate that the data processing
        # operation has started.
        # - Process the data (see below).
        # - Use the appropriate function in the module tui to display a message to indicate that the data processing
        # operation has completed.
        #
        # To process the data, it is recommended that you create and call one or more separate functions that do the
        # following:
        # - Use the appropriate function in the module tui to display a menu of options for processing the data.
        # - Check what option has been selected
        #
        #   - If the user selected the option to retrieve an entity then
        #       - Use the appropriate function in the module tui to indicate that the entity retrieval process
        #       has started.
        #       - Use the appropriate function in the module tui to retrieve the entity name
        #       - Find the record for the specified entity in records.  You should appropriately handle the case
        #       where the entity cannot be found.
        #       - Use the appropriate function in the module tui to list the entity
        #       - Use the appropriate function in the module tui to indicate that the entity retrieval process has
        #       completed.
        #
        #   - If the user selected the option to retrieve an entity's details then
        #       - Use the appropriate function in the module tui to indicate that the entity details retrieval
        #       process has started.
        #       - Use the appropriate function in the module tui to retrieve the entity details
        #       - Find the record for the specified entity details in records.  You should appropriately handle the
        #       case where the entity cannot be found.
        #       - Use the appropriate function in the module tui to list the entity
        #       - Use the appropriate function in the module tui to indicate that the entity details retrieval
        #       process has completed.
        #
        #   - If the user selected the option to categorise entities by their type then
        #       - Use the appropriate function in the module tui to indicate that the entity type categorisation
        #       process has started.
        #       - Iterate through each record in records and assemble a dictionary containing a list of planets
        #       and a list of non-planets.
        #       - Use the appropriate function in the module tui to list the categories.
        #       - Use the appropriate function in the module tui to indicate that the entity type categorisation
        #       process has completed.
        #
        #   - If the user selected the option to categorise entities by their gravity then
        #       - Use the appropriate function in the module tui to indicate that the categorisation by entity gravity
        #       process has started.
        #       - Use the appropriate function in the module tui to retrieve a gravity range
        #       - Iterate through each record in records and assemble a dictionary containing lists of entities
        #       grouped into low (below lower limit), medium and high (above upper limit) gravity categories.
        #       - Use the appropriate function in the module tui to list the categories.
        #       - Use the appropriate function in the module tui to indicate that the categorisation by entity gravity
        #       process has completed.
        #
        #   - If the user selected the option to generate an orbit summary then
        #       - Use the appropriate function in the module tui to indicate that the orbit summary process has
        #       started.
        #       - Use the appropriate function in the module tui to retrieve a list of orbited planets.
        #       - Iterate through each record in records and find entities that orbit a planet in the list of
        #       orbited planets.  Assemble the found entities into a nested dictionary such that each entity can be
        #       accessed as follows:
        #           name_of_dict[planet_orbited][category]
        #       where category is "low" if the mean radius of the entity is below 100 and "high" otherwise.
        #       - Use the appropriate function in the module tui to list the categories.
        #       - Use the appropriate function in the module tui to indicate that the orbit summary process has
        #       completed.
        # TODO: Your code here
        if choice == 2:
            started("[Process Data]")
            second_choice = process_type()

            if second_choice == 1:
                started("[Retrieve entity]")
                entity = entity_name()
                entity_found = retrieve_entity(entity)  # calls a separate function at the bottom of the main.py file. Finds the entity in records
                if entity_found is None:
                    error("The specified entity was not found!")
                else:
                    print(entity_found)
                    completed("[Retrieve entity]")
                    
            elif second_choice == 2:
                entity_details_list = []
                started("[Retrieve entity details]")
                entity = entity_details()
                retrieved_entity = retrieve_entity(entity[0])
                if retrieved_entity is None:
                    error("The specified entity was not found!")
                else:
                    for i in entity[1]:
                        entity_details_list.append(retrieved_entity[i])
                    print(entity_details_list)
                    completed("[Retrieve entity details]")

            elif second_choice == 3:
                started("[Categorise entities by type]")
                type_dictionary = categorise_type()  # calls a separate function at the bottom of the main.py file.
                list_categories(type_dictionary)

            elif second_choice == 4:
                started("[Categorise entities by gravity]")
                gravity = gravity_range()
                gravity_dictionary = categorise_gravity(gravity) # calls a separate function at the bottom of the main.py file.
                list_categories(gravity_dictionary)

            elif second_choice == 5:
                started("[Summarise entities by orbit]")
                orbited_entities = orbits()
                print(orbited_entities)

        # Task 23: Check if the user selected the option for visualising data.  If so, then do the following:
        # - Use the appropriate function in the module tui to indicate that the data visualisation operation
        # has started.
        # - Visualise the data (see below).
        # - Use the appropriate function in the module tui to display a message to indicate that the data visualisation
        # operation has completed.
        #
        # To visualise the data, it is recommended that you create and call one or more separate functions that do the
        # following:
        # - Use the appropriate function in the module tui to retrieve the type of visualisation to display.
        # - Check what option has been selected
        #
        #   - if the user selected the option to visualise the entity type then
        #       - Use the appropriate function in the module tui to indicate that the entity type visualisation
        #       process has started.
        #       - Use your code from earlier to assemble a dictionary containing a list of planets and a list of
        #       non-planets.
        #       - Use the appropriate function in the module visual to display a pie chart for the number of planets
        #       and non-planets
        #       - Use the appropriate function in the module tui to indicate that the entity type visualisation
        #       process has completed.
        #
        #   - if the user selected the option to visualise the entity gravity then
        #       - Use the appropriate function in the module tui to indicate that the entity gravity visualisation
        #       process has started.
        #       - Use your code from earlier to assemble a dictionary containing lists of entities grouped into
        #       low (below lower limit), medium and high (above upper limit) gravity categories.
        #       - Use the appropriate function in the module visual to display a bar chart for the gravities
        #       - Use the appropriate function in the module tui to indicate that the entity gravity visualisation
        #       process has completed.
        #
        #   - if the user selected the option to visualise the orbit summary then
        #       - Use the appropriate function in the module tui to indicate that the orbit summary visualisation
        #       process has started.
        #       - Use your code from earlier to assemble a nested dictionary of orbiting planets.
        #       - Use the appropriate function in the module visual to display subplots for the orbits
        #       - Use the appropriate function in the module tui to indicate that the orbit summary visualisation
        #       process has completed.
        #
        #   - if the user selected the option to animate the planet gravities then
        #       - Use the appropriate function in the module tui to indicate that the gravity animation visualisation
        #       process has started.
        #       - Use your code from earlier to assemble a dictionary containing lists of entities grouped into
        #       low (below lower limit), medium and high (above upper limit) gravity categories.
        #       - Use the appropriate function in the module visual to animate the gravity.
        #       - Use the appropriate function in the module tui to indicate that the gravity animation visualisation
        #       process has completed.
        # TODO: Your code here
        if choice == 3:
            started("[Visualise Data]")
            second_choice = visualise()

            if second_choice == 1:
                started("[Entities by type]")
                type_dictionary = categorise_type()  # calls a separate function at the bottom of the main.py file.
                entities_pie(type_dictionary)
                completed("[Entities by type]")

        # Task 28: Check if the user selected the option for saving data.  If so, then do the following:
        # - Use the appropriate function in the module tui to indicate that the save data operation has started.
        # - Save the data (see below)
        # - Use the appropriate function in the module tui to indicate that the save data operation has completed.
        #
        # To save the data, you should demonstrate the application of OOP principles including the concepts of
        # abstraction and inheritance.  You should create an AbstractWriter class with abstract methods and a concrete
        # Writer class that inherits from the AbstractWriter class.  You should then use this to write the records to
        # a JSON file using in the following order: all the planets in alphabetical order followed by non-planets 
        # in alphabetical order.
        # TODO: Your code here

        # Task 29: Check if the user selected the option for exiting.  If so, then do the following:
        # break out of the loop
        # TODO: Your code here

        # Task 30: If the user selected an invalid option then use the appropriate function of the module tui to
        # display an error message
        # TODO: Your code here


def retrieve_entity(entity):
    for i in range(len(records)):
        for j in range(len(records[i][0])):
            if records[i][j] == entity:
                entity_record = records[i]
                return entity_record


def categorise_type():
    entity_by_type = {'Planets': [], 'Non Planets': []}
    for i in range(len(records)):
        if records[i][1] == 'FALSE':
            entity_by_type['Non Planets'].append(records[i][0])
        else:
            entity_by_type['Planets'].append(records[i][0])
    return entity_by_type


def categorise_gravity(gravity_range):
    entity_by_gravity = {'Low': [], 'Medium': [], 'High': []}
    for i in range(len(records)):
        if float(records[i][8]) < gravity_range[0]:
            entity_by_gravity['Low'].append(records[i][0])
        elif float(records[i][8]) > gravity_range[1]:
            entity_by_gravity['High'].append(records[i][0])
        else:
            entity_by_gravity['Medium'].append(records[i][0])
    return entity_by_gravity


def summarise_orbit():
    entity_by_gravity = {}


if __name__ == "__main__":
    run()
