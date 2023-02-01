# Hack Technology / Project Attempted


## What you built? 

I built a quiz generator-it takes a chunk of text (presumably an article or perhaps youtube subtitles) and gets the most common words, filters out stop words and words that are too common, and then generates a short quiz where the user must produce the spanish translation.

There isn't a whole lot of code, however, I spent a lot of time working on different APIs and setting them up. I started with an unofficial package called 'googletrans' that wraps the google translate API, then did the official google cloud API, then did Microsoft Azure's translation.

## Who Did What?

I worked by myself.

## What you learned

I learned a lot about the different translation options out there. The first one, googletrans, worked well, but was advertised as potentially unreliable. As a result, I switched to google cloud. However, setting up google cloud was a HUGE pain in the butt. Just getting to the point where the API was enabled was a hassle, and then authenticating my local environment was very difficult and took a long time. Google Cloud ended up not having what I wanted anyway (multiple translations for a word), so I tried out Microsoft Azure, which did have that option. Azure was still annoying, but much better overall than google, particularly regarding authentication, which was much clearer. 

Overall, I was also happy with the quiz generation, and was pleased that I could get to a point where it took multiple different words (synonyms) as correct.

## Acknowledgments

Loosely following [this tutorial](https://realpython.com/nltk-nlp-python/) on python's NLTK package
Used [this](https://console.cloud.google.com/welcome?project=buoyant-set-376321&walkthrough_id=translation_api_v3_index) tutorial for the Google Translate API