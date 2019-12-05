All of the files needed to set things are are in the folder called 'setup'.
The folder 'setup' includes:
  - py2html.py
  - tabS.py
  - creatDbII.sql  
  - loadcmd.txt 
 
** Designing the website **
Designing a website using python cgi was challenging.  So, we designed the
site using html.  This is why we made the python script py2html.py.  When 
you run it, you can pass the path to an html file to it, and it will convert
the html to a python file ready for cgi.

** Processing the data **
We need a way to take the supplied data and put it into file format that 
mysql can work with.  For this, we created the tabS.py python script.  It 
takes in the filename, (one file per run), processes the data, and then 
appends it to a file called dbData.txt.  When you finish processing the 
data, you are ready to fill the database.  All of these files can be found 
in the 'setup/' folder.

** Setting up the Database **
All of the files needed to set the database can be found in the setup/ 
folder.  To create the table, you can use the contents from the file 
'createDbII.sql'.  After processing the data, you will have a file called 
dbData.txt.  To load the data into the database, copy the command from the 
file 'loadcmd.txt'.  Change the user name and table, in the command, as 
needed. 

** Trouble Shooting **
If the web pages fail to load, check their permissions.  You may have to 
change them using the command: 
$ chmod u+rx,g+rx,o+rx *.py
  



