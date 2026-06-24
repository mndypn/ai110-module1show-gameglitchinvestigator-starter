# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

The game prompted me to make a guess between 1 and 100 (the Normal difficulty range) and showed me the attempts remaining. When I made a guess, sometimes the hint was backwards, so it would say "go higher" when the actual number is lower for example. It also seemed to malfunction based on the attempt number as even if I input the same guess, it would switch back and forth from a hint of go lower to go higher on the next. The game also ended earlier than expected as Normal gives 8 attempts but ends on the 7th attempt since the attempt counter starts at 1 before starting a game. When the difficulty is changed, the secret does not generate in the respective range and always generates within the Normal 0 to 100 range. The start new game feature also does not work correctly as it does not allow replay.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| guess of 2 on attempts left: 1 | hint: go HIGHER | hint: go LOWER, Out of attempts! The secret was 90. Score: -35 | none |
| difficulty set to easy | range 0 to 20 | range still is 0 to 100 | none |
| guess of 5 on all attempts (secret: 27) | hint: go HIGHER | hint is correct on odd numbered attempt, shows go LOWER for even numbered attempt | none |
| switch difficulties and start new game | secret generates within the difficulty range | secret generates 0 to 100 | none |
| start new game after ending a game | allows player to replay game | still shows game over | none |
| no guess | attempts should be 8 left and on attempt 0 | Attempts left: 7 and debug panel Attempts: 1 | Attempts: 1 | 

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used Claude to ask questions about the app and suggestions to fix. An example of a correct AI suggestion was that it 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
