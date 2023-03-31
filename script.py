import boto3

def lambda_handler(event, context):
    sqs = boto3.resource('sqs')
    queue_name = 'my-sqs-queue'
    queue = sqs.create_queue(QueueName=queue_name)
    return {
        'statusCode': 200,
        'body': f'Successfully created SQS queue {queue_name}'
    }
