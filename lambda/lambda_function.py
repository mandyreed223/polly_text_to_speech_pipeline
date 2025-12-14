import os
import json
import time
import base64
import boto3

s3 = boto3.client("s3")
polly = boto3.client("polly")

BUCKET = os.environ["S3_BUCKET_NAME"]             
ENVIRONMENT = os.environ.get("ENVIRONMENT", "beta")   # beta or prod

def lambda_handler(event, context):
    try:
        # Get body from API Gateway event
        body = event.get("body", "{}")

        # If API Gateway sends base64-encoded body, decode it
        if event.get("isBase64Encoded"):
            body = base64.b64decode(body).decode("utf-8")

        # Convert JSON string -> dict
        if isinstance(body, str):
            body = json.loads(body)

        text = body.get("text", "").strip()
        if not text:
            return {
                "statusCode": 400,
                "headers": {"Content-Type": "application/json"},
                "body": json.dumps({"error": "Missing 'text' in request body"})
            }

        # Timestamped output path (matches your requirement)
        ts = int(time.time())
        key = f"polly-audio/{ENVIRONMENT}/{ts}.mp3"

        # Call Polly
        response = polly.synthesize_speech(
            Text=text,
            OutputFormat="mp3",
            VoiceId="Joanna"
        )

        audio_stream = response.get("AudioStream")
        if not audio_stream:
            raise Exception("Polly response missing AudioStream")

        audio_bytes = audio_stream.read()

        # Upload to S3
        s3.put_object(
            Bucket=BUCKET,
            Key=key,
            Body=audio_bytes,
            ContentType="audio/mpeg"
        )

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({
                "message": "Audio created",
                "environment": ENVIRONMENT,
                "s3_uri": f"s3://{BUCKET}/{key}"
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({
                "error": str(e),
                "environment": ENVIRONMENT
            })
        }
