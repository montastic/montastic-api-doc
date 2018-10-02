# Montastic API Documentation

Montastic (www.montastic.com) is a web site monitoring service developed by Metadot.
It allows webmasters to be alerted if their website goes down or if certain conditions
 are met such as the presence or the absence of a keyword on a HTML page.

## Python Example

A complete example in Python is available at [/examples/python](./examples/python)

## Authentication With API Key

The Montastic user's account `API key` must be used for authentication using a special header `X-API-KEY`.

api key found in user account page at www.montastic.com

Example:

    curl -H "X-API-KEY: $YOUR_API_KEY" -H 'Accept: application/json' $URL

## Requesting JSON format

To request a `JSON` response, the request `HTTP` header `Accept` needs to be
specified as follows: `'Accept: application/json'`

Example:

    curl -H "X-API-KEY: $YOUR_API_KEY" -H 'Accept: application/json' $URL

### Requesting XML Responses (deprecated)

    This document describes Montastic API using XML format
    ================= LINK TODO

## Terminology

In Montastic lingo, a `checkpoint` is a URL Montastic service is monitoring.

## Note for Coders

In this document, and for script reading purpose we use these shell variables:
    
    YOUR_API_KEY='SECRET_KEY'
    URL='https://montastic.com/checkpoints'

## Checkpoint Resource

A checkpoint is described as follows:  

- `url`: required
 - URL to monitor. E.g. https://www.daskeyboard.com/
- `name`
 - Human / friendly name of this checkpoint. E.g. 'Website login page'.
- `grep_this`
  - Keyword Montastic should look for. E.g. keyboard
- `grep_presence`
  - true (default) | false: if true, Montastic checks the presence of `grep-this` keyword. If false, Montastic checks that the document does not contain the `grep-this` keyword.
- `id`
  - id of a checkpoint. Unique id assigned automatically at checkpoint creation time.
- `is_monitoring_enabled`
  - true | false: if true, Montastic monitors the checkpoint on a regular basis based on `check_interval_id`. If false, monitoring is paused.
- `status`
  - -1 | 0 | 1: If -1 checkpoint is in alarm (e.g. website down). 1 means all is OK. 0 means transient status.
- `status_changed_on`
  - Date of the last status change.
- `check_interval_id`
  - Monitoring interval in minutes. Possible values are 5, 10, 30, 60, 180, 360, 1440.


## Creating a Checkpoint

Endpoint: `POST` https://montastic.com/checkpoints

Example:

    curl -H 'Accept: application/json' -H 'Content-type: application/json' -H "X-API-KEY: $YOUR_API_KEY"  $URL -d '{"url": "https://www.daskeyboard.com/"}' -X POST

Response:

    Status: 201:CREATED

````JSON
{
  "id": 124,
  "url": "https://www.daskeyboard.com/",
  "name": "",
  "status": 1,
  "status_changed_on": "2018-10-02T16:42:21.000Z",
  "check_result_code": "0",
  "is_monitoring_enabled": true,
  "check_interval_id": 360,
  "grep_this": null,
  "grep_presence": true,
  "notes": null
}
````

## Getting a Checkpoint by id

Endpoint: `GET` https://montastic.com/checkpoints/:id

Example:

    curl -H 'Accept: application/json' -H "X-API-KEY: $YOUR_API_KEY" $URL/124

Response:

    Status: 200:OK

````JSON
{
  "id": 124,
  "url": "https://www.daskeyboard.com/",
  "name": "",
  "status": 1,
  "status_changed_on": "2018-10-02T16:42:21.000Z",
  "check_result_code": "0",
  "is_monitoring_enabled": true,
  "check_interval_id": 360,
  "grep_this": null,
  "grep_presence": true,
  "notes": null,
  "badge_token": "c28343443dfqal"
}
````

## Deleting a Checkpoint

Endpoint: `DELETE` https://montastic.com/checkpoints/:id

Example:

    curl -X DELETE -H "X-API-KEY: $YOUR_API_KEY" $URL/124

Response:

    Status: 204:No Content

## Getting All Checkpoints

Endpoint: GET https://montastic.com/checkpoints

Example:

    curl -H "X-API-KEY: $YOUR_API_KEY" -H 'Accept: application/json' $URL

Response:

     Status: 200:OK

````JSON
[
  {
    "id": 121,
    "url": "https://www.daskeyboard.com/",
    "status": 1,
    "name": "",
    "status_changed_on": "2018-10-02T16:32:57.000Z",
    "check_result_code": "0",
    "is_monitoring_enabled": true,
    "check_interval_id": 360,
    "time_between_last_two_checks": 0,
    "grep_this": "logitech",
    "notes": null,
    "grep_presence": false,
    "badge_token": "608c85348c2fa9c9b3fb8a6a28f64d645447ecd5"
  }
]
````

## Updating a Checkpoint

Endpoint: `PATCH` https://montastic.com/checkpoints/:id

    curl  -X PATCH -H "X-API-KEY: $YOUR_API_KEY" -H 'Accept: application/json' -H 'Content-type: application/json' -d '{"name": "Website production"}' http://montastic.com/checkpoints/21

Response:

    Status: 200:OK

