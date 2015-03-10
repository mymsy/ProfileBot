"""A bot for changing pronouns in a twitter profile.

Imagined use case is running once a day via cron and a shell script
(updateprof.sh is provided with the repository)

0 0 * * * cd /home/user/profilebot; bash updateprof.sh >>error.log 2>&1
"""

import tweepy
import random

class ProfileBot:
    """A bot for changing pronouns in a twitter profile"""

    def __init__(self, consumer_key, consumer_secret, access_token,
                 access_token_secret):
        """Initialise the bot with twitter api auth tokens

        Arguments (all values from apps.twitter.com):
        consumer_key - Twitter consumer key
        consumer_secret - Twitter consumer secret
        access_token - Twitter app access token
        access_token_secret - Twitter app access token secret

        Postcondition: 
        An api access object is created using the access tokens
        """
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        self.api = tweepy.API(auth)

    def newprofile(self, profile, oldword, wordlist):
        """Update profile text with a random wordlist

        Arguments:
        profile - string with the base profile text
        oldword - string with the word to be replaced
        wordlist - List of potential replacement strings, 
                   one will be chosen at random

        Postcondition:
        Twitter profile has been changed to the new string with
        randomly chosen replacement word. Currently unable to
        determine success or failure - this is missing from tweepy
        documentation.
        """

        # pick a word at random from the word list and replace
        newword = wordlist[random.randrange(len(wordlist))]
        profile = profile.replace(oldword, newword)

        # update profile
        self.api.update_profile(description=profile)


if __name__ == '__main__':
    import argparse

    # use the first line of the doc string as the program description
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--consumer_key", required=True,
                        help="Twitter consumer key")
    parser.add_argument("--consumer_secret", required=True,
                        help="Twitter consumer secret")
    parser.add_argument("--access_token", required=True,
                        help="Twitter app access token")
    parser.add_argument("--access_token_secret", required=True,
                        help="Twitter app access token secret")
    parser.add_argument("--profile", required=True,
                        help="Base profile string, for substitution")
    parser.add_argument("--replace", default="WORD", 
                        help="Word to be replaced")
    parser.add_argument("--with", dest="wordlist", nargs="+", required=True,
                        help="List of possible replacements")

    args = parser.parse_args()

    # create the bot (initialising the auth method)
    bot = ProfileBot(args.consumer_key, args.consumer_secret, 
                     args.access_token, args.access_token_secret)
    
    # update the profile
    bot.newprofile(args.profile, args.replace, args.wordlist)
