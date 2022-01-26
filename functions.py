import re
import os
import pandas as pd

def file_to_df(path, dir = "data\\fasta_file\\"):
    data_dict = {}

    with open(dir + path,"r") as obj:
        data = obj.read()

    datalist = re.findall("[>][^>]+", data)

    for item in datalist:
        a = re.findall("_([a-zA-Z0-9.]{3,})", item)[-1]
        gene_name = item.splitlines()[0]
        i = ''.join(item.splitlines()[1:])
        data_dict[a] = []
        data_dict[a].append(gene_name)  #####original format
        data_dict[a].append(i)
        filename = re.match("(\w+)(\.)",path)
        df = pd.DataFrame(data_dict)
        df['Name'] = ">" + filename.group(1)
        df = df.sort_index(axis = 1)
        df.iloc[1,0] = ""  #####original format
    return df


def get_fasta_file_data(dir = "data\\fasta_file"):
    filelist = os.listdir(dir)
    templist = []
    for file in filelist:
        templist.append(file_to_df(file,dir+"\\"))
    return templist


def combine_data_frame(dir = "data\\fasta_file"):
    templist = get_fasta_file_data(dir)
    result = templist[0]
    n = 0
    while n < len(templist)-1:
        n += 1
        result = pd.concat([templist[n],result],ignore_index=True) #combine data and sort column name
    return result


def write_data_to_excel(data, output = "output.xlsx", excel_path=None): #add the new combined data to original excel
    if excel_path != None:
        original_data = pd.read_excel(excel_path, index_col=False)
        original_data = pd.concat([original_data,data],ignore_index=True)
        original_data.to_excel(output,index = False) 
    else:
        data.to_excel(output,index = False) 

def runMain(dir, output = "output.xlsx", excel_path = None):
    write_data_to_excel(combine_data_frame(dir), output, excel_path)


if __name__ == "__main__":
    runMain("data\\fasta_file\\")