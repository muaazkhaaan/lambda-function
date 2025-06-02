import json

def lambda_handler(event, context):
    print("=== Incoming Event ===")

    method = event.get("httpMethod") or event.get("requestContext", {}).get("http", {}).get("method", "GET")
    
    if method == "GET":
        print("GET METHODS USED!")
        return {'statusCode': 200, 'body': 'hello world'}

    elif method == "POST":
        try:
            body = json.loads(event.get("body", "{}"))
            msg = body.get("message", "No message provided")
            print("GET POST METHOD USED!")
            return {'statusCode': 200, 'body': f"Received: {msg}"}
        except Exception as e:
            return {'statusCode': 400, 'body': f"Error: {str(e)}'}

    return {'statusCode': 405, 'body': 'Method Not Allowed'}
