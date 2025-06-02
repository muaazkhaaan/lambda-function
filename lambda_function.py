import json

def lambda_handler(event, context):
    # Log the incoming event for debugging
    print("=== Incoming Event ===")
    print(json.dumps(event, indent=2))  # This will appear in CloudWatch Logs

    # For Lambda Function URLs, method is inside 'requestContext'
    method = event.get("httpMethod") or event.get("requestContext", {}).get("http", {}).get("method", "GET")
    
    if method == "GET":
        return {
            'statusCode': 200,
            'body': 'hello world\n'
        }

    elif method == "POST":
        try:
            body = json.loads(event.get("body", "{}"))
            msg = body.get("message", "No message provided")
            return {
                'statusCode': 200,
                'body': f"Received: {msg}\n"
            }
        except Exception as e:
            return {
                'statusCode': 400,
                'body': f"Error parsing POST body: {str(e)}\n"
            }

    return {
        'statusCode': 405,
        'body': 'Method Not Allowed\n'
    }
