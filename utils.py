## This module contains utility functions for the project.


def create_columns(column_map, path):
    ## Create from a dictionary column_map a column.txt file in the path directory
    ## The map is separated by -> arrow
    with open(path + "/columns.txt", "w") as f:
        for key, value in column_map.items():
            f.write(key + " -> " + value + "\n")
