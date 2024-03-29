#!/usr/bin/env python3
import pymysql.cursors
import pymysql
import cgi
import cgitb
cgitb.enable()

# Create an instance of the FieldStorage
form = cgi.FieldStorage()

# Get the names
gene_name = form.getvalue('gene_form')
trans_name = form.getvalue('transcript_form')

# Connect to the database
conn = pymysql.connect(host='localhost',
                       user='overbejt',
                       password='bio466',
                       cursorclass=pymysql.cursors.DictCursor)

# Print the HTML out
print('Content-Type: text/html')
print('')
print('<!DOCTYPE html>')
print('<html lang="en">')
print('<head>')
print('<meta charset="UTF-8">')
print('<meta name="description" content="This is for the final project in BIO 466">')
print('<meta name="author" content="Josh Overbeck">')
print('<meta name="author" content="Julia Timko">')
print('<meta name="keywords" content="Bioinformatics Computer Science Gene annotation">')
print('<meta name="contact" content="overbejt@miamioh.edu">')
print('<meta name="contact" content="timkojm@miamioh.edu">')
print('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
print('<link rel="stylesheet" type="text/css" href="css/bio.css">')
print('<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">')
print('<title>BIO 466</title>')
print('</head>')
print('<body>')
print('<!-- navigation -->')
print('<nav class="navbar navbar-expand-lg navbar-dark bg-dark">')
print('<a class="navbar-brand" href="#">')
print('<img src="images/Miami_Redhawks_logo.svg" alt="Miami Redhawks logo" class="logo">')
print('BIO 466')
print('</a>')
print('<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">')
print('<span class="navbar-toggler-icon"></span>')
print('</button>')
print('')
print('<div class="collapse navbar-collapse" id="navbarSupportedContent">')
print('<ul class="navbar-nav ml-auto">')
print('<li class="nav-item ">')
print('<a class="nav-link" href="index.html">Home</a>')
print('</li>')
print('<li class="nav-item">')
print('<a class="nav-link active" href="about.html">About</a>')
print('</li>')
print('<li class="nav-item dropdown">')
print('<a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">')
print('Other pages <span class="sr-only">(current)</span></a>')
print('<div class="dropdown-menu dropdown-menu-right" aria-labelledby="navbarDropdown">')
print('<a class="dropdown-item" href="search.py">Search for a Gene or Transcript</a>')
print('<a class="dropdown-item" href="cat-count.py">Categories of Genes</a>')
print('<a class="dropdown-item" href="ano-transc-cnt.py"> Annotated Transcripts </a>')
print('<a class="dropdown-item" href="gene-cat-trans.py"> Transcripts by Gene Category </a>')
# print('<a class="dropdown-item" href="min-max.py" > Min/max of Transcripts per Gene </a>')
print('<!-- NOT YET - ->')
print('<!-- < a class = "dropdown-item" href = "gene-annotation.html" > Annotations < /a > -->')
print('<a class="dropdown-item" href="gt98.py"> Genes and Transcripts -- ENSMBL 98 Only </a>')
print('<a class="dropdown-item" href="gt82.py"> Genes and Transcripts -- ENSMBL 82 Only </a>')
print('</div>')
print('</li>')
print('</ul>')
print('</div>')
print('</nav><!-- end of navigation -->')
print('<!-- main container -->')
print('<div class="container">')
print('<div class="h-100 row align-items-center justify-content-center">')
print('<div class="col-lg-8 col-md-8 col-sm-12 pt-5">')
# print('<div class="row"><!-- header row -->')
# print('<h1>This is where the search results will end up</h1>')

# print('<p>The gene name is {0} and the transcript name is {1}'.format(gene_name, trans_name))

# print('</div><!-- end of the header row -->')

# Print out table for gene only if user entered a gene name
if gene_name is not None:
    print('<div class="row pt-5"><!-- Gene table row -->')
    print('<h1>Genes</h1>')
    print('<table class="table table-striped">')
    print('<thead class="bg-danger">')
    print('<tr>')
    print('<th scope="col">Gene Name</th>')
    print('<th scope="col">Start</th>')
    print('<th scope="col">End</th>')
    print('<th scope="col">Strand</th>')
    print('<th scope="col">Gene Category</th>')
    print('</tr>')
    print('</thead>')
    print('<tbody>')
    try:
        # Get all of the genes and transcripts
        with conn.cursor() as cursor:
            sql = 'SELECT DISTINCT STRAND, START_INDEX, END_INDEX, GENE_BIOTYPE FROM overbejt.geneII WHERE GENE_NAME=%s'
            cursor.execute(sql, gene_name)
            res = cursor.fetchone()

            # Print the data only if there is some to print
            if res is not None:
                print('<tr>')
                print('<td>{0}</td>'.format(gene_name))
                print('<td>{0}</td>'.format(res['START_INDEX']))
                print('<td>{0}</td>'.format(res['END_INDEX']))
                print('<td>{0}</td>'.format(res['STRAND']))
                print('<td>{0}</td>'.format(res['GENE_BIOTYPE']))
                print('</tr>')
            else:
                print('<tr>')
                print('<td>Gene {0} does not exist</td>'.format(gene_name))
                print('<td></td>')
                print('<td></td>')
                print('<td></td>')
                print('<td></td>')
                print('</tr>')

    finally:
        conn.close()
    print('</tbody>')
    print('</table>')
    print('</div>')

# Print out data for transcript only if the user entered a transcipt name
if trans_name is not None:
    print('<div class="row pt-5"><!-- Transcripts table row -->')
    print('<h1>Transcripts</h1>')
    print('<table class="table table-striped">')
    print('<thead class="bg-danger">')
    print('<tr>')
    print('<th scope="col">Transcript Name</th>')
    print('<th scope="col">Start</th>')
    print('<th scope="col">End</th>')
    print('<th scope="col">Exons Count</th>')
    print('<th scope="col">Introns Count</th>')
    print('</tr>')
    print('</thead>')
    print('<tbody>')
    try:
        with conn.cursor() as cursor:
            # Get the count of exons for the transcript
            sql = 'SELECT COUNT(*) AS exon_cnt FROM overbejt.geneII WHERE TRANSCRIPT_NAME=%s AND FEATURE="exon"'
            cursor.execute(sql, trans_name)
            exons = cursor.fetchone()

            # Get the count of introns for the transcript
            sql = 'SELECT COUNT(*) AS intron_cnt FROM overbejt.geneII WHERE TRANSCRIPT_NAME=%s AND FEATURE="intron"'
            cursor.execute(sql, trans_name)
            introns = cursor.fetchone()

            # Get all of the transcripts start and end positions
            sql = 'SELECT DISTINCT START_INDEX, END_INDEX FROM overbejt.geneII WHERE TRANSCRIPT_NAME=%s'
            cursor.execute(sql, trans_name)
            start_end = cursor.fetchall()

            # Make sure there is something to actually print out
            if len(start_end) > 0:
                # Print the first row
                print('<tr>')
                print('<td>{0}</td>'.format(trans_name))
                print('<td>{0}</td>'.format(start_end[0]['START_INDEX']))
                print('<td>{0}</td>'.format(start_end[0]['END_INDEX']))
                print('<td>{0}</td>'.format(exons['exon_cnt']))
                print('<td>{0}</td>'.format(introns['intron_cnt']))
                print('</tr>')

                # Loop and print the rest of the table
                count = 1
                for row in start_end:
                    if count > 2:
                        print('<tr>')
                        print('<td></td>')
                        print('<td>{0}</td>'.format(row['START_INDEX']))
                        print('<td>{0}</td>'.format(row['END_INDEX']))
                        print('<td></td>')
                        print('<td></td>')
                        print('</tr>')
                    count += 1
            else:
                print('<tr>')
                print('<td>Transcript {0} does not exist</td>'.format(trans_name))
                print('<td></td>')
                print('<td></td>')
                print('<td></td>')
                print('<td></td>')
                print('</tr>')

    finally:
        conn.close()
    print('</tbody>')
    print('</table>')
    print('</div><!-- end of the Transcripts table row -->')
print('</div><!-- end of container col -->')
print('</div><!-- end of container row -->')
print('</div><!-- end of the main container -->')
print('')
print('')
print('<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>')
print('<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>')
print('<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>')
print('')
print('</body>')
print('</html>')
