# Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

import boto3
import botocore
import numpy as np
import cv2
import PIL

ANNOTATED_IMAGES_PATH = 'annotated_images/'
IMAGE_NAME = 'annotated_{}'
BUCKET_NAME = 'aws.rekognition.cld.education.1'

def transform_bounding(frame, box):
    imgWidth, imgHeight = frame
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
    color = (0, 255, 0)
    thickness = 2

    # Transform bounding boxes
    for label in labels:

        for instance in label['Instances']:

            left, top, right, bottom = transform_bounding(frame.shape[:-1], instance['BoundingBox'])
            conf = instance['Confidence']
            name = label['Name']

            cv2.rectangle(frame, (left, top), (right, bottom), color, thickness)

            cv2.putText(frame, name+":"+str(conf)[0:4], (left, top - 12), 0, 1e-3 * imgHeight, color, thickness//1)


    # Save image into annoteated images folder
    cv2.imwrite(ANNOTATED_IMAGES_PATH + IMAGE_NAME.format(photo), frame)

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

    if "ImageProperties" in str(response):
        print("Background:")
        print(response["ImageProperties"]["Background"])
        print()
        print("Foreground:")
        print(response["ImageProperties"]["Foreground"])
        print()
        print("Quality:")
        print(response["ImageProperties"]["Quality"])
        print()

    # Annotate image
    annotate_photo(bucket, photo, response['Labels'])

    return len(response['Labels'])

def main():
    photo = 'img0.png'
    label_count = detect_labels(photo, BUCKET_NAME)
    print("Labels detected: " + str(label_count))


if __name__ == "__main__":
    main()
