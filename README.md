www contains the web side of the code, if you open index.html, you can see what the web side of the code looks like.

In order to run the backend, simply run command:
    source flask_env/bin/activate
    python run.py
    
tweet_gatherer.py is a script that can run in the background that will search for tweets and add them to our database if they are tagged as sick based on our classifier (contained in corpora)
tweet_gatherer.py calls upon sickness_classifier_defines.py in order to generate the NgramModels and calculate perplexity of the tweets.

In addition, we use tweet_tokenizer.py, which is a function that has been provided by Christopher Potts on the web.

