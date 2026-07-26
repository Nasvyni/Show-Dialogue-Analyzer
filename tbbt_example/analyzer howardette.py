import os
import time
import pandas as pd
from groq import Groq

# Paste your Groq API key here muehehe
client = Groq(api_key="")

csv_filename = "1_10_seasons_tbbt.csv"
if not os.path.exists(csv_filename):
    print(f"Error: Could not find {csv_filename}.")
    exit()

print("Loading Kaggle dataset...")
df = pd.read_csv(csv_filename)

output_filename = "howard_bernadette_roleplay_s3e5_onwards.md"

with open(output_filename, "w", encoding="utf-8") as out_f:
    out_f.write("# Howard and Bernadette Role-Play Gags (S3E5 Onwards)\n\n")

    for episode_name, group in df.groupby('episode_name', sort=False):
        
        # SKIP LOGIC: Skip anything before Season 3 Episode 5
        if "Series 01" in episode_name or "Series 02" in episode_name:
            continue
        if "Series 03" in episode_name:
            ep_num_str = episode_name.split("Episode")[1].strip()[:2]
            if ep_num_str.isdigit() and int(ep_num_str) < 5:
                print(f"Skipping {episode_name}...")
                continue

        print(f"Analyzing {episode_name}...")
        
        episode_text = "\n".join([f"{row['person_scene']}: {row['dialogue']}" for _, row in group.iterrows()])
        
        prompt = f"""STRICT FILTER INSTRUCTION: You are a strict data parser. You are analyzing an episode of The Big Bang Theory. 
Your ONLY objective is to find  conversations or scenes where **Howard and Bernadette** (as a couple) engage in or talk about THEIR (Bernadette and Howard's) **bedroom/couple role-play** (e.g., pretending to be people who they are not).

 RULES:
1. Ignore ALL other characters (Sheldon, Leonard, Raj, Penny, Amy, etc.). If they are doing role-play, it does NOT count.
2. If Howard and Bernadette are not in the episode, or if they are just having a normal conversation without a role-play gag, you MUST output ONLY the word: NONE. Do not write anything else.
3. Do not hallucinate quotes or mix up episodes.

If and ONLY IF you find a REAL Howard & Bernadette role-play gag in this text, output it in this exact format:
- **Episode:** {episode_name}
- **Scenario:** (brief description)
- **Quote:** (short dialogue proof)

Dialogue Text:
{episode_text[:15000]}"""
        
        try:
            chat_completion = client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model="llama-3.3-70b-versatile", # Switched to 70B for much higher accuracy
            )
            
            result_text = chat_completion.choices[0].message.content.strip()
            print(result_text)
            
            # Only save real results, completely ignore "NONE"
            if "NONE" not in result_text.upper():
                out_f.write(result_text + "\n\n---\n\n")
            
        except Exception as e:
            print(f"Skipped due to error: {e}")
            time.sleep(10)
        
        time.sleep(2)

print(f"Done! Results saved to: {output_filename}")
