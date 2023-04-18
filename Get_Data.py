import csv
import json

with open("AnimeList.csv", "r", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    animes_data = []

    for row in reader:
        anime_id = int(row["anime_id"]) if row["anime_id"].isdigit() else 0
        title = row["title"]
        title_english = row["title_english"] if row["title_english"] else title
        source = row["source"]
        episodes = int(row["episodes"]) if row["episodes"].isdigit() else 0
        score = float(row["score"]) if row["score"].replace(".", "").isdigit() else 0.0
        scored_by = int(row["scored_by"]) if row["scored_by"].isdigit() else 0
        rank = int(row["rank"]) if row["rank"].isdigit() else 0
        popularity = int(row["popularity"]) if row["popularity"].isdigit() else 0

        animes_data.append(
            {
                "anime_id": anime_id,
                "title": title,
                "title_english": title_english,
                "source": source,
                "episodes": episodes,
                "score": score,
                "scored_by": scored_by,
                "rank": rank,
                "popularity": popularity,
            }
        )

with open("animes.json", "w", encoding="utf-8") as jsonfile:
    json.dump(animes_data, jsonfile, ensure_ascii=False, indent=4)

print("Animes data saved to 'animes.json'")
