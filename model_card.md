# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

The genre weight is too strong. I tested a profile where someone wanted metal but with peaceful, low energy music. The system returned Iron Curtain as the top result even though its energy is 0.97. Autumn Prelude was a much better fit but ranked second just because the genre label did not match. The catalog is also pretty unbalanced. Lofi has three songs while most other genres have only one, so lofi users always get solid results and genres like folk or classical barely show up for anyone. There is also no way to get a surprising recommendation. The system just keeps returning the closest match with no variety built in.  

---

## 7. Evaluation  

I tested four profiles: High-Energy Pop, Chill Lofi with an acoustic preference, Deep Intense Rock, and an adversarial case that mixed metal with peaceful low-energy preferences. For each one I checked whether the top 5 results felt right and whether the reasons made sense.

The Chill Lofi profile worked well. The top 3 were all actual lofi tracks and the acoustic bonus pushed Midnight Coding and Library Rain ahead of Focus Flow, which lined up well with expectations. The rock profile showed a problem right away. There is only one rock song in the catalog so Storm Runner wins by a huge margin and the rest of the slots just fill up with high-energy songs from other genres. The adversarial profile was the most interesting. Iron Curtain ranked first even though its energy was completely wrong, which showed how much the genre weight can dominate everything else. When I ran the weight shift experiment and cut genre in half, Autumn Prelude moved to the top and Iron Curtain dropped out entirely.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

The thing that surprised me most was the adversarial profile. I went in thinking genre was the obvious thing to weight highest and for most normal profiles it works fine. But when the genre and everything else point in opposite directions the system just breaks. It recommended a near-max-energy metal track to someone who said they wanted something peaceful and quiet. A person can like metal but want something calm right now and the system has no way to handle that. Spotify probably deals with this by having some kind of session or mood layer separate from your long-term taste. This simulation does not have that at all. The chill lofi profile felt the most accurate out of everything I tested, mostly because the catalog happens to have three lofi songs and they are all pretty different from each other in energy.
