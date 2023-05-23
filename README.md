# CLD - Workshop 2023

Damien Maier, Elliot Ganty, Mélissa Gehring, Thomas Germano

## Topic

[Amazon Rekognition](https://aws.amazon.com/rekognition/)

## Use cases

- [Face liveness](https://docs.aws.amazon.com/rekognition/latest/dg/face-liveness-requirements.html)
- [Labels](https://docs.aws.amazon.com/rekognition/latest/dg/labels.html?pg=ln&sec=ft)

## Scenario

**Face liveness**

_given_

Our face liveness backend and frontend servers are up and running

_when_

A user accesses the frontend

_then_

The backend receives a SessionID from AWS rekognition service and sends it to the client

_then_

The javascript FaceLivenessDetector component, that runs on the client, uses the client webcam and displays instructions to the user. During this process, it communicates with the Recognition Streaming Service that si running on AWS, using the SessionID.

_then_

The backend uses the SessionID to retrieve the result of the liveness detection from AWS. The result includes a liveliness score, and a picture appropriate to perform facial recognition.

---

**Detecting labels**

_given_

Our label detector service is up and running, and images are uploaded to the Amazon S3 bucket

_when_

Rekognition is called

_then_
  
The image is processed, and labels are annotated on the image and uploaded to the Amazon S3 bucket.
