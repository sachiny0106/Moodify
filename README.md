# Moodify 🎵

Moodify is an emotion-based music recommender system that curates a personalized listening experience just for you. By analyzing your facial expressions in real-time, Moodify detects your current mood and plays songs that match your vibe from Spotify, SoundCloud, or YouTube.

**Live Demo:** [Check it out here](https://vibescape.streamlit.app/) *(Note: Demo link might still reflect the old version)*

## Features

-   **Emotion Recognition:** Uses a webcam to detect emotions like Happy, Sad, Angry, Fear, Surprise, and Neutral.
-   **Multi-Platform Support:** Seamlessly integrates with Spotify, SoundCloud, and YouTube.
-   **Smart Recommendations:** Automatically selects playlists that fit your detected mood.
-   **Analyzer Tool:** Search for tracks and artists to visual their audio features (danceability, energy, etc.).

## Installation

1.  **Clone the repo:**
    ```bash
    git clone https://github.com/yourusername/Moodify.git
    cd Moodify
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Setup Credentials:**
    -   Create a file named `.env` in the root directory.
    -   Add your Spotify API keys (get them from the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/)):
        ```env
        SPOTIPY_CLIENT_ID=your_client_id_here
        SPOTIPY_CLIENT_SECRET=your_client_secret_here
        ```

## Usage

1.  **Run the App:**
    ```bash
    streamlit run 1_🎵_Homepage.py
    ```

2.  **Groove:**
    -   Allow camera access when prompted.
    -   Let Moodify scan your emotion.
    -   Navigate to your preferred music service from the sidebar and enjoy!

## Tech Stack

-   **Frontend:** Streamlit
-   **Computer Vision:** MediaPipe, OpenCV
-   **ML Model:** Keras/TensorFlow
-   **APIs:** Spotify Web API

## Contributing

Feel free to fork this project and submit PRs. If you find any bugs, just open an issue!

## License

MIT License. See [LICENSE](LICENSE) for more info.
