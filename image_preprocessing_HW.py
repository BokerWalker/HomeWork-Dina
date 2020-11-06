import os 
import shutil
from PIL import Image
import math
import matplotlib.pyplot as plt

# Create folders for test and train sets.
def mkplibs (direc_name):
    path = input("enter a valid path:")
    if (path == ''):
        path = 'C:/Users/Admin/Desktop' # Change username
    pat = os.path.join(path,direc_name)
    try:
        if (not os.path.exists(pat)):  # Avoid making another spare directory if already 
            os.mkdir(pat)              # exists.
            os.mkdir( os.path.join(pat,"test"))
            os.mkdir( os.path.join(pat,"train"))
        else:
            print("directory already created in this path")
    except OSError:
        print ("Creation of the directory %s failed" % path)
        


# Find all directories with the same name within a presepcified path  
        
        
def find_all(name,path):
    result = []
    for root, dirs, files in os.walk(path):
        if name in dirs:
            result.append(os.path.join(root, name))
    return result

# Delete all directories with the same name within a presepcified path 
    
def del_all (name,path):
    res =find_all(name,path)
    for direc in res:
        shutil.rmtree(direc) # remove all directories + sub-directories 
                             # within the path
    

# transfer images from origin folder to train/test folder   

def split_imgs(data_path,imgs_path):
    images = os.listdir(imgs_path)
    if (os.path.split(data_path)[-1] == "test"):
        for i in images:
            shutil.move(os.path.join(imgs_path,i),os.path.join(data_path,i))
    elif(os.path.split(data_path)[-1] == "train"):
        for i in images[ : math.floor(0.7 * len(images))]:
            shutil.move(os.path.join(imgs_path,i),os.path.join(data_path,i))

# show all pictures within a directory
            
def print_imgs(data_path):
    for i in os.listdir(data_path):
        try:
         image = Image.open(os.path.join(data_path,i))
         plt.imshow(image)
         plt.show()
        except:
            print()

# return images in train and test to original folder:
         # direc_path = parent directory of train + test
         # imgs_path = pictures complete dataset
         
def merge_test_train (imgs_path,direc_path):
    test = os.path.join(direc_path,'test')
    train = os.path.join(direc_path,'train')
    for i in os.listdir(test):
        shutil.move(os.path.join(test,i),os.path.join(imgs_path,i))
    for i in os.listdir(train):
        shutil.move(os.path.join(train,i),os.path.join(imgs_path,i))
    


def main():
    
    # main is an example of implementing the methods with the following parameters:
    # parent directory of train + test: C:/Users/Admin/deb1
    # pictures complete dataset: C:/Users/Admin/Pictures/test
    
    mkplibs("deb1")
    #print(find_all("deb1",'C:/Users/Admin'))
    split_imgs('C:/Users/Admin/deb1/train','C:/Users/Admin/Pictures/test')
    split_imgs('C:/Users/Admin/deb1/test','C:/Users/Admin/Pictures/test')
    print_imgs("C:/Users/Admin/deb1/train")
    print_imgs("C:/Users/Admin/deb1/test")
    #merge_test_train('C:/Users/Admin/Pictures/test','C:/Users/Admin/deb1')
    #del_all("deb1",'C:/Users/Admin')
    #print(find_all("deb1",'C:/Users/Admin'))
    

if __name__ == '__main__':
    main()