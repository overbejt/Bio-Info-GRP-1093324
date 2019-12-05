import sys

file82 = 'Mus_musculus.GRCm38.82.chr.gtf'
file98 = 'Mus_musculus.GRCm38.98.chr.gtf'

attributes = set()  # redundant
attrib_val = set()  # redundant

def getAttribute(key, attributes):
    """
    This is a method that will get the desired attribute value.

    :param key: The key for the desired attribute
    :param attributes: A list of all the attributes
    :return: The desired value for the indicated attribute
    """
    index = 0
    for i in attributes:
        if i == key:
            index += 1
            break
        index += 1
    # Try to clean it up
    try:
        if ';' in attributes[index]:
            attributes[index] = attributes[index].replace(';', '')
        if '\"' in attributes[index]:
            attributes[index] = attributes[index].replace('\"', '')
    except:
        print(key, attributes)
        # Do nothing
        pass
    finally:
        return attributes[index]

def main():
    file = open(sys.argv[1], 'r')
    outfile = open('dbData.txt', 'a')
    output = ''

    for line in file:
        # Prevent memory leak
        output = ''
        # Specify which ENSMBL version is being used
        if sys.argv[1] == file82:
            output += '82\t'
        else:
            output += '98\t'

        # Parse line by line
        if line[0] is not '#':
            arr = line.split('\t')
            # 0: seqname -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
            arr[0] = arr[0].strip()
            output += arr[0] + '\t'
            # 1: source -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
            arr[1] = arr[1].strip()
            output += arr[1] + '\t'
            # 3: feature -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
            arr[2] = arr[2].strip()
            output += arr[2] + '\t'
            # 4: start -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
            arr[3] = arr[3].strip()
            output += arr[3] + '\t'
            # 5: end -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
            arr[4] = arr[4].strip()
            output += arr[4] + '\t'
            # 6: score -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
            arr[5] = arr[5].strip()
            # Make sure it is not null
            if arr[5] == '.':
                output += 'null\t'
            else:
                output += arr[5] + '\t'
            # 7: strand -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
            arr[6] = arr[6].strip()
            output += arr[6] + '\t'
            # 8: frame -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
            arr[7] = arr[7].strip()
            # Make sure it is not null
            if arr[7] == '.':
                output += 'null\t'
            else:
                output += arr[7] + '\t'
            # 9: attributes -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-x
            # Make arr[8] easier to loop through
            arr[8] = arr[8].strip()
            attrib = arr[8].split(' ')
            # 10: transcript_version -=-=-=-=-=-=-=-=-=-=-=-=-
            focus = 'transcript_version'
            if focus in attrib:
                output += getAttribute(focus, attrib)
            else:
                output += 'null'
            output += '\t'
            # 11: transcript_source -=-=-=-=-=-=-=-=-=-=-=-=-=-
            focus = 'transcript_source'
            if focus in attrib:
                output += getAttribute(focus, attrib)
            else:
                output += 'null'
            output += '\t'
            # 12: transcript_biotype -=-=-=-=-=-=-=-=-=-=-=-=-=
            focus = 'transcript_biotype'
            if focus in attrib:
                output += getAttribute(focus, attrib)
            else:
                output += 'null'
            output += '\t'
            # 13: transcript_support_level -=-=-=-=-=-=-=-=-=-=
            focus = 'transcript_support_level'
            if focus in attrib:
                output += getAttribute(focus, attrib)
            else:
                output += 'null'
            output += '\t'
            # 14: gene_version -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
            focus = 'gene_version'
            if focus in attrib:
                output += getAttribute(focus, attrib)
            else:
                output += 'null'
            output += '\t'
            # 15: exon_id -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
            focus = 'exon_id'
            if focus in attrib:
                output += getAttribute(focus, attrib)
            else:
                output += 'null'
            output += '\t'
            # 16: ccds_id -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
            focus = 'ccds_id'
            if focus in attrib:
                output += getAttribute(focus, attrib)
            else:
                output += 'null'
            output += '\t'
            # 17: transcript_name -=-=-=-=-=-=-=-=-=-=-=-=-=-=-
            focus = 'transcript_name'
            if focus in attrib:
                output += getAttribute(focus, attrib)
            else:
                output += 'null'
            output += '\t'
            # 18: exon_version -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
            focus = 'exon_version'
            if focus in attrib:
                output += getAttribute(focus, attrib)
            else:
                output += 'null'
            output += '\t'
            # 19: transcript_id -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
            focus = 'transcript_id'
            if focus in attrib:
                output += getAttribute(focus, attrib)
            else:
                output += 'null'
            output += '\t'
            # 20: gene_name -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
            focus = 'gene_name'
            if focus in attrib:
                output += getAttribute(focus, attrib)
            else:
                output += 'null'
            output += '\t'
            # 21: protein_id -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
            focus = 'protein_id'
            if focus in attrib:
                output += getAttribute(focus, attrib)
            else:
                output += 'null'
            output += '\t'
            # 22: protein_version -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
            focus = 'protein_version'
            if focus in attrib:
                output += getAttribute(focus, attrib)
            else:
                output += 'null'
            output += '\t'
            # 23: tag -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
            focus = 'tag'
            if focus in attrib:
                output += getAttribute(focus, attrib)
            else:
                output += 'null'
            output += '\t'
            # 24: gene_source -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
            focus = 'gene_source'
            if focus in attrib:
                output += getAttribute(focus, attrib)
            else:
                output += 'null'
            output += '\t'
            # 25: gene_biotype -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
            focus = 'gene_biotype'
            if focus in attrib:
                output += getAttribute(focus, attrib)
            else:
                output += 'null'
            output += '\t'
            # 26: gene_id -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
            focus = 'gene_id'
            if focus in attrib:
                output += getAttribute(focus, attrib)
            else:
                output += 'null'
            output += '\t'
            # 27: exon_number -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
            focus = 'exon_number'
            if focus in attrib:
                output += getAttribute(focus, attrib)
            else:
                output += 'null'
            # output += '\t'  # Do I need this?

            # Add a new line
            output += '\n'
            outfile.write(output)
    print(output)

    file.close()
    outfile.close()


if __name__ == '__main__':
    main()

#  END OF FILE
