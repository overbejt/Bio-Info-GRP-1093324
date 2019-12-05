import sys


def main():
    filename = sys.argv[1]
    print('Converting {0} from html to python'.format(filename))
    ifile = open(filename, 'r')
    filename.strip('.html')
    filename += '.py'
    ofile = open(filename, 'w')

    for iline in ifile:
        oline = 'print('
        oline += iline
        oline += ')'
        ofile.write(oline)

    ifile.close()
    ofile.close()
    print('Finished...')


if __name__ == '__main__':
    main()

#  END OF FILE
