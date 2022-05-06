import boto3
from datetime import date
import random
import string

#Creating S3 Boto3 session using assumed credentials from environment
s3 = boto3.client('s3')

def generate_big_random_letters(size):
    """
    generate big random letters/alphabets to a file
    :param filename: the filename
    :param size: the size in bytes
    :return: void
    """
    #Generate Random Prefix
    randomprefix = ''.join([random.choice(string.ascii_letters) for i in range(10)])
    
    for x in range (10):
        #Generate Random File Name and Date
        randomfilename = ''.join([random.choice(string.ascii_letters) for i in range(10)])
        filedate = str(date.today())
        filename = filedate + "_random_file_" + randomfilename
        
        #Generate File Data
        chars = ''.join([random.choice(string.ascii_letters) for i in range(size)]) #1
        objectpath = "filegenerator2/" + filedate + "_" + randomprefix + "/" + filename + ".txt"
        print(objectpath)
                
        #Upload object to S3
        object = s3.put_object(
            Bucket='BUCKETNAME',
            Body=chars,
            Key=objectpath,
            StorageClass='INTELLIGENT_TIERING'
        )
    else:
        print("Done")
    
def lambda_handler(event, context):
    print(event)
    print(context)
    generate_big_random_letters(1024*1024)
    return {
        'message' : "done"
    }