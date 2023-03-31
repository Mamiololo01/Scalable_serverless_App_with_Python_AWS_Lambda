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

<img width="1232" alt="Screenshot 2023-03-31 at 09 38 47" src="https://user-images.githubusercontent.com/67044030/229112262-ce987907-0391-4031-a314-229c35296139.png">

We paste our code into our Lambda function code and click the ‘Deploy’ button and should receive a green confirmation banner that our function was updated.

<img width="1111" alt="Screenshot 2023-03-31 at 09 43 37" src="https://user-images.githubusercontent.com/67044030/229112798-508c2c72-50ce-484d-a3ff-4758b40550b6.png">

Next we need to configure our test event. Remember, our Lambda needs to be triggered by an API gateway request. Therefore, we need to configure our test event to reflect that.

We set up our test event back in our Lambda function dashboard by clicking the orange “Test” button. If this is your first time testing this particular function, AWS should route you immediately to a test configuration page, if it doesn’t, it will test based on their default test event or a previously configured test, which may not execute properly.

If this is the case, you can click the ‘down arrow’ on the orangge ‘Test’ button to create a new ‘test event’.

Attached is the JSON-based trigger event for an API gateway action. Feel free to use it or configure your own test event

We give our test event a name, we will make ours private and paste in our JSON, then click “Save”.


Back in our function, we can test to see if our python script runs as expected by clicking the orange “Test” button and selecting our newly created test event, if needed.

Our script should return a response of ‘200’ and a brief message informing us that an SQS queue was created

<img width="1111" alt="Screenshot 2023-03-31 at 09 43 37" src="https://user-images.githubusercontent.com/67044030/229115565-eebe7801-4b06-4b7a-9483-d954c562f259.png">


We can also verify our test results by visiting the SQS dashboard to see our message and move onto configuring our API as a trigger for our Lambda.

<img width="1098" alt="Screenshot 2023-03-31 at 09 44 39" src="https://user-images.githubusercontent.com/67044030/229115400-81b37b8d-71b1-4f37-8582-73d1c4c43cbd.png">

Step 4: Configuring our REST API in AWS API Gateway

We start by heading to API Gateway in the AWS console. For our use-case we are going to create a REST API.

We’re going to give our API a name and click “Next”

<img width="1271" alt="Screenshot 2023-03-31 at 09 55 39" src="https://user-images.githubusercontent.com/67044030/229116738-27456a55-d928-4c03-9467-87627bd83613.png">


We are going to select REST for our protocol. We select new API, give our API a name, and click “Create API”

Next we need to create a Resource, give our resource a name, and click “Create Resource”

<img width="1227" alt="Screenshot 2023-03-31 at 09 57 30" src="https://user-images.githubusercontent.com/67044030/229117730-25d63295-2730-42a3-8634-5dd5fbfd3832.png">

<img width="1246" alt="Screenshot 2023-03-31 at 09 56 48" src="https://user-images.githubusercontent.com/67044030/229117269-088182f8-0d75-4bd3-9e6f-c4073b099e3f.png">

Select “POST” for our use-case and click the checkmark to confirm.


We are going to set our integreation type to “Lambda Function”, select Lambda proxy integration, select the same region that our Lambda function is in, select our particular Lambda function, and click “Save”.


<img width="1038" alt="Screenshot 2023-03-31 at 10 01 01" src="https://user-images.githubusercontent.com/67044030/229118252-bdd65fea-08b6-4bc8-a2be-551ec6d79220.png">


We are going to be prompted to enable permissions for our API to invoke our Lambda function.

<img width="1252" alt="Screenshot 2023-03-31 at 10 01 30" src="https://user-images.githubusercontent.com/67044030/229118635-1a8cc23e-765c-4e65-ac41-b4aec6e16193.png">


Finally, we need to deploy our API and select or assign a stage for our API. Finally, we click, “Deploy”.

<img width="1239" alt="Screenshot 2023-03-31 at 10 02 56" src="https://user-images.githubusercontent.com/67044030/229119110-fccb8b56-8010-4521-971c-d67e8eca4d39.png">

Now that our API is configured and deployed, we need to test that our API invokes our Lambda function so that it produces an SQS queue for our website ecommerce store. To do this, we navigate to “Stages” in our left-side menu and click on our “POST” method.

<img width="1255" alt="Screenshot 2023-03-31 at 10 04 05" src="https://user-images.githubusercontent.com/67044030/229119559-78d99839-4264-4d7b-95c5-814629a999bd.png">

<img width="1255" alt="Screenshot 2023-03-31 at 10 05 18" src="https://user-images.githubusercontent.com/67044030/229120147-d0688f70-f0b3-4102-84a6-be3e5b7e82b1.png">

In our POST method menu, we click “TEST”:

<img width="1253" alt="Screenshot 2023-03-31 at 10 07 32" src="https://user-images.githubusercontent.com/67044030/229120453-95b0a5a1-7058-4c56-8f09-f6dc0fb1ade9.png">

This will open a test menu. At the bottom, click “Test” and on the request side, should return a 200 Status code indicating a successful Lambda function run:

<img width="1223" alt="Screenshot 2023-03-31 at 10 09 43" src="https://user-images.githubusercontent.com/67044030/229120695-55b9f43a-0283-4104-b2a1-85242ae03a3f.png">

Finally, we head over to our SNS Dashboard one more time. Here we can verify that our serverless application successfully ran through our integration from our API trigger to our Python Function in Lambda into a created queue in SQS







