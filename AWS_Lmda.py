import json
import boto3
import requests

def lambda_handler(event, context):
    # Preprocess the input
    user_input = event.get("body", "")
    tokenized_input = preprocess(user_input)

    # Send the preprocessed input to the LLM inference service (K8s or EC2)
    llm_service_url = "http://llm-service-url:8080/inference"  # Your LLM inference service URL
    
    response = requests.post(llm_service_url, json={"input": tokenized_input})

    # Return the response back to API Gateway
    return {
        'statusCode': 200,
        'body': json.dumps({
            'response': response.json().get("output")
        })
    }

def preprocess(input_text):
    # Tokenization or other preprocessing logic here
    return input_text
