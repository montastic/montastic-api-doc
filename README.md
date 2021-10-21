[![Services Health](https://mon.montastic.io/badge)](https://mon.montastic.io)

# Montastic API Documentation

The Montastic REST API allows users to perform `CRUD` (Create, Retrieve, Update, Delete)
 operations to the URLs they monitor with Montastic.

Montastic (www.montastic.com) is a web site monitoring service developed by <www.metadot.com>.
It allows webmasters to be recieve notification by SMS or email when their website goes down or if certain conditions are met such as the presence or the absence of a keyword on a HTML page.

## Python Example

A complete example in Python is available at [/examples/python](./examples/python)

## Note for Coders

In this document, and for script reading purpose we use these shell variables:

    YOUR_API_KEY='SECRET_KEY'
    URL='https://montastic.com/checkpoints'
    
## Authentication With API Key

The Montastic user's account `API key` must be used for authentication using a the HTTP header `X-API-KEY`.

User's API key can found in user account page at https://montastic.com/me

Example:

    curl -H "X-API-KEY: $YOUR_API_KEY" -H 'Accept: application/json' $URL

## Requesting JSON format

To request a `JSON` response, the request `HTTP` header `Accept` needs to be
specified as follows: `'Accept: application/json'`

Example:

    curl -H "X-API-KEY: $YOUR_API_KEY" -H 'Accept: application/json' $URL

### Requesting XML Responses (deprecated)

We recommend to use JSON format. However if you need XML here is 
the documentation:

   [Montastic XML API (deprecated)](./deprecated)

## Terminology

In Montastic lingo, a `checkpoint` is a URL Montastic service is monitoring.

## Checkpoint Resource

A checkpoint JSON or XML answer is described as follows:  

- `url`: required
  - URL to monitor. E.g. https://www.daskeyboard.com/
- `name`
  - Human / friendly name of this checkpoint. E.g. 'Das keyboard website home page'.
- `grep_this`
  - Keyword Montastic should look for. E.g. keyboard
- `grep_presence`
  - true (default) | false: if true, Montastic checks the presence of `grep-this` keyword in the monitored URL. If false, Montastic checks that the document does not contain the `grep-this` keyword.
- `check_interval_id`
  - Monitoring interval in minutes. Possible values are 5, 10, 30, 60, 180, 360, 1440.
- `notes`
  - a text field to add some notes. E.g.: "if this site is down: contact Bob"
- ====> *values below this line are read-only*
- `id`
  - id of a checkpoint. Unique id assigned automatically at checkpoint creation time.
- `is_monitoring_enabled`
  - true | false: if true, Montastic monitors the checkpoint on a regular basis based every `check_interval_id`. If false, monitoring is paused and no alerts are sent.
- `status`
  - -1 | 0 | 1: If -1 checkpoint is in alarm (e.g. website down). 1 means all is OK. 0 means transient status.
- `status_changed_on`
  - date of the last status change.
- `badge_token`
  - a UUID for the Montastic status badge

## Creating A Checkpoint

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

## Getting A Checkpoint By id

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

## Deleting A Checkpoint

Endpoint: `DELETE` https://montastic.com/checkpoints/:id

Example:

    curl -X DELETE -H "X-API-KEY: $YOUR_API_KEY" $URL/124

Response:

    Status: 204:No Content

## Getting All Checkpoints

Endpoint: `GET` https://montastic.com/checkpoints

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

## Enable / Disabling Checkpoint Monitoring

Endpoint: `POST` https://montastic.com/checkpoints/:id/enable_monitoring
or
Endpoint: `POST` https://montastic.com/checkpoints/:id/disable_monitoring

    curl  -X PATCH -H "X-API-KEY: $YOUR_API_KEY" http://montastic.com/checkpoints/21/disable_monitoring
or

    curl  -X PATCH -H "X-API-KEY: $YOUR_API_KEY" http://montastic.com/checkpoints/21/enable_monitoring

Response:

    Status: 200:OK
