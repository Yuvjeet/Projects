import shutil,os
dic_ex={
    'Video_extension':(".mp4",".webm"),
    'Text_extension':(".txt",".docx"),
    'Audio_extension':(".mp3"),
    'Image_extension':(".png",".jpg"),
    }
folderpath=input("folder path")
def file_finder(folder_path,file_ex):
    files=[]
    for file in os.listdir(folder_path):
        for ex in file_ex:
            if file.endswith(ex):
                files.append(file)
    return files
for ex_type,ex_tuple in dic_ex.items():
    folder_name=ex_type.split("_")[0]+'Files'
    folder_path=os.path.join(folderpath,folder_name)
    if os.path.exists(folder_path):
        for item in file_finder(folderpath,ex_tuple):
            item_path=os.path.join(folderpath,item)
            item_new=os.path.join(folder_path,item)
            shutil.move(item_path,item_new)
    else:
        for item in file_finder(folderpath,ex_tuple):
            if os.path.exists(folder_path):
                item_path=os.path.join(folderpath,item)
                item_new=os.path.join(folder_path,item)
                shutil.move(item_path,item_new)
            else:
                os.mkdir(folder_path)
                item_path=os.path.join(folderpath,item)
                item_new=os.path.join(folder_path,item)
                shutil.move(item_path,item_new)
        
