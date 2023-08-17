import os
 
# Function to rename multiple files
def main():

    folder = r'C:\Users\HP\Desktop\ranger\labels\train'
    for count, filename in enumerate(os.listdir(folder)):
        dst = f"{str(f'ranger_{count}')}.txt"
        src =f"{folder}/{filename}"  # foldername/filename, if .py file is outside folder
        dst =f"{folder}/{dst}"
         
        # rename() function will
        # rename all the files
        os.rename(src, dst)
 
# Driver Code
if __name__ == '__main__':
     
    # Calling main() function
    main()