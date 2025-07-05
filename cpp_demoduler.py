import os

header_lines=[]
source_lines=[]
main_lines=[]

header_ext=".hpp"
header_ext=".cpp"

def process_file(file_name):
    if file_name.endswith(".hpp"):
        with open(file_name, 'r', encoding='utf-8', errors='ignore') as file:
            for line in file:
                header_lines.append(line)
        header_lines.append("\n")
    elif file_name.endswith(".cpp"):
        with open(file_name, 'r', encoding='utf-8', errors='ignore') as file:
            for line in file:
                if "main" in file_name:
                    main_lines.append(line)
                elif line.startswith("#include")==False:
                    source_lines.append(line)
            source_lines.append("\n")
            if "main" in file_name:
                print("Found main file! Placing that in front of other files.")
                main_lines.append("\n")

def get_source_header_data(root_dir):

    for root, _, files in os.walk(root_dir):
        for file in files:
            file_path = os.path.join(root, file)

            process_file(file_path)

def demodule_to_file(master_filename):
    with open(master_filename, 'a', encoding='utf-8', errors='ignore') as dstfile:
        for line in header_lines:
            if line.startswith("#include")==False or ".hpp" not in line:
                dstfile.write(line)
                
        for line in source_lines:
            dstfile.write(line)
            
        for line in main_lines:
            if line.startswith("#include")==False or ".hpp" not in line:
                dstfile.write(line)

if __name__ == "__main__":
    is_cpp=True
    
    file_extname="main_demoduled.cpp"
    if is_cpp==True:
        header_ext=".hpp"
        header_ext=".cpp"
    else:
        file_extname="main_demoduled.c"
        header_ext=".h"
        header_ext=".c"
      
        
    folder_path = input("Enter the folder path: ")
    master_file_path = os.path.join(folder_path, file_extname)

    print(f"Demoduling all .cpp and .hpp files...")
    get_source_header_data(folder_path)
    
    demodule_to_file(master_file_path)
    print("Demoduling done. (written in "+file_extname+")")
