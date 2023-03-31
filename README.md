# Scalable_serverless_App_with_Python_AWS_Lambda
Building a Scalable Serverless Application with Python and AWS Lambda

Lambda functions and API Gateway are two essential components of the AWS ecosystem that can work together to create powerful solutions for a wide range of business needs. One such use case is using a Lambda function which is triggered by an API Gateway which then creates an Amazon Simple Queue Service (SQS) queue.

Consider the following scenario:

Suppose your company is running a high-traffic e-commerce website that receives a large number of orders each day. To process these orders efficiently, the company can set up an API Gateway to receive incoming order requests from the website’s front-end. The API Gateway can then trigger a Lambda function, which can use the information from the order requests to create a new SQS queue.

The SQS queue can act as a buffer between the website’s front-end and the back-end processing system, allowing the company to process orders in batches and avoid overwhelming the back-end system. The Lambda function can also be configured to send notifications to relevant stakeholders when a new queue is created or when new orders are added to the queue.

In this article, I am going to show you how you can create this architecture using an API Gateway trigger, a Lambda function coded in Python which creates an SQS queue message.

Let’s jump right in!

Prerequisites

* 		Familiarity with AWS services, including Lambda, API Gateway, and SQS
* 		Proficiency in programming languages supported by Lambda functions, such as JavaScript, Python, and Java
* 		Knowledge of RESTful API design principles and how to create an API using API Gateway
* 		Understanding of serverless architecture and how to optimize serverless applications for performance and cost-effectiveness
* 		Experience in developing scalable and fault-tolerant systems, including designing queue-based architectures like the one described above.

Step 1: Creating our Lambda Function

We start in the Lambda dashboard, by clicking “Create function”.

We are going to ‘author from scratch’, give our function a name, select our run-time as ‘Python 3.7’, leave the architecture as default as well as the Lambda default permissions, which we are going to configure for our use-case in the next step. Finally, we click “Create function’.
