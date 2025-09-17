---
id: 11a7ea6c2c
question: AWS suggestions
section: Module 1: Introduction
course: mlops-zoomcamp
sort_order: 340
---

Make sure when you stop an EC2 instance that it actually stops (there's a meme about it somewhere). There are green circles (running), orange (stopping), and red (stopped). Always refresh the page to make sure you see the red circle and status of stopped.

Even when an EC2 instance is stopped, there WILL be other charges that are incurred (e.g. if you uploaded data to the EC2 instance, this data has to be stored somewhere, usually an EBS volume and this storage incurs a cost).

You can set up billing alerts. (I've never done this, so no advice on how to do this).

(Question by: Akshit Miglani () and Answer by Anna Vasylytsya)

