# visualize-csv
Codes here are a sample of visualization of CSV file using python under the simple CGI setting.
One can use these codes for making easily to check the contents of a CSV file and it allows a few modifications on the CSV at the same time.

There are two sets of codes as follows for modifying CSV on a browser and generating an HTML consisting of a table of the CSV and its graphs of numerical data.
[Set1]
This set plays a role in editing a CSV on a browser.
1. form.html
2. style.css
3. csv2table.py
4. edit_table.py

The functionalities available in the former set are as follows:
1. Delete several columns from the table by listing up the header (label of each column) with a comma-separated format as well as CSV. It is noted that any spaces must not be involved in the list of columns.
2. Pick up and show several columns in contrast to 1 in the same manner of the above.
3. Download link for the current (modified) table.

These codes are developed and confirmed with work on firefox in the following environment.
OS: Ubuntu 18.04.3 LTS
Server version: Apache/2.4.29
Python version: 3.6.9
Pandas version: 0.25.3

[Set2]
This set plays a role in generating HTML for helping visualization.
It is noted that the code 'generate_html.py' uses matplotlib to plot the contents of a table. 
1. generate_html.py
2. okayama_weatherdata.csv (This is a sample data)
