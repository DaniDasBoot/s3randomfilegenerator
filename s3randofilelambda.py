import os
import boto3
from datetime import date
import random
import string

#Set variables to Lambda environment variables
S3ObjectsToCreate = int(os.environ['S3ObjectsToCreate'])
S3Bucket = os.environ['S3Bucket']
S3StorageClass = os.environ['S3StorageClass']
S3ObjectSize = int(os.environ['S3ObjectSize'])

#Creating S3 Boto3 session using assumed credentials from environment
s3 = boto3.client('s3')

def generate_big_random_letters():
    """
    generate big random letters/alphabets to a file
    :param filename: the filename
    :param size: the size in bytes
    :return: void
    """
    #Generate Random Prefix
    randomprefix = ''.join([random.choice(string.ascii_letters) for i in range(10)])
    
    #Run loop for how many objects should be created. Object count defined in environment variable
    for x in range (S3ObjectsToCreate):
        #Generate Random File Name and Date
        randomfilename = ''.join([random.choice(string.ascii_letters) for i in range(10)])
        filedate = str(date.today())
        filename = filedate + "_random_file_" + randomfilename
        
        #Generate File Data, object size is defined in environment variable
        chars = ''.join([random.choice(string.ascii_letters) for i in range(S3ObjectSize)]) #1
        objectpath = "filegenerator2/" + filedate + "_" + randomprefix + "/" + filename + ".txt"
        print("Writing S3 object" + objectpath)
                
        #Upload object to S3, bucket and storage class defined in environment variables
        object = s3.put_object(
            Bucket = S3Bucket,
            Body = chars,
            Key = objectpath,
            StorageClass = S3StorageClass
        )
    else:
        print("Done")
    
def lambda_handler(event, context):
    print(event)
    print("Printing Lambda Environment Variables:")
    print("S3 Bucket: " + os.environ['S3Bucket'])
    print("S3 Storage Class: " + os.environ['S3StorageClass'])
    print("S3 Object Count: " + os.environ['S3ObjectsToCreate'])
    print("S3 Object Size (bytes): " + os.environ['S3ObjectSize'])

    generate_big_random_letters()
    return {
        'message' : "Done"
    }