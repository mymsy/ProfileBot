#!/bin/bash

python profilebot.py --consumer_key CK \
					 --consumer_secret CS \
                     --access_token AT \
                     --access_token_secret ATS \
                     --profile "I'm a profile bot!" \
                     --replace "profile" \
                     --with "profile" "ridiculous" "silly" "ebooks" "annoying"
