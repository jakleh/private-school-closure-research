I wrote this program to identify 700+ California and Pennsylvania private schools as either open or closed. Each state has its own department of
education with a website that identifies private schools as either open or closed. Hence, since each website maintains a consistent layout for 
each school search, I was able to use web scraping in order to identify the activity status of each school.

The entire program is written in Python.

excelExtraction.py generates a list of tuples containing relevant information about each school so that the web scraping program can properly search
for each school using the searchbar provided by each site.

stateScraping.py uses Selenium (python package) to search for each school, isolate the HTML element which corresponds to said school's activity status, 
create an output excel file, and then write said activity status to the output file as either a "0" [for closed] or a "1" [for open].

functions.py provides the functions necessary to carry out the tasks relegated to stateScraping.py.

