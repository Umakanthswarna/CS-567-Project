import logging

# Set up basic configuration for logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Track:
    def __init__(self, title, artist, album, genre, year=None):
        self.title = title
        self.artist = artist
        self.album = album
        self.genre = genre
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.artist} on {self.album} [{self.genre}, {self.year}]"

class MusicLibrary:
    def __init__(self):
        self.tracks = []

    def add_track(self, track):
        if track not in self.tracks:
            self.tracks.append(track)
            logging.info(f"Track added: {track}")
            return "Track added."
        logging.warning("Attempted to add a track that already exists.")
        return "Track already exists."

    def remove_track(self, title):
        for track in self.tracks:
            if track.title == title:
                self.tracks.remove(track)
                logging.info(f"Track removed: {track}")
                return "Track removed."
        logging.warning("Attempted to remove a track that does not exist.")
        return "Track not found."

    def find_by_artist(self, artist):
        found = [track for track in self.tracks if track.artist.lower() == artist.lower()]
        if not found:
            logging.info(f"No tracks found for artist: {artist}")
        return found

    def find_by_album(self, album):
        found = [track for track in self.tracks if track.album.lower() == album.lower()]
        if not found:
            logging.info(f"No tracks found for album: {album}")
        return found

    def list_tracks(self):
        if not self.tracks:
            return "No tracks in library."
        return "\n".join(str(track) for track in self.tracks)

    def categorize_by_genre(self):
        genre_dict = {}
        for track in self.tracks:
            genre_list = genre_dict.setdefault(track.genre, [])
            genre_list.append(track)
        return genre_dict

    def search_tracks(self, keyword):
        found = [track for track in self.tracks if keyword.lower() in track.title.lower() or keyword.lower() in track.artist.lower()]
        if not found:
            logging.info(f"No tracks found matching keyword: {keyword}")
        return found

    def update_track_info(self, title, **kwargs):
        for track in self.tracks:
            if track.title == title:
                for key, value in kwargs.items():
                    setattr(track, key, value)
                logging.info(f"Updated track info for {title}: {kwargs}")
                return f"Updated {title}."
        return "Track not found."

    def sort_tracks_by_title(self):
        sorted_tracks = sorted(self.tracks, key=lambda x: x.title.lower())
        return sorted_tracks

    def sort_tracks_by_artist(self):
        sorted_tracks = sorted(self.tracks, key=lambda x: x.artist.lower())
        return sorted_tracks

    def sort_tracks_by_album(self):
        sorted_tracks = sorted(self.tracks, key=lambda x: x.album.lower())
        return sorted_tracks

    def sort_tracks_by_year(self):
        sorted_tracks = sorted(self.tracks, key=lambda x: x.year)
        return sorted_tracks

    def find_by_year(self, year):
        found = [track for track in self.tracks if track.year == year]
        if not found:
            logging.info(f"No tracks found for year: {year}")
        return found

    def count_tracks(self):
        return len(self.tracks)

    def export_library(self, filename):
        with open(filename, 'w') as file:
            for track in self.tracks:
                file.write(f"{track.title},{track.artist},{track.album},{track.genre},{track.year}\n")
        logging.info(f"Library exported to {filename}")

    def import_library(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                title, artist, album, genre, year = line.strip().split(',')
                if year == "":
                    year = None
                track = Track(title, artist, album, genre, year)
                self.add_track(track)
        logging.info(f"Library imported from {filename}")