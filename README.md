# Audio Generator

This script generates audio files using the ElevenLabs API for given test values.

## Requirements

- Python 3.10.5
- `elevenlabs` package (Install using `pip install elevenlabs`)

## Usage

1. Clone the repository or download the script `audio_generator.py`.
2. Ensure you have Python 3.10.5 installed on your system.
3. Install the required packages using `pip install -r requirements.txt`.
4. Obtain an API key from ElevenLabs and replace the placeholder `API_KEY` in the script with your actual API key.
5. Run the script using the following command:

    ```bash
    python audio_generator.py <test_values> [--output_dir OUTPUT_DIR]
    ```

    - `<test_values>`: Comma-separated list of test values for which you want to generate audio.
    - `--output_dir OUTPUT_DIR` (Optional): Directory to save the audio files. Defaults to `output_audio`.

Example:

```bash
python audio_generator.py "Hello,How are you?,I am fine,Thank you" --output_dir generated_audio
