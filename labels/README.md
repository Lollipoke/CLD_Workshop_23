# CLD - Workshop 2023

Damien Maier, Elliot Ganty, Mélissa Gehring, Thomas Germano

## Topic

[Amazon Rekognition](https://aws.amazon.com/rekognition/)

## Use cases

- [Face analysis and detection](https://docs.aws.amazon.com/rekognition/latest/dg/collections.html?pg=ln&sec=ft)
- [Labels](https://docs.aws.amazon.com/rekognition/latest/dg/labels.html?pg=ln&sec=ft)

## Scenario

**Face analysis**

_given_

Our face analysis system is up and running

_when_

A picture is sent

_then_

The image is processed and 

---

**Detecting labels**

_given_

Our label detector service is up and running, and images are uploaded to the Amazon S3 bucket

_when_

Rekognition is called

_then_
  
The image is processed, and labels are annotated on the image and uploaded to the Amazon S3 bucket.
