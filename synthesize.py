import os
import boto3

def main():
    print("✅ synthesize.py started")

    # Read environment variables (set in GitHub Actions)
    bucket_name = os.environ.get("S3_BUCKET_NAME")
    output_key = os.environ.get("OUTPUT_KEY")

    print(f"Bucket: {bucket_name}")
    print(f"Key: {output_key}")

    if not bucket_name or not output_key:
        raise ValueError("Missing required env vars: S3_BUCKET_NAME and/or OUTPUT_KEY")

    # Read input text
    with open("speech.txt", "r", encoding="utf-8") as f:
        text = f.read().strip()

    print(f"Text length: {len(text)}")

    if not text:
        raise ValueError("speech.txt is empty. Add text before running.")

    polly = boto3.client("polly")
    s3 = boto3.client("s3")

    print("Calling Amazon Polly...")
    response = polly.synthesize_speech(
        Text=text,
        OutputFormat="mp3",
        VoiceId="Joanna"
    )

    # Save mp3 locally
    local_file = "output.mp3"
    audio_stream = response.get("AudioStream")
    if not audio_stream:
        raise ValueError("Polly response missing AudioStream")

    with open(local_file, "wb") as audio_file:
        audio_file.write(audio_stream.read())

    print("✅ output.mp3 created, uploading to S3...")

    # Upload to S3
    s3.upload_file(local_file, bucket_name, output_key)

    print(f"✅ Uploaded {local_file} to s3://{bucket_name}/{output_key}")

if __name__ == "__main__":
    main()
