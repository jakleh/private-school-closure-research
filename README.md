I wrote this program to identify 1000+ California and Pennsylvania private schools as either open or closed. Each state has its own department of
education with a website that identifies private schools as either open or closed. Hence, since each website maintains a consistent layout for 
each school search, I was able to use web scraping in order to identify the activity status of each school.

The entire program is written in Python.

excelExtraction.py generates a list of tuples containing relevant information about each school so that the web scraping program can properly search
for each school using the searchbar provided by each site.

stateScraping.py uses Selenium (python package) to search for each school, isolate the HTML element which corresponds to said school's activity status, 
create an output excel file, and then write said activity status to the output file as either a "0" [for closed] or a "1" [for open].

functions.py provides the functions necessary to carry out the tasks relegated to stateScraping.py.

***

To run the program:

1. Download the excel file that contains the list of private schools: https://drive.google.com/file/d/1rpzqA5fDkH7ROVio18nuTpmVgkhK7FKB/view?usp=sharing.
2. Save the downloaded file to the directory containing the program.
3. Navigate to said directory.
4. Generate the proper list of tuples by running "python3 excelExtraction.py" in the terminal.
5. Run "python3 stateScraping.py" in the terminal and then type either "Ca" or "Pa" depending on which state you'd like to scrape.

Happy scraping!

***

Here is the list of sources that I used to build this project:

• https://www.browserstack.com/guide/locators-in-selenium
• https://www.youtube.com/watch?v=OjyDAxK720Q
• https://stackabuse.com/reading-and-writing-excel-files-in-python-with-the-pandas-library
• https://www.youtube.com/watch?v=knnhkraHsBg
• https://www.youtube.com/watch?v=-stXyMIrsck
• https://www.youtube.com/watch?v=eDrFWRi13DY
• https://selenium-python.readthedocs.io/locating-elements.html

