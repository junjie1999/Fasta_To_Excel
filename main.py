import argparse
import os
import re
from functions import runMain

parser = argparse.ArgumentParser()
parser.add_argument("input_dir", help = "directory of input file (fasta and txt format only)")
parser.add_argument("-output", help = "name of output file (excel format)\ndefault name: output.xlsx")
parser.add_argument("-ori", help = "original excel to add-on dir data")
args = parser.parse_args()

if os.path.exists(args.input_dir) == False:  #check input file
    print("ERROR! input file does not exist")

if os.path.exists(args.input_dir) == True:
    if args.output != None:
        if re.match("[\w\s]+.xlsx", args.output) == None:
            print("output file ERROR! Must be EXCEL file")
        else:
            try:
                runMain(args.input_dir, args.output, args.ori)
                print("SUCCESS!")
            except:
                print("FAIL!")
    else:
        try:
            runMain(dir = args.input_dir, excel_path = args.ori)
            print("SUCCESS!")
        except:
            print("FAIL!")