# almanac-xml-export
Barebones, hideous Django project to take in an almanac database and export 50 state files + related pictures

The project assumes that current almanac data has been ported into the Django project
Once that's been completed, visiting 127.0.0.1:8000/check/ will begin a file creation and export process
You won't see anything in the web browser, but in your console that's running the current Django server, you'll see progress information
If something goes wrong, the project is still in debug mode, so you should be able to 

#Structure
There isn't much of one. The base URL calls a function in the xml_dump module called "check_states" which iterates through states.
For the most enlightening view of what I'm doing on the Python side of things, check out xml_dump/views.py

#Notes
I sort of built it under the assumption that it was possible, but not enitrely likely, that it'd have to be used again
With this in mind, other people looking through the code might have a hard time seeing what I'm doing, but I figured I'd be around until well after the Almanac project in its current form goes obsolete
