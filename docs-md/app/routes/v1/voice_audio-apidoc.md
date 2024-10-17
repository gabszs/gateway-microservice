Below is a detailed documentation for the provided Python script that uses the Google Cloud Text-to-Speech API to convert text into WAV audio files.

---

# File Documentation: `voice_audio.py`

## Overview
This script uses the Google Cloud Text-to-Speech API to synthesize speech from text and save it as a WAV audio file. The script is designed to handle multiple languages and voice configurations by specifying the voice name and the respective language code. It requires Google Cloud credentials to authenticate API requests.

## Dependencies
- `google-cloud-texttospeech`: The Google Cloud client library for the Text-to-Speech API.
- `google.oauth2.service_account`: Used to authenticate using a service account key file.

## Functions

### `text_to_wav(voice_name: str, text: str, credentials_path: str)`
Converts a given text string to a WAV audio file using a specified voice.

#### Parameters:
- `voice_name`: A string representing the name of the voice to be used for synthesis. This also implies the language.
- `text`: The text content to be converted into speech.
- `credentials_path`: The file path to the Google Cloud service account JSON credentials.

#### Key Steps:
1. **Authenticate**: Loads the Google Cloud credentials from the provided JSON credentials file.
2. **Extract Language Code**: Derives the language code from the `voice_name` by splitting it at hyphens and joining the first two segments (e.g., "pt-BR" from "pt-BR-Wavenet-A").
3. **Set Up Synthesis Input**: Prepares the text input for the synthesis process.
4. **Configure Voice Parameters**: Establishes the language code and voice name for the synthesis.
5. **Audio Configuration**: Sets the audio encoding to LINEAR16, which is suitable for WAV files.
6. **Synthesize Speech**: Calls the `synthesize_speech` method of the `TextToSpeechClient` to convert the text to audio.
7. **Save Audio File**: Writes the resulting audio content to a WAV file named after the `voice_name`.

#### Output:
- A WAV file containing the synthesized speech is saved in the current directory with a name matching the `voice_name`.

## Main Execution
The script includes a main block that executes when the script is run directly. It performs the following tasks:

1. **Define Credentials Path**: Specifies the path to the Google Cloud service account credentials JSON file.
2. **Example Texts**:
   - `text_pt`: A sample text in Portuguese.
   - `text_en`: A sample text in English.
3. **Call `text_to_wav` Function**:
   - Converts the Portuguese text to speech using the "pt-BR-Wavenet-A" voice.
   - Converts the English text to speech using the "en-US-Wavenet-D" voice.

## Usage
To use this script:
1. Ensure that the `google-cloud-texttospeech` library is installed.
2. Obtain a Google Cloud service account JSON key file with appropriate Text-to-Speech permissions.
3. Adjust the `credentials_path` to point to your service account key file.
4. Modify the `text` variables and `voice_name` parameters as needed for your use case.
5. Run the script to generate the WAV files.

## Notes
- The script assumes that the Google Cloud SDK is set up correctly and that billing is enabled on the associated Google Cloud project.
- The generated WAV files are saved in the same directory where the script is executed.
- Ensure that the voice names and language codes used are supported by the Google Cloud Text-to-Speech API.

---