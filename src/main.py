"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


PROFILES = {
    "High-Energy Pop": {"genre": "pop", "mood": "happy", "energy": 0.9},
    "Chill Lofi": {"genre": "lofi", "mood": "chill", "energy": 0.4, "likes_acoustic": True},
    "Deep Intense Rock": {"genre": "rock", "mood": "intense", "energy": 0.95},
    "Adversarial (metal / peaceful / low energy)": {"genre": "metal", "mood": "peaceful", "energy": 0.15},
}


def main() -> None:
    songs = load_songs("data/songs.csv")

    for profile_name, user_prefs in PROFILES.items():
        print(f"\n--- {profile_name} ---")
        print(f"Profile: {user_prefs}\n")
        print(f"{'#':<3} {'Title':<25} {'Score':<7} Reasons")
        print("-" * 70)

        recommendations = recommend_songs(user_prefs, songs, k=5)
        for i, (song, score, explanation) in enumerate(recommendations, start=1):
            print(f"{i:<3} {song['title']:<25} {score:<7.2f} {explanation}")


if __name__ == "__main__":
    main()
