import os
from collections import Counter

def DirectoryScanner(DirectoryName):
    Ret = False
    Ret = os.path.exists(DirectoryName)
    
    if(Ret == False):
        print("There is no such directory")
        return
    
    Ret = os.path.isdir(DirectoryName)
    if(Ret == False):
        print("It is not directory")
        return
    
    tot_subfolder = 0
    tot_subfolderName = []
    tot_file = 0
    ext_count = Counter()
    
    for FolderName,SubFolderName,FileName in os.walk(DirectoryName):
        
        if FolderName == DirectoryName:
            tot_subfolderName = SubFolderName
         
        tot_subfolder += len(SubFolderName)
        tot_file += len(FileName)
        
        for fname in FileName:
            ext = os.path.splitext(fname)[1].lower()
            if ext == "":
                ext = "(no ext)"
            ext_count[ext] += 1
            
    with open("demo.log","a",encoding="utf-8") as fobj:
        fobj.write("==============================\n")
        fobj.write("📂 Directory Scanner Summary\n")
        fobj.write("==============================\n\n")
        fobj.write("Path : "+ DirectoryName +"\n")
        
        fobj.write("Top-level folders : "+str(tot_subfolder)+"\n")
        fobj.write("Files Found : "+ str(tot_file) +"\n \n")
        
        fobj.write("📌 Total folders (recursive) : \n")
        
        for folder in tot_subfolderName:
            fobj.write(f" - {folder}\n")
        fobj.write("📌 Extension counts:\n")
        
        for ext, cnt in ext_count.most_common():
            fobj.write(f" {ext:8} : {cnt}\n")
        print("Scan completed. Check demo.log")

def main():
    directory_name = input("Enter the name of directory: ")
    DirectoryScanner(directory_name)

if __name__ == '__main__':
    main()
    