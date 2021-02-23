import os 
import sys
from dropbox.files import WriteMode

class DP:

    access_token, local_directory, dropbox_destination = sys.argv[1:4]


    def __init__(self, access_token):
        self.access_token=access_token
    

    def upload_file(self, file_from, file_to):
        client = WriteMode(access_token)

        for root, dirs, files in os.walk(local_directory): 
            for filename in files:
                local_path = os.path.join(root, filename)
                relative_path = os.path.relpath(local_path, local_directory)
                dropbox_path = os.path.join(dropbox_destination, relative_path)

                with open(local_path, 'rb') as f: 
                    client.put_file(dropbox_path, f) 

def main():
    access_token = 'E-x9-dSNM-0AAAAAAAAAAa8YDt0gjJEAla-4LblpgHoEsEWi8PxVmI4G8vIcEfju'
    tranferData = DP(access_token)

    file_from = input("Enter folder path... ")
    file_to = input("Enter destination path... ")

    tranferData.upload_file(file_from, file_to)

if __name__  == '__main__':
    main()