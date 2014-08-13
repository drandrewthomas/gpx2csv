#GPX2CSV for Python 2

I've got one of those tiny IgotU GPS trackers that can be used for photo-logging, but which is also really handy for general waypointing because it's so easy and quick to use. The TripPC software that comes with it can export tracks to the GPX format, which makes it really easy for me to view files on my PC or Android tablet. But, quite often, I want to create a CSV file containing the waypoints for use in spreadsheets or coding work.

For that reason I decided to write GPX2CSV as a Python command line tool that reads through all GPX file waypoint child elements and saves them in a CSV file (with the same file name, plus '.csv' tagged on the end). I've only used it with TripPC exported files, but I imagine it should work with most GPX files, although if it's not robust enough for foibles in file structure it should be pretty easy to modify to new needs. I wrote it using Python 2, but only minor changes should be needed to make it work on v3 if you prefer.

To use it you'll obviously need to add the file location to your path environment variable. In a terminal you can then just run commands such as 'gpx2csv.py ./mygpxfile.gpx'.
