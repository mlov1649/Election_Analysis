import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object.
     print(election_data)



# To do: perform analysis.


# Open the election results and read the file.
election_data = open(file_to_load, 'r')


# Close the file. Make sure to use this when not using the WITH function to open 
election_data.close()


import datetime
# Use the now() attribute on the datetime class to get the present time.
now = datetime.datetime.now()
# Print the present time.
print("The time right now is ", now)
