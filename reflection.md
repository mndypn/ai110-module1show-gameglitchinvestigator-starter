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

I used Claude to ask questions about the app and suggestions to fix. 
An example of a correct AI suggestion was that it pointed out that secret was being turned into a string, causing incorrect hints, and I verified this by confirming the correct hints after fixing it. 
An example of an incorrect AI suggestion was that when I asked it to refactor the fixed check_guess function to logic.utils and import to app.py, it would give me different ways of fixing the function on each file.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I considered a bug fixed when the game worked correctly across many rounds and the same issue didn’t reappear after changing difficulty or restarting the app.
One test I ran was switching difficulties and checking whether the secret number stayed inside the correct range. This showed me that the secret range not updating bug was gone because each difficulty change produced a new valid secret.
AI helped me understand the code by explaining parts of the logic in plain language, which made it easier to see what each function was supposed to do.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Streamlit reruns your whole script every time you click anything, almost like it’s starting fresh each time. Session state is the place where you save the things you don’t want it to forget, like the secret number or your score.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One strategy I want to reuse in future projects is to break up the code into sections when I am debugging.
One thing I would do differently is to make more commits, since I would often forget to commit.
This project changed the way I think about AI generated code because I learned that AI needs clear and precise instructions and that you should double check suggestions instead of assuming they are correct.