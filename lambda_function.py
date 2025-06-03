import os
import json
import logging

# Set up logger with configurable level from environment (default to INFO)
LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO").upper()
logger = logging.getLogger()
logger.setLevel(getattr(logging, LOG_LEVEL, logging.INFO))

def lambda_handler(event, context):
    # Determine HTTP method
    method = event.get("httpMethod") or event.get("requestContext", {}).get("http", {}).get("method", "GET")
    logger.debug(f"Request method: {method}")

    if method == "GET":
        return handle_get()

    elif method == "POST":
        return handle_post(event)

    # Catch-all for unsupported methods
    logger.warning(f"Unsupported HTTP method received: {method}")
    return {
        'statusCode': 405,
        'body': 'Method Not Allowed\n'
    }

def handle_get():
    # Handles GET requests
    logger.info("GET request handled successfully")
    return {
        'statusCode': 200,
        'body': 'hello world\n'
    }

def handle_post(event):
    # Handle POST request with JSON body
    try:
        body = json.loads(event.get("body", "{}"))
        msg = body.get("message", "No message provided")
        logger.info("POST request handled successfully")
        logger.debug(f"POST message: {msg}")
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