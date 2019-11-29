#!/usr/bin/env python3
import cgi, cgitb
cgitb.enable()
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
print('Other pages')
print('</a>')
print('<div class="dropdown-menu" aria-labelledby="navbarDropdown">')
print('<a class="dropdown-item" href="gene-annotation.html">Annotations <span class="sr-only">(current)</span></a>')
print('</div>')
print('</li>')
print('</ul>')
print('</div>')
print('</nav><!-- end of navigation -->')
print('<!-- main container -->')
print('<div class="container">')
print('<div class="h-100 row align-items-center justify-content-center">')
print('<div class="col-auto pt-5">')
print('<form id="gs-form" action="scripts/find-gene.py"><!-- gene selection form -->')
print('<div class="form-row align-items-center">')
print('<div class="col-auto">')
print('<select class="custom-select mr-sm-2" id="gene-selection">')
print('<option selected>Choose...</option>')
print('<option value="1">One</option>')
print('<option value="2">Two</option>')
print('<option value="3">Three</option>')
print('</select>')
print('</div>')
print('<div class="col-auto">')
print('<button type="submit" class="btn btn-primary">Submit</button>')
print('</div>')
print('</div>')
print('</form>')
print('</div>')
print('</div>')
print('</div><!-- end of the main container -->')
print('')
print('')
print('<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>')
print('<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>')
print('<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>')
print('')
print('</body>')
print('</html>')
