# Python calculate_average Function Bug
This repository contains a demonstration of a common error in Python functions that deal with numeric data: improper handling of non-numeric input.

The `calculate_average` function is designed to calculate the average of a list of numbers. However, if the input list contains any non-numeric elements (such as strings or other data types), it will raise a `TypeError` exception.

The solution provided addresses this by first checking if all elements in the list are numbers before performing the calculation. If not, an appropriate error message is displayed, and 0 is returned if the list is empty.