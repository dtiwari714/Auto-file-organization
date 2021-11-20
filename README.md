# Auto-file-organization
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





Auto file organization:
So,our project is about auto file organization. its simply managing a different type of files in well manner. Now we take an example we have a sample folder which have different types of files like,jpg, pdf, mp3, mp4 which is look like inappropriate. If we want to arrange manually than it takes much time to arrange in proper manner.
So, python is the key to solve this problem. Python is arranging all the files in category wise by using some module.
So here is the code for auto file organization.
 We can import OS module which interact with our operating system and we import shutil module it gives some function which deal with files and collection of files.
Now, we make dictionary which can store key and values pair. where we can write files extension in keys and                                                                         folder name in values where extension can be store. We named dictionary as extension.
Now we have to define a function create folder which is store the extension.Now we have taken for loop and inside loop we take an if statement to check whether previously folder for extension present or not. If not then we need to make a directory for folder.
Then we define second function for move the extension in the folder named as move files. Now it can check keys which is extension and move to the folder. Here if condition check where files are end with which extension and then move to folder.
Then we define the third function deleteempty.it simply deletes the empty folder.In the create folder function is create all the folder which is in values.so it delete the extra empty folder which dont have any files.                                  
Now we can call the create_folder function and we give the path where we need to arrange the file.
Now we run the code
Code is ask for the path so we need to give the any path where we want to arrange file so here we take sample folder path where we want to arrange.so we can copy the path of the sample folder and paste it and press enter.
Now we see that all the file are arranged in proper form.
