#!/usr/bin/env python3
import pymysql.cursors
import pymysql
import cgi
import cgitb
cgitb.enable()

# Connect to the database
conn = pymysql.connect(host='localhost',
                       user='overbejt',
                       password='bio466',
                       cursorclass=pymysql.cursors.DictCursor)

# Print some html
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
print('<div class="dropdown-menu" aria-labelledby="navbarDropdown">')
print('<a class="dropdown-item" href="gene-annotation.html">Annotations</a>')
print('</div>')
print('</li>')
print('</ul>')
print('</div>')
print('</nav><!-- end of navigation -->')
print('<!-- main container -->')
print('<div class="container">')
print('<div class="h-100 row align-items-center justify-content-center">')
print('<div class="col-lg-8 col-md-8 col-sm-12 pt-5">')
print('<div class="row ml-auto mr-auto">')
print('<h1>Search for a Gene or Transcript</h1>')
print('</div>')
print('<div class="pt-4">')
print('<table class="table table-striped">')
print('<thead class="bg-danger">')
print('<tr>')
print('<th scope="col">Category</th>')
print('<th scope="col">Count</th>')
print('</tr>')
print('</thead>')

try:
    # Get all of the gene categories and their count
    with conn.cursor() as cursor:
        # Get the total count of genes
        sql = 'SELECT COUNT(DISTINCT GENE_ID) AS count FROM geneII WHERE FEATURE=\'gene\''
        cursor.execute(sql)
        res = cursor.fetchone()
        gene_total = res['count']

        # Ge the total count of transcripts
        sql = 'SELECT COUNT(DISTINCT TRANSCRIPT_ID) AS count FROM geneII WHERE FEATURE=\'transcript\''
        cursor.execute(sql)
        res = cursor.fetchone()
        gene_total = res['count']

        # Get the total count of genes in 98
        sql = 'SELECT COUNT(DISTINCT GENE_ID) AS count FROM geneII WHERE FEATURE=\'gene\' AND ENSMBLE_VERSION = 98'
        cursor.execute(sql)
        res = cursor.fetchone()
        genes_98 = res['count']

        # Get the total count of genes in 82
        sql = 'SELECT COUNT(DISTINCT GENE_ID) AS count FROM geneII WHERE FEATURE=\'gene\' AND ENSMBLE_VERSION = 82'
        cursor.execute(sql)
        res = cursor.fetchone()
        genes_82 = res['count']

        # Get the total count of transcripts in 98
        sql = 'SELECT COUNT(DISTINCT TRANSCRIPT_ID) AS count FROM geneII WHERE FEATURE=\'transcript\' AND ENSMBLE_VERSION = 98'
        cursor.execute(sql)
        res = cursor.fetchone()
        genes_98 = res['count']

        # Get the total count of transcripts in 82
        sql = 'SELECT COUNT(DISTINCT TRANSCRIPT_ID) AS count FROM geneII WHERE FEATURE=\'transcript\' AND ENSMBLE_VERSION = 82'
        cursor.execute(sql)
        res = cursor.fetchone()
        genes_82 = res['count']

    print('<tbody>')
    print('<tr>')
    print('<td>Genes Total</td>')
    print('<td>{0}</td>'.format(gene_total))
    print('</tr>')
    print('<tr>')
    print('<td>Transcripts Total</td>')
    print('<td>{0}</td>'.format(transcript_total))
    print('</tr>')
    print('<tr>')
    print('<td>Genes in 98</td>')
    print('<td>{0}</td>'.format(genes_98))
    print('</tr>')
    print('<tr>')
    print('<td>Genes in 82</td>')
    print('<td>{0}</td>'.format(genes_82))
    print('</tr>')
    print('<tr>')
    print('<td>Transcripts in 98</td>')
    print('<td>{0}</td>'.format(trans_98))
    print('</tr>')
    print('<tr>')
    print('<td>Transcripts in 82</td>')
    print('<td>{0}</td>'.format(trans_82))
    print('</tr>')

finally:
    conn.close()

print('</tbody>')
print('</table>')
print('</div>')
print('<div class="row pt-5 pb-5"><!-- search row -->')
print('<div class="col-lg-6 col-md-6 col-sm-12"> <!-- Gene form -->')
print('<form>')
print('<div class="form-group">')
print('<label for="gene_form">Search for a Gene</label>')
print('<input type="email" class="form-control" id="gene_form" placeholder="Enter a gene name">')
print('</div>')
print('<button type="submit" class="btn btn-primary">Submit</button>')
print('</form>')
print('</div><!-- end of Gene form -->')
print('<div class="col-lg-6 col-md-6 col-sm-12"> <!-- Transcript form -->')
print('<form>')
print('<div class="form-group">')
print('<label for="transcript_form">Search for a Transcript</label>')
print('<input type="email" class="form-control" id="transcript_form" placeholder="Enter a transcript name">')
print('</div>')
print('<button type="submit" class="btn btn-primary">Submit</button>')
print('</form>')
print('</div><!-- end of Transcript form -->')
print('</div><!-- end of search row -->')
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
