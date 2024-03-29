** Introduction **
Automation in gene annotation is needed because it cuts down the manual
workload greatly. According to a research article published in BMC
Bioinformatics, semi-automating gene annotation comparisons decreased
manual comparison to only 13% of the gene. In this project, we explore
semi-automating the comparison of gene annotations. The purpose of this
project is to compare the gene annotations between two releases of a
specified gene. In our project, we used the mouse genome between
ENSEMBL release 82 and release 98.

We had five questions that we wanted to answer with our project. The
questions were as follows:
  1. How many different categories of genes are there and what are their
     counts?
  2. How many transcripts are annotated in release 82, release 98, and
     in total?
  3. What are the transcript numbers associated with each gene category?
  4. What are the genes and transcripts annotated in release 82?
  5. What are the genes and transcripts annotated in release 98?

** Setting up the website **
The easiest way to replicate this website is clone the git repository.
The repository is located at:
https://github.com/overbejt/Bio-Info-GRP-1093324.git

Once the repository is cloned, the website ready to go.  To build the
website manually, refer to the section ** Setting up the Database **,
below.  Once the database is setup, put the files: about.html,
ano-transc-cnt.py, cat-count.py, gene-cat-trans.py, gt82.py, gt98.py,
index.html, min-max.py, results.py, search.py into your public_html
folder.  You will also need to move the folders: css/ and images/ to
your public_html folder.  Then the website should be ready to go.

** File Structure **
- css/
    - bio.css
- images/
    - Miami_Redhawks_logo.svg
    - josh-at-graduation.jpg
    - julia-at-pelotonia.JPG
- setup/
    - creatDbII.sql
    - dbData.txt
    - loadcmd.txt
    - Mus_musculus.GRCm38.82.chr.gtf
    - Mus_musculus.GRCm38.98.chr.gtf
    - py2html.py
    - tabS.py
- templates/
    - ano-transc-cnt.html
    - cat-count.html
    - gene-annotation.html
    - gene-cat-trans.html
    - gt82.html
    - gt98.html
    - min-max.html
    - search.html
- about.html
- ano-transc-cnt.py
- cat-count.py
- gene-cat-trans.py
- gt82.py
- gt98.py
- index.html
- min-max.py
- results.py
- search.py

*All of the files needed to set things are are in the folder called
'setup'.

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
needed.  The file containing the data for the database is setup/dbData.txt

** Trouble Shooting **
If the web pages fail to load, check their permissions.  You may have to
change them using the command:
$ chmod a+rx *.py




