import boto3
import os 

# Access environment variables
aws_access_key_id = os.environ['aws_access_key_id']
aws_secret_access_key = os.environ['aws_secret_access_key']
region_name=os.environ['region_name']

# Create a new Polly client using the IAM user's credentials
session = boto3.Session(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region_name
)

# Set up the AWS Polly client
polly = session.client('polly')


# Set the path to the input and output files
input_file = '/tmp/input.txt'
output_file = '/tmp/output.mp3'

# Read the input text from the file
with open(input_file, 'rb') as f:
    text = f.read()

# Use AWS Polly to synthesize the text into audio
response = polly.synthesize_speech(
    Text=text,
    OutputFormat='mp3',
    VoiceId='Joanna'
)

# Save the audio to a file
with open(output_file, 'wb') as f:
    f.write(response['AudioStream'].read())

print(f"Audio saved to {output_file}")
