# Fresh Tomatoes - Movie Trailer Website

A Python application that generates a website to display your favorite movies with their trailers.

## Project Overview

This project creates a dynamic website that showcases your favorite movies. Each movie displays a poster image, and clicking on a movie opens its YouTube trailer in a modal window.

## Files Included

- `fresh_tomatoes.py` - Module that generates the HTML webpage (provided)
- `media.py` - Defines the Movie class for storing movie information
- `entertainment_center.py` - Creates movie instances and generates the website
- `fresh_tomatoes.html` - Generated HTML file (created when you run the program)

## Requirements

- Python 3.x
- A web browser

## How to Run

1. **Install Python** (if not already installed)
   - Download from <https://www.python.org/>

2. **Navigate to the project directory:**

   ```bash
   cd /path/to/ud036_StarterCode
   ```

3. **Run the entertainment center script:**

   ```bash
   python entertainment_center.py
   ```

4. **Start a local web server to view the trailers:**

   The YouTube trailers require a local web server due to browser security restrictions. In a new terminal window, run:

   ```bash
   python -m http.server 8000
   ```

5. **View your movie website:**
   - Open your web browser and go to: `http://localhost:8000/fresh_tomatoes.html`
   - Click on any movie poster to watch its trailer
   - To stop the server, press `Ctrl+C` in the terminal

**Note:** Opening `fresh_tomatoes.html` directly in your browser (file:// protocol) will not work for YouTube trailers due to security restrictions. You must use the local web server.

## How to Customize

To add your own favorite movies, edit `entertainment_center.py`:

1. Create a new Movie instance:

   ```python
   movie_name = Movie(
       "Movie Title",
       "URL_to_poster_image",
       "YouTube_trailer_URL"
   )
   ```

2. Add it to the `movies` list:

   ```python
   movies = [existing_movies, movie_name]
   ```

3. Run the script again to regenerate the website

## Movie Trailer URLs

YouTube URLs can be in the following formats:

- `https://www.youtube.com/watch?v=VIDEO_ID`
- `https://youtu.be/VIDEO_ID`

## Project Structure

The Movie class in `media.py` has the following properties:

- `title` - The name of the movie
- `poster_image_url` - URL to the movie's poster image
- `trailer_youtube_url` - URL to the movie's YouTube trailer

## Notes

- Poster images should be hosted externally (e.g., IMDb, Amazon, etc.)
- Make sure YouTube trailer URLs are publicly accessible
- The website uses Bootstrap 3 for styling

## Archival Note

This repository is deprecated. For issues or suggestions, please visit:

- <https://knowledge.udacity.com/> forum for content-specific issues
- Submit a support ticket with your forked repository link if needed
