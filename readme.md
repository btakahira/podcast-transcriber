# Podcast Transcription Tool

This is a Python-based tool for transcribing podcast audio files (MP3 or WAV) to text. The transcription is done locally using the **Vosk** speech-to-text engine, which supports Brazilian Portuguese and does not require an internet connection.

---

## **Features**
- Converts MP3 files to WAV automatically (if needed).
- Transcribes audio files locally without using cloud services.
- Displays a user-friendly progress bar with percentage and estimated time remaining.
- Saves the transcription as a `.txt` file with the same name as the input audio file.

---

## **Requirements**
- Python 3.7 or later
- The **Vosk** model for Brazilian Portuguese
- Required Python libraries:
  - `vosk`
  - `pydub`

---

## **Installation**

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/podcast-transcription-tool.git
   cd podcast-transcription-tool
   ```

2. **Install Dependencies**
   Use `pip` to install the required libraries:
   ```bash
   pip install vosk pydub
   ```

3. **Download the Vosk Model for Brazilian Portuguese**
   - Go to the [Vosk models page](https://alphacephei.com/vosk/models).
   - Download the **Brazilian Portuguese** model (e.g., `vosk-model-small-pt`).
   - Extract the downloaded folder and place it in the same directory as the script.

   Example folder structure:
   ```
   podcast-transcription-tool/
   ├── vosk-model-small-pt/
   ├── transcribe_podcast.py
   ├── README.md
   ```

---

## **Usage**

Run the script from the command line, passing the audio file (MP3 or WAV) as an argument:

```bash
python transcribe_podcast.py <input_file>
```

### Example
For an MP3 file:
```bash
python transcribe_podcast.py podcast.mp3
```

For a WAV file:
```bash
python transcribe_podcast.py podcast.wav
```

### Output
- A `.txt` file with the transcription will be created in the same directory.
- The file will have the same name as the input audio file, e.g.:
  - Input: `podcast.mp3`
  - Output: `podcast.txt`

---

## **Example Output**

```
Converting MP3 to WAV...
Conversion completed: podcast.wav
Transcribing audio...
[#######################                      ] 50.0% - ETA: 30.5 sec
Finalizing transcription...
Transcription saved to: podcast.txt

Transcription completed:
----------------------------------------
This is the transcribed text from the podcast...
----------------------------------------
```

---

## **Notes**
- Ensure the audio file is clear for accurate transcription.
- Only MP3 and WAV files are supported.
- The Vosk model requires audio in mono and a 16 kHz sample rate. This script automatically converts the audio if needed.

---

## **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## **Acknowledgments**
- [Vosk Speech Recognition](https://alphacephei.com/vosk/)
- [pydub Library](https://github.com/jiaaro/pydub)
