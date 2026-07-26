# Show-Dialogue-Analyzer
A Python script utilizing the Groq API (Or whatever other API you want) to scan and analyze TV show dialogue datasets (from kaggle) for specific behavioral patterns/character interactions.

---

## Folder Structure

This repository is organized into distinct directories to separate the customizable framework from a working example!

* **`/custom/`**
  * Contains the **general-purpose template script** !! (`analyzer.py`). 
  * You can use this blank-canvas version to point at *any* dataset, filter for *any* characters, and write your own custom prompts for text analysis!
* **`/tbbt_example/`**
  * Contains a **ready-to-run example** built specifically to scan *The Big Bang Theory* dataset.
  * Uses the custom script logic to scan Seasons 3–10 for Howard and Bernadette's couple role-play gags (because i wanted to write a VERY VERY VERY accurate fanfic.), complete with pre-filtered skip logic (because Bernadette only appeared in the show on S3E5!) + the prompt!

---
## Setup & Installation

1. **Clone the Repository:**
Download/clone this repository (Or, you can choose from the two directories.)

2. **Libraries:**
Make sure you have Python installed, then install the required libraries:

       pip install pandas groq 

Note: You can use the API key of your choice
    
3. **Set Up Your Groq API Key:**

Get an API key and paste it into the script where indicated (client = Groq(api_key="")).

4. **Run the Script!**

Made with 🩷 by @Nasvyni (And Bernadette + Howard too I guess)
