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

<img width="1233" alt="Screenshot 2023-03-31 at 09 27 37" src="https://user-images.githubusercontent.com/67044030/229107332-3bc2a60a-a0c2-4448-9749-58b9358d2433.png">

<img width="1251" alt="Screenshot 2023-03-31 at 09 28 18" src="https://user-images.githubusercontent.com/67044030/229108076-c61f6a7f-adbc-4d4a-bb6a-e3e817931f6f.png">

Step 2: Assigning Permissions to our Lambda

Now that we’ve created our function, we need to ensure that he will have the permissions needed to create and SQS queue when the Lambda is triggered. To do this, we can click the ‘configuration’ sub-menu link.

<img width="1211" alt="Screenshot 2023-03-31 at 09 29 20" src="https://user-images.githubusercontent.com/67044030/229108463-3d562c0f-de3d-4168-92e1-98c3ec6f1f14.png">

Next we make our way to the “Permissions” left side menu and click on our “Execution role” link. This will open a new tab in our browser and bring us to our IAM dashboard where we can re-configure the IAM role for our Lambda function.

<img width="1229" alt="Screenshot 2023-03-31 at 09 31 30" src="https://user-images.githubusercontent.com/67044030/229109565-1370177d-a46a-40df-a97e-6f495e7fb2bb.png">

In the particular role for Lambda within the IAM dashboard, we click the ‘Add permissoins’ drop-down menu and click ‘Attach policies’.

<img width="1191" alt="Screenshot 2023-03-31 at 09 31 40" src="https://user-images.githubusercontent.com/67044030/229110179-9ceef0ce-1685-4a50-a79c-56ade3001a2c.png">

We can then search for ‘SQS’ and for our purposes are going to select the ‘AWSSQSFullAccess’ and click “Add permissions’.


We will then be re-directed back to our IAM dashboard where we receive confirmation that our policy was attached correctly. We can now move back to our Lambda function dashboard to code our python script.

<img width="879" alt="Screenshot 2023-03-31 at 09 34 09" src="https://user-images.githubusercontent.com/67044030/229112006-63159b08-d9d8-4d7f-ab90-b1a44e265397.png">

<img width="1256" alt="Screenshot 2023-03-31 at 09 33 58" src="https://user-images.githubusercontent.com/67044030/229110639-6942851c-0bcf-4403-80f8-6c0fc6800f42.png">

Step 3: Coding our Python Script in Lambda

Now that our Lambda has the proper permissions to send a message to our SQS queue. We can code our python script into our code of our lambda with inline comments.
I will briefly describe what our script does, but it should be evident from our introduction. Based on our scope and use-case, our script:

* 		Creates an instance of the SQS client
* 		Names the queue
* 		Creates the queue using the SQS client
* 		Returns a success message




