import json
import logging  # For logging request and error details

# Set up basic logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    # Determine HTTP method from event
    method = event.get("httpMethod") or event.get("requestContext", {}).get("http", {}).get("method", "GET")
    logger.info(f"Request method: {method}")

    if method == "GET":
        # Respond to GET requests
        logger.info("Handled GET request successfully")
        return {
            'statusCode': 200,
            'body': 'hello world\n'
        }

    elif method == "POST":
        # Handle POST request with JSON body
        try:
            body = json.loads(event.get("body", "{}"))
            msg = body.get("message", "No message provided")
            logger.info(f"Handled POST request successfully with message: {msg}")
            return {
                'statusCode': 200,
                'body': f"Received: {msg}\n"
            }
        except Exception as e:
            # Log and return error if body parsing fails
            logger.error(f"Failed to parse POST body: {str(e)}")
            return {
                'statusCode': 400,
                'body': f"Error parsing POST body: {str(e)}\n"
            }

    # Catch-all for unsupported methods
    logger.warning("Unsupported HTTP method received")
    return {
        'statusCode': 405,
        'body': 'Method Not Allowed\n'
    }