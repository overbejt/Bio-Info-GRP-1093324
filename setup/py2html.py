import sys


def main():
    filename = sys.argv[1]
    print('Converting {0} from html to python'.format(filename))
    ifile = open(filename, 'r')
    filename = filename.replace('.html', '.py')
    ofile = open(filename, 'w')

    # Add in some basic stuff
    ofile.write('#!/usr/bin/env python3\nimport pymysql.cursors\nimport pymysql\n')
    ofile.write('import cgi\nimport cgitb\ncgitb.enable()\n\n')
    ofile.write('# Connect to the database\n')
    ofile.write('conn = pymysql.connect(host=\'localhost\', user=\'overbejt\', password=\'bio466\', cursorclass=pymysql.cursors.DictCursor)\n\n')

    for iline in ifile:
        oline = 'print(\''
        oline += iline.strip()
        oline += '\')\n'
        ofile.write(oline)

    ifile.close()
    ofile.close()
    print('Finished...')


if __name__ == '__main__':
    main()

#  END OF FILE
