# e3f64fbf54c8f33f505061cddc4d8619

import requests
import os

# Function to fetch movie details from The Movie Database (TMDb) API
def get_movie_details(movie_title, release_year):
	api_key = "e3f64fbf54c8f33f505061cddc4d8619"
	search_url = f"https://api.themoviedb.org/3/search/movie"
	
	params = {
		"api_key": api_key,
		"query": movie_title,
		"year": release_year  # Include the release year in the search query
	}
	
	response = requests.get(search_url, params=params)
	data = response.json()
	
	if data["results"]:
		movie_details = data["results"][0]
		imdb_id = movie_details.get("imdb_id")
		poster_path = movie_details.get("poster_path")
		
		return {
			"imdb_id": imdb_id,
			"poster_url": f"https://image.tmdb.org/t/p/original{poster_path}" if poster_path else None
		}
	
	return None

# Function to download an image from a URL and save it locally
def download_image(url, filename):
	response = requests.get(url)
	if response.status_code == 200:
		with open(filename, 'wb') as f:
			f.write(response.content)
		print("✅ Image downloaded successfully!")
	else:
		print("⛔️ Error downloading image.")

# Function to create the markdown file
def create_markdown_file(title, number, movie_title):
	# Fetch movie details from The Movie Database (TMDb) API
	release_year = ""
	while not release_year:
		release_year = input("📅 Enter the expected release year: ")

	movie_data = get_movie_details(movie_title, release_year)
	
	# Extract movie details if available
	if movie_data:
		imdb_id = movie_data['imdb_id']
		image_url = movie_data['poster_url']
	else:
		print("⛔️ Error: Movie not found on The Movie Database.")
		return
	
	# Confirm TMDb information
	print("🎬 Movie details from The Movie Database:")
	print(f"Title: {movie_title}")
	print(f"Release Year: {release_year}")
	confirm_tmdb = input("❓ Is the above information correct? (y/n): ").lower()
	if confirm_tmdb != "y":
		print("⚠️ Aborted. No markdown file created.")
		return
 
	# Construct IMDb link if IMDb ID is available, otherwise prompt for input
	if imdb_id:
		imdb_link = f"https://www.imdb.com/title/{imdb_id}/"
	else:
		imdb_link = input("⚠️ Enter the IMDb link (if available): ")

	# Download and save the poster image locally
	image_filename = f"episode-{number}.jpg"
	download_image(image_url, image_filename)

	pub_date = input("🗓 Enter the publication date (YYYY-MM-DD): ")
	apple_link = input("🍏 Enter the Apple episode link: ")
	spotify_link = input("🎧 Enter the Spotify episode link: ")
	lbx_link = input("📚 Enter the Letterboxd link: ")

	# Construct content for the markdown file
	content = f"""---
layout: ../../layouts/EpisodeLayout.astro
number: {number}
title: "{title}"
pubDate: {pub_date}
episodeLink:
  apple: "{apple_link}"
  spotify: "{spotify_link}"
image:
  url: "{image_url}"
  alt: "{movie_title} Poster"
movieLinks:
  lbx: "{lbx_link}"
  imdb: "{imdb_link}"
---
"""

	# Create the markdown file
	file_name = f"{number}.md"
	with open(file_name, "w") as f:
		f.write(content)
	
	print(f"✅ Markdown file '{file_name}' created successfully!")

# Main program
if __name__ == "__main__":
	title = input("📝 Enter the episode title: ")
	number = input("🔢 Enter the number: ")
	movie_title = input("🎥 Enter the movie title: ")
	
	# Proceed with fetching TMDB data and confirming, then proceed with the rest of the inputs
	create_markdown_file(title, number, movie_title)