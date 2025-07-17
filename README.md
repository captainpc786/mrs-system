# Movie Recommender System

A web-based Movie Recommender System built with Streamlit. This app suggests movies similar to your selection, displaying their posters and titles using data from The Movie Database (TMDb).

## Features
- Select a movie from a dropdown list
- Get 5 similar movie recommendations
- View posters and titles of recommended movies
- Fast and interactive web interface

## Demo
![Demo Screenshot](demo_screenshot.png)

**Live App:** [https://mrs-system-23glkb7jpwnvotrjakcnym.streamlit.app/](https://mrs-system-23glkb7jpwnvotrjakcnym.streamlit.app/)

## Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd movie-recommender
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Download required files:**
   - Ensure `movies.pkl` is present in the project directory.
   - The app will automatically download `similarity.pkl` from Google Drive.

## Usage

Run the Streamlit app:
```bash
streamlit run mrsapp.py
```

Open the provided local URL in your browser to use the app.

## File Structure
```
movie recommanded/
├── movies.pkl
├── mrsapp.py
├── myappp/
├── Procfile
├── project link.txt
├── requirements.txt
├── setup.sh
```

## Requirements
- Python 3.7+
- See `requirements.txt` for full list

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.


## Contact
For questions or feedback, please contact pushpendrachauhan9494@gmail.com. 
