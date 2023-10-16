# Python program that receives a path of a MusicXML file as a command line argument,
# and it splits the score based on the <words> tag with text in format PT:X where X is the elapsed time in seconds.
# The program should keep tempo, staff, and clef information on each cut.
# The program should create a new MusicXML file for each cut.
# The name of the new file should be the same as the original file with the addition of the cut number.
# For example, if the original file is named "song.xml", the new files should be named "song_1.xml", "song_2.xml", etc.

import sys
import xml.etree.ElementTree as ET
import os


def main():
    # get the path of the file
    path = sys.argv[1]
    # open the file with ET
    tree = ET.parse(path)
    root = tree.getroot()
    number_of_cut = -1
    # copy the original tree without the measures
    cut_tree = ET.ElementTree()
    cut_tree._setroot(root)
    cut_tree._root.clear()

    # find a measure containing the words tag with the time mark "PT:X", for example, "PT:56.196274"
    for measure in root.iter('measure'):
        # add the measure to the cut tree
        cut_tree._root.append(measure)
        # find the words tag
        for words in measure.iter('words'):
            # find the time mark in the text of the words tag
            if 'PT:' == words.text[0:3]:
                time_mark = words.text
                # get the time mark in seconds
                seconds = float(time_mark.split(':')[1].strip())
                # get the measure number
                measure_number = measure.attrib['number']
                # increase the number of cut
                number_of_cut += 1
                # get the name of the file
                file_name = os.path.basename(path)
                # get the name of the file without the extension
                file_name_without_extension = os.path.splitext(file_name)[0]
                # create a new name for the file
                new_file_name = file_name_without_extension + '_' + str(number_of_cut) + '.xml'
                # write the new file with the stored measures
                cut_tree.write(new_file_name)
                # create a new tree for the next cut
                cut_tree._setroot(root)
                cut_tree._root.clear()


if __name__ == '__main__':
    main()
