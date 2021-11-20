'''
NAME:DURGESH TIWARI
ENROLL NO.:20SOECE11071
CLASS:3CEB
'''
#OS module:functions for interacting with the operating system.
#Shutil module: many functions of high-level operations on files and collections of files.
import os
import shutil
#These are file extensions and folders
extensions = {'.mp3': 'Audio','.wav': 'Audio','.wpl': 'Audio','.wma': 'Audio',#Audio files
    '.zip': 'Compressed',#Compressed extensions
    '.gif': 'Images','.jpg': 'Images','.jpeg': 'Images','.png': 'Images','.webp':'Images','.tiff':'Images',#Images
    '.ppt': 'Presentations','.pptx': 'Presentations', #Presentation files
    '.c': 'Programming files','.cpp': 'Programming files','.py': 'Programming files',#Programming files
    '.m4v': 'Videos','.mkv': 'Videos','.mov': 'Videos','.mp4': 'Videos','.wmv': 'Videos',#Video files
    '.doc': 'Documents','.docx': 'Documents','.pdf': 'Documents','.txt': 'Documents','.wpd': 'Documents'#Documents
    }
def create_folder(folderDir):#create folder for different extensions
    for extension in extensions.values():
        if extension not in os.listdir(folderDir):#now if codition check whether specified folder for extension present or not.
            os.makedirs(os.path.join(folderDir,extension))#If not present then it will make a folder for that.
    moveFiles(folderDir)  #now move files to specified folder
def moveFiles(folderDir):
    for file in os.listdir(folderDir):
        if os.path.isfile(os.path.join(folderDir,file)):
            for extension in extensions.keys():
                if file.endswith(extension): #if condition check extension and move to specified folder
                    shutil.move(os.path.join(folderDir,file),os.path.join(folderDir,extensions[extension]))
                    break
    deleteEmpty(folderDir)#now it delete that folder which is empty
def deleteEmpty(folderDir):
    for folder in os.listdir(folderDir):
        try:
            if os.path.isdir(os.path.join(folderDir,folder)):
                os.rmdir(os.path.join(folderDir,folder))
        except OSError:
            continue
path_1=input("enter the path:")#now input from user to organize the specific path
create_folder(path_1)