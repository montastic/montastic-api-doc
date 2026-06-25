[![Services Health](https://mon.montastic.io/badge)](https://mon.montastic.io)

# Montastic API Documentation

The Montastic REST API allows users to perform `CRUD` (Create, Retrieve, Update, Delete)
 operations to the URLs they monitor with Montastic.

Full Montastic API doc is located here: <https://montastic.com/developers> 

Montastic (www.montastic.com) is a web site monitoring service developed by <www.metadot.com>.
It allows webmasters to be receive notifications by SMS or email when their website goes down or if certain conditions are met such as the presence or the absence of a word on a HTML page.

    
## Authentication With API Key

The Montastic user's account `API key` must be used for authentication using a the HTTP header `X-API-KEY`.

User's API key can found in user account page at https://montastic.com/me


## Python Example

An example in Python is available at [/examples/python](./examples/python)
