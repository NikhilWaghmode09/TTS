import os
import argparse
from elevenlabs import play
from elevenlabs.client import ElevenLabs

# Define your ElevenLabs API key here
API_KEY = "0205c9ff320b9c203fd19b8d30d61f72"

# Function to generate and save audio
def generate_audio(client, test_value, output_filename):
    audio_generator = client.generate(
        # text=f"Hello My friend {test_value}. Really excited to see you tonight.",
        text = test_value,
        voice="LrnwgcdTLxc99sutUxGU",
        model="eleven_multilingual_v2"
    )
    
    with open(output_filename, "wb") as file:
        for audio_chunk in audio_generator:
            file.write(audio_chunk)
    print(f"Generated audio for '{test_value}' and saved to '{output_filename}'")

def parse_arguments():
    parser = argparse.ArgumentParser(description="Generate audio files for given test values.")
    parser.add_argument("test_values", help="Comma-separated list of test values")
    parser.add_argument("--output_dir", default="output_audio", help="Directory to save the audio files")
    return parser.parse_args()

def main():
    args = parse_arguments()

    # Initialize ElevenLabs client
    client = ElevenLabs(api_key=API_KEY)

    # Get the test values
    test_values = [value.strip() for value in args.test_values.split(',')]

    # Directory to save the audio files
    os.makedirs(args.output_dir, exist_ok=True)

    # Generate and save audio for each test value
    for test_value in test_values:
        output_filename = f"{test_value}.mp3"
        output_filepath = os.path.join(args.output_dir, output_filename)
        generate_audio(client, test_value, output_filepath)

    print("All audio files have been generated and saved.")

if __name__ == "__main__":
    main()
