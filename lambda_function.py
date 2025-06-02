import json

def lambda_handler(event, context):
    # Determine HTTP method
    method = event.get("httpMethod") or event.get("requestContext", {}).get("http", {}).get("method", "GET")

    # Log only method and outcome
    print(f"Received {method} request")

    if method == "GET":
        print("GET request handled successfully")
        return {
            'statusCode': 200,
            'body': 'hello world\n'
        }

    elif method == "POST":
        try:
            body = json.loads(event.get("body", "{}"))
            msg = body.get("message", "No message provided")
            print("POST request handled successfully")
            return {
                'statusCode': 200,
                'body': f"Received: {msg}\n"
            }
        except Exception as e:
            print(f"POST request failed: {str(e)}")
            return {
                'statusCode': 400,
                'body': f"Error parsing POST body: {str(e)}\n"
            }

    print("Unsupported HTTP method received")
    return {
        'statusCode': 405,
        'body': 'Method Not Allowed\n'
    }
