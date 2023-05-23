# Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

import os
import boto3

IMAGES_PATH = 'images/'
IMAGE_NAME = 'img{}.png'
BUCKET_NAME = 'aws.rekognition.cld.education.1'

def upload_photo(path, bucket, photo):
    client = boto3.client('s3')  # TODO check params
    client.upload_file(path, bucket, photo)

def main():
    # Find the number of images in the folder
    num_images = len([name for name in os.listdir(IMAGES_PATH) if os.path.isfile(os.path.join(IMAGES_PATH, name))])

    # Upload images to S3
    for i in range(num_images):
        upload_photo(IMAGES_PATH + IMAGE_NAME.format(i), BUCKET_NAME, IMAGE_NAME.format(i))

    print("{} images uploaded to S3".format(num_images))
    

if __name__ == "__main__":
    main()
