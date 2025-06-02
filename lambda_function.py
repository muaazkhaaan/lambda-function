import json
import logging

# Setup logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    method = event.get("httpMethod") or event.get("requestContext", {}).get("http", {}).get("method", "GET")
    logger.info(f"Request method: {method}")

    if method == "GET":
        logger.info("Handled GET request successfully")
        return {
            'statusCode': 200,
            'body': 'hello world\n'
        }

    elif method == "POST":
        try:
            body = json.loads(event.get("body", "{}"))
            msg = body.get("message", "No message provided")
            logger.info(f"Handled POST request successfully with message: {msg}")
            return {
                'statusCode': 200,
                'body': f"Received: {msg}\n"
            }
        except Exception as e:
            logger.error(f"Failed to parse POST body: {str(e)}")
            return {
                'statusCode': 400,
                'body': f"Error parsing POST body: {str(e)}\n"
            }

    logger.warning("Unsupported HTTP method received")
    return {
        'statusCode': 405,
        'body': 'Method Not Allowed\n'
    }
