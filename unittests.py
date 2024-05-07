import unittest
from unittest.mock import patch
import os
from musiclibrary import *

class TestMusicLibrary(unittest.TestCase):
    def setUp(self):
        self.library = MusicLibrary()
        self.track1 = Track("Song 1", "Artist A", "Album Y", "Pop", 2020)
        self.track2 = Track("Song 2", "Artist B", "Album Z", "Rock", 2021)
        self.track3 = Track("Song 3", "Artist A", "Album X", "Jazz", 2020)
        self.library.add_track(self.track1)
        self.library.add_track(self.track2)

    def test_add_track(self):
        # Test adding a new track
        response = self.library.add_track(self.track3)
        self.assertEqual(response, "Track added.")
        self.assertIn(self.track3, self.library.tracks)

        # Test adding a duplicate track
        response = self.library.add_track(self.track1)
        self.assertEqual(response, "Track already exists.")
        self.assertEqual(len(self.library.tracks), 3)

    def test_remove_track(self):
        # Test removing an existing track
        response = self.library.remove_track("Song 1")
        self.assertEqual(response, "Track removed.")
        self.assertNotIn(self.track1, self.library.tracks)

        # Test removing a non-existent track
        response = self.library.remove_track("Song 4")
        self.assertEqual(response, "Track not found.")

    def test_find_by_artist(self):
        # Test finding tracks by artist
        results = self.library.find_by_artist("Artist A")
        self.assertEqual(len(results), 1)
        self.assertIn(self.track1, results)

    def test_find_by_album(self):
        # Test finding tracks by album
        results = self.library.find_by_album("Album Z")
        self.assertEqual(len(results), 1)
        self.assertIn(self.track2, results)

    def test_list_tracks(self):
        # Test listing all tracks
        results = self.library.list_tracks()
        self.assertIn("Song 1 by Artist A on Album Y [Pop, 2020]", results)

    def test_categorize_by_genre(self):
        # Test categorization by genre
        results = self.library.categorize_by_genre()
        self.assertEqual(len(results["Pop"]), 1)

    def test_search_tracks(self):
        # Test search functionality
        results = self.library.search_tracks("Song")
        self.assertEqual(len(results), 2)

    def test_update_track_info(self):
        # Test updating track information
        response = self.library.update_track_info("Song 2", genre="Alternative", year=2022)
        self.assertEqual(response, "Updated Song 2.")
        self.assertEqual(self.track2.genre, "Alternative")
        self.assertEqual(self.track2.year, 2022)

    def test_sort_tracks_by_title(self):
        # Test sorting tracks by title
        results = self.library.sort_tracks_by_title()
        self.assertEqual(results[0].title, "Song 1")

    def test_sort_tracks_by_artist(self):
        # Test sorting tracks by artist
        results = self.library.sort_tracks_by_artist()
        self.assertEqual(results[0].artist, "Artist A")

    def test_sort_tracks_by_album(self):
        # Test sorting tracks by album
        results = self.library.sort_tracks_by_album()
        self.assertEqual(results[0].album, "Album Y")

    def test_sort_tracks_by_year(self):
        # Test sorting tracks by year
        results = self.library.sort_tracks_by_year()
        self.assertEqual(results[0].year, 2020)

    def test_find_by_year(self):
        # Test finding tracks by year
        results = self.library.find_by_year(2020)
        self.assertEqual(len(results), 1)

    def test_count_tracks(self):
        # Test counting tracks in the library
        count = self.library.count_tracks()
        self.assertEqual(count, 2)

    def test_export_import_library(self):
        filename = "test_library.csv"
        self.library.export_library(filename)
        # Check if file was created
        self.assertTrue(os.path.exists(filename))
        # Import into a new library to verify contents
        new_library = MusicLibrary()
        new_library.import_library(filename)
        self.assertEqual(len(new_library.tracks), 2)
        # Cleanup
        os.remove(filename)

if __name__ == '__main__':
    unittest.main()
