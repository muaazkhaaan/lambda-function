def lambda_handler(event, context):
    method = event.get("httpMethod")
    
    if method == "GET":
        return {
            'statusCode': 200,
            'body': 'hello world'
        }
    
    elif method == "POST":
        import json
        body = json.loads(event.get("body", "{}"))
        msg = body.get("message", "No message provided")
        return {
            'statusCode': 200,
            'body': f"Received: {msg}"
        }
    
    return {
        'statusCode': 405,
        'body': 'Method Not Allowed'
    }