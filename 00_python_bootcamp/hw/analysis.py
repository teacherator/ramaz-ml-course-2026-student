"""HW00 — Analysis: Songs Dataset

Implement the pieces below using plain Python: file I/O, a Counter-based
aggregation, and a small class hierarchy for ranking songs. The dataset is
data/songs.csv (open it to see the raw rows). Its columns are:

    title             str    song title
    artist            str    performing artist
    genre             str    e.g. Pop, Rock, Hip-Hop
    year              int    year the song charted
    weeks_on_chart    int    total weeks the song spent on the chart
    peak_position     int    best chart position reached (1 = number one)
    streams_millions  float  total streams, in millions

After completing the functions, run this script to print your results:

    uv run python analysis.py

Use the printed output to answer the questions in writeup.md.
"""

from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path


def load_songs(path: Path) -> list[dict]:
    """Load the songs CSV and return a list of records, one dict per row.

    Casts year, weeks_on_chart, and peak_position to int, and
    streams_millions to float. All other fields stay strings.

    Args:
        path: Path to the songs CSV file.

    Returns:
        A list of dicts, one per song, with the correct field types.

    Example:
        >>> songs = load_songs(Path("data/songs.csv"))
        >>> isinstance(songs[0]["year"], int)
        True
    """
    songlist=[]
    with open(path, newline='') as csvfile:
        songreader = csv.DictReader(csvfile)
        
        for row in songreader:
            
            row['year']= int(row['year'])
            row['weeks_on_chart']= int(row['weeks_on_chart'])
            row['peak_position']= int(row['peak_position'])
            row['streams_millions']= float(row['streams_millions'])
            #print(row)
            songlist.append(row)
           
    return songlist


class SongRanker:
    """Base class for ranking a list of songs by some criterion.

    Subclasses implement score() to define what "best" means; rank() is
    shared logic that works for any scoring rule.
    """

    def score(self, song: dict) -> float:
        """Return the value used to rank this song. Higher is better.

        Subclasses must override this.
        """
        raise NotImplementedError("not implemented")
 
       

    def rank(self, songs: list[dict], n: int = 10) -> list[dict]:
        """Return the top n songs, highest score() first.

        Args:
            songs: List of song records (as returned by load_songs).
            n: Number of songs to return (default 10).

        Returns:
            A list of the n songs with the highest score(), sorted
            highest-first. Ties may break in any order.

        Example:
            >>> top = StreamsRanker().rank(songs, n=3)
            >>> len(top)
            3
            >>> top[0]["streams_millions"] >= top[1]["streams_millions"]
            True

        https://docs.python.org/3/library/csv.html


        """
       
       

        return sorted(songs, key=lambda song: self.score(song), reverse=True)[:n]



class StreamsRanker(SongRanker):
    """Ranks songs by total streams_millions."""

    def score(self, song: dict) -> float:
        return  song["streams_millions"]


class LongevityRanker(SongRanker):
    """Ranks songs by weeks_on_chart (how long they stuck around)."""

    def score(self, song: dict) -> float:
        return song["weeks_on_chart"]


def avg_weeks_by_genre(songs: list[dict]) -> dict[str, float]:
    """Return the average weeks_on_chart for each genre.

    Args:
        songs: List of song records.

    Returns:
        A dict mapping genre name (str) to average weeks (float).

    Example:
        >>> avgs = avg_weeks_by_genre(songs)
        >>> isinstance(avgs, dict)
        True
        >>> all(isinstance(v, float) for v in avgs.values())
        True

        return {'Pop':39.0, 'Rock', 23.0}

        {'title': 'Slow It Down', 'artist': 'Benson Boone', 'genre': 'Pop', 'year': '2024',
          'weeks_on_chart': '10', 'peak_position': '12', 'streams_millions': '350.0'}

          for each genre we need the total weeks / number of songs
          so should we first make a list of dicts like
          [
          {'genre':'Pop', 'songs':[dict]}
          ]
    """
   
    #print(hashable_data)
    #get a listy of genres
    #genres=set(s['genre'] for s in songs )
    avg={}
    tweeks = Counter()
    nweeks = Counter(s["genre"] for s in songs if "genre" in s)#counts the number of songs with each genre
    for s in songs:
        tweeks[s['genre']]+=s['weeks_on_chart']
       
    
    for g in tweeks:
        avg[g]=tweeks[g]/nweeks[g]
   
    return avg


def most_streamed_artist(songs: list[dict]) -> str:
    """Return the name of the artist with the highest total streams_millions.

    If an artist has multiple songs, sum all their streams.

    Args:
        songs: List of song records.

    Returns:
        The artist name as a string.

    Example:
        >>> artist = most_streamed_artist(songs)
        >>> isinstance(artist, str)
        True
    """
    #artists = Counter(s["artist"] for s in songs if "artist" in s)
    artists = Counter()
    for s in songs:
        artists[s['artist']]+=s['streams_millions']
    #print(artists.most_common(1)[0][0])

    return artists.most_common(1)[0][0]


def hits_per_year(songs: list[dict], max_position: int = 10) -> dict[int, int]:
    """Count songs with peak_position <= max_position, grouped by year.

    A "hit" is any song that reached position max_position or better (lower
    number). Only years that have at least one hit appear in the result; a
    year with no qualifying songs is omitted entirely (do not include it with
    a count of 0).

    Args:
        songs: List of song records.
        max_position: Peak position threshold (default 10).

    Returns:
        A dict mapping year (int) to hit count (int).
        {1970:1000,1971:2000}

    Example:
        >>> hits = hits_per_year(songs, max_position=5)
        >>> all(isinstance(k, int) for k in hits.keys())
        True
    """
  
    hits = Counter(s["year"] for s in songs if s["peak_position"] <= max_position)
    return dict(hits)


# ── Main: print results for writeup.md ────────────────────────────────────────

if __name__ == "__main__":
    data_path = Path(__file__).parent / "data" / "songs.csv"
    songs = load_songs(data_path)

    print("=== Top 10 Songs by Streams ===")
    top = StreamsRanker().rank(songs, n=10)
    for song in top:
        print(f"  {song['title']} — {song['artist']} ({song['streams_millions']:.0f}M streams)")

    print("\n=== Top 10 Songs by Weeks on Chart ===")
    longest = LongevityRanker().rank(songs, n=10)
    for song in longest:
        print(f"  {song['title']} — {song['artist']} ({song['weeks_on_chart']} weeks)")

    print("\n=== Average Weeks on Chart by Genre ===")
    avg_weeks = avg_weeks_by_genre(songs)
    for genre, avg in sorted(avg_weeks.items(), key=lambda x: -x[1]):
        n_songs = sum(1 for s in songs if s["genre"] == genre)
        label = "song" if n_songs == 1 else "songs"
        print(f"  {genre}: {avg:.1f} weeks  ({n_songs} {label})")

    print("\n=== Most Streamed Artist ===")
    artist = most_streamed_artist(songs)
    total_streams = sum(s["streams_millions"] for s in songs if s["artist"] == artist)
    print(f"  {artist} ({total_streams:.0f}M total streams)")

    print("\n=== Top-10 Hits per Year (peak position <= 10) ===")
    hits = hits_per_year(songs, max_position=10)
    for year, count in sorted(hits.items()):
        print(f"  {year}: {count} hit(s)")
