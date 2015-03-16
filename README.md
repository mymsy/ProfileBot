# ProfileBot
A tool for randomly changing words in a Twitter profile.

Apart from your Twitter account, you will need:
* Application access tokens from [apps.twitter.com](apps.twitter.com).
Directions for generating them are given at the end of this file.
* Python (tested with 2.7.9)
* [Tweepy](http://www.tweepy.org/), a Python library for Twitter

## Usage 
Basic use case is running periodically via cron and 
`updateprof.sh`. Enter your access tokens, profile text, and potential 
word replacements into `updateprof.sh`, run `crontab -e` to edit 
your cron file, and add a line like (with `/home/user/` changed to whichever
directory hosts ProfileBot)


```
0 0 * * * cd /home/user/ProfileBot; bash updateprof.sh >>error.log 2>&1
```

This will run the script once a day, at midnight, with all output and
errors written to `/home/user/ProfileBot/error.log`

Alternately, you can run the Python script directly

```
python profilebot.py --consumer_key <CK> \
                     --consumer_secret <CS> \
                     --access_token <AT> \
                     --access_token_secret <ATS> \
                     --profile "This is a ADJECTIVE message!" \
                     --replace "ADJECTIVE" \
                     --with "profile" "ridiculous" "silly" "annoying"
```

with the same substitutions as in the shell script.

## Obtaining Access Tokens
Twitter requires four access tokens for an application to autonomously 
update your profile, which you will need to generate:
* Log in to Twitter with the account you want the script to affect.
* Open [Twitter Application Management](apps.twitter.com).
* Click the 'Create New App' button and fill out the form. Callback URL 
doesn't matter.
* Switch to the 'Permissions' tab, select 'Read and Write', and click 
'Update Settings'. This allows the script to write to your profile.
* Switch to the 'Keys and Access Tokens' tab. Your consumer key and consumer 
secret will already be available and are listed near the top. 
* Click the 'Create my access token' button to create your access token and
access token secret.
