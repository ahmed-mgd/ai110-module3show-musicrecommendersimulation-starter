# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

VibeFinder 1.0

---

## 2. Intended Use  

This system suggests songs from a small catalog based on a user's preferred genre, mood, and energy level. It is built for classroom exploration only. It is not meant for real users or production use. It assumes the user has a single fixed preference and does not account for how taste changes depending on context or time of day.

Not to be used for: real music platforms, personalization at scale, or any use case where recommendation quality actually matters to the end user.

---

## 3. How the Model Works  

Each song in the catalog gets a score based on how closely it matches what the user said they like. Genre match gives the most points. Mood match gives a smaller boost. Energy uses a proximity calculation so a song closer to the user's target energy scores higher than one that is far away. There is also a small bonus for acoustic songs if the user said they prefer acoustic. Once every song has a score the system sorts them and returns the top five.

---

## 4. Data  

The catalog has 18 songs. I started with 10 from the starter file and added 8 more to cover genres that were missing. The catalog now includes pop, lofi, rock, hip-hop, r&b, classical, folk, country, metal, edm, soul, jazz, synthwave, indie pop, and ambient. Most genres have only one song. Lofi has three. The data reflects mostly Western popular and electronic music and does not cover non-western genres at all.

---

## 5. Strengths  

The system works best when the user's preferred genre has more than one song in the catalog. The chill lofi profile consistently returns good results because there are three lofi songs with different energy levels to choose from. The reasons output is also easy to understand. You can look at any result and immediately see exactly why it ranked where it did.

---

## 6. Limitations and Bias 

The genre weight is too strong. I tested a profile where someone wanted metal but with peaceful, low energy music. The system returned Iron Curtain as the top result even though its energy is 0.97. Autumn Prelude was a much better fit but ranked second just because the genre label did not match. The catalog is also pretty unbalanced. Lofi has three songs while most other genres have only one, so lofi users always get solid results and genres like folk or classical barely show up for anyone. There is also no way to get a surprising recommendation. The system just keeps returning the closest match with no variety built in.

---

## 7. Evaluation  

I tested four profiles: High-Energy Pop, Chill Lofi with an acoustic preference, Deep Intense Rock, and an adversarial case that mixed metal with peaceful low-energy preferences. For each one I checked whether the top 5 results felt right and whether the reasons made sense.

The Chill Lofi profile worked well. The top 3 were all actual lofi tracks and the acoustic bonus pushed Midnight Coding and Library Rain ahead of Focus Flow, which lined up well with expectations. The rock profile showed a problem right away. There is only one rock song in the catalog so Storm Runner wins by a huge margin and the rest of the slots just fill up with high-energy songs from other genres. The adversarial profile was the most interesting. Iron Curtain ranked first even though its energy was completely wrong, which showed how much the genre weight can dominate everything else. When I ran the weight shift experiment and cut genre in half, Autumn Prelude moved to the top and Iron Curtain dropped out entirely.

---

## 8. Future Work  

First I would add more songs per genre so the catalog is more balanced. Right now most genres only have one entry which means users outside of lofi or pop do not get meaningful variety in their results. Second I would add some kind of diversity rule so the top 5 cannot all be from the same genre. Third I would separate long-term taste from session mood so a user could say they like metal overall but want something calm right now, which is a totally normal thing to want.

---

## 9. Personal Reflection  

The thing that surprised me most was the adversarial profile. I went in thinking genre was the obvious thing to weight highest and for most normal profiles it works fine. But when the genre and everything else point in opposite directions the system just breaks. It recommended a near max energy metal track to someone who said they wanted something peaceful and quiet. A person can like metal but want something calm right now and the system has no way to handle that. Spotify probably deals with this by having some kind of session or mood layer separate from your long-term taste. This simulation does not have that at all. The chill lofi profile felt the most accurate out of everything I tested, mostly because the catalog happens to have three lofi songs and they are all quite different from each other in energy.
