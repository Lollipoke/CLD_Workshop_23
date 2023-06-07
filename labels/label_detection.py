# Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

import boto3
import botocore
import numpy as np
import cv2
import PIL

ANNOTATED_IMAGES_PATH = 'annotated_images/'
IMAGE_NAME = 'img{}.png'
ANNOTATED_IMAGE_NAME = 'annotated_{}'
BUCKET_NAME = 'aws.rekognition.cld.education'

WRITTEN_LABELS = []

def transform_bounding(frame, box):
    imgHeight, imgWidth = frame
    left = int(imgWidth * box['Left'])
    top = int(imgHeight * box['Top'])
    right = left + int(imgWidth * box['Width'])
    bottom = top + int(imgHeight * box['Height'])
    return left, top, right, bottom

def annotate_photo(bucket, photo, labels):

    # Load image from s3 bucket
    bucket = boto3.resource('s3').Bucket(bucket)
    img = bucket.Object(photo).get().get('Body').read()
    frame = cv2.imdecode(np.asarray(bytearray(img)), cv2.IMREAD_COLOR)

    # get image size
    imgHeight, imgWidth, _ = frame.shape

    # Set bounding box color and thickness
    color = (0, 255, 80)
    thickness = 2

    # Transform bounding boxes
    WRITTEN_LABELS.clear()
    for label in labels:
        name = label['Name']
        for instance in label['Instances']:

            left, top, right, bottom = transform_bounding(frame.shape[:-1], instance['BoundingBox'])
            conf = instance['Confidence']

            cv2.rectangle(frame, (left, top), (right, bottom), color, thickness)

            # Check if label is within image, otherwise move label inside image
            if top - 12 < 0:
                top = 25

            if left - 12 < 0:
                left = 5

            # Check if label is overlapping with other labels, otherwise move label down
            for label in WRITTEN_LABELS:
                if top - 12 <= label[1] and top + 12 >= label[1] and left - 12 <= label[0] + 100 and left + 100 >= label[0]:
                    top = top + 40

            cv2.putText(frame, name+":"+str(conf)[0:4]+"%", (left, top - 12), 0, 1e-3 * imgHeight, color, thickness//1)
            # Add the location of the label to the list of written labels
            WRITTEN_LABELS.append((left, top - 12))


    # Save image into annoteated images folder
    cv2.imwrite(ANNOTATED_IMAGES_PATH + ANNOTATED_IMAGE_NAME.format(photo), frame)

def detect_labels(photo, bucket):
    client = boto3.client('rekognition')
    response = client.detect_labels(Image={'S3Object': {'Bucket': bucket, 'Name': photo}},
                                    MaxLabels=3,
                                    # Uncomment to use image properties and filtration settings
                                    #Features=["GENERAL_LABELS", "IMAGE_PROPERTIES"],
                                    # Settings={"GeneralLabels": {"LabelInclusionFilters":["Cat"]},
                                    # "ImageProperties": {"MaxDominantColors":10}}
                                    )
    
    print('Detected labels for ' + photo)
    print()
    for label in response['Labels']:
        print("Label: " + label['Name'])
        print("Confidence: " + str(label['Confidence']))
        print("Instances:")

        for instance in label['Instances']:
            print(" Bounding box")
            print(" Top: " + str(instance['BoundingBox']['Top']))
            print(" Left: " + str(instance['BoundingBox']['Left']))
            print(" Width: " + str(instance['BoundingBox']['Width']))
            print(" Height: " + str(instance['BoundingBox']['Height']))
            print(" Confidence: " + str(instance['Confidence']))
            print()

        print("Parents:")
        for parent in label['Parents']:
            print(" " + parent['Name'])

        print("Aliases:")
        for alias in label['Aliases']:
            print(" " + alias['Name'])

            print("Categories:")
        for category in label['Categories']:
            print(" " + category['Name'])
            print("----------")
            print()

    # Annotate image
    annotate_photo(bucket, photo, response['Labels'])

    return len(response['Labels'])

def get_num_images(bucket):
    client = boto3.client('s3')
    result = client.list_objects(Bucket=bucket)
    return result['Contents'].__len__()

def main():
    # Find the number of images in the bucket
    num_images = get_num_images(BUCKET_NAME)

    # Detect labels in images
    for i in range(num_images):
        photo = IMAGE_NAME.format(i)
        label_count = detect_labels(photo, BUCKET_NAME)
        print("Labels detected for {}: {}".format(photo, label_count))

if __name__ == "__main__":
    main()
