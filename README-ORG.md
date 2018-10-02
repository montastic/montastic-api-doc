# Montastic API Documentation

Montastic (www.montastic.com) is a web site monitoring service developed by Metadot. 
It allows web masters to be alerted if their website goes down or if certain conditions are met such as the presence or the absence of a keyword. This document describes its public API.

## About Montastic API

Montastic API is easy to use. It allows 3rd party developers to build web, desktop, and server applications or simple scripts that can communicate with the Montastic service. The communication is done by using `RESTful` `HTTPS` requests and `JSON` or `XML` responses. The use of `JSON` format is recommended.

## Authentication With API Key

A Montastic user account API key must be used for authentication using a special header `X-API-KEY`. Example:

    curl -H "X-API-KEY: YOUR-API-KEY" -H 'Accept: application/json' https://www.montastic.com/checkpoints/index
    
## XML or JSON Response?

The request `HTTP` header `Accept` will determine the format Montastic will use for the response. `JSON` format is recommended.

### To get JSON responses (Recommended)

    curl -H "X-API-KEY: YOUR-API-KEY" -H 'Accept: application/json' https://www.montastic.com/checkpoints/index

### To get XML Responses

    curl -H "X-API-KEY: YOUR-API-KEY" -H 'Accept: application/xml' https://www.montastic.com/checkpoints/index

## Terminology

In Montastic lingo, a `checkpoint` is a URL Montastic service is monitoring.

## Creating a New Checkpoint in XML

    curl -H 'Accept: application/xml' -H 'Content-type: application/xml' -H "X-API-KEY: YOUR-API-KEY"  https://www.montastic.com/checkpoints/create -d '<checkpoint><url>http://ww3.test3.com</url></checkpoint>' -X POST
    
Response:

    Status: OK
    <?xml version="1.0" encoding="UTF-8"?>
    <checkpoint>
      <check-interval-id type="integer">5</check-interval-id>
      <id type="integer">9830</id>
      <is-monitoring-enabled type="boolean">true</is-monitoring-enabled>
      <name>Login Page</name>
      <status type="integer">1</status>
      <status-changed-on type="datetime">2009-10-30T13:42:50-06:00</status-changed-on>
      <url>http://ww3.test3.com</url>
    </checkpoint>
    

## Retrieving a Checkpoint  

JSON

    curl -H 'Accept: application/json' -H "X-API-KEY: YOUR-API-KEY" https://www.montastic.com/checkpoints/show/9795

XML

    curl -H 'Accept: application/xml' -H "X-API-KEY: YOUR-API-KEY" https://www.montastic.com/checkpoints/show/9795
   
Response:

    Status: OK
    <?xml version="1.0" encoding="UTF-8"?>
    <checkpoint>
      <check-interval-id type="integer">3</check-interval-id>
      <grep-this>Login</grepthis>
      <grep-presence>true</grep-presence>
      <id type="integer">9795</id>
      <is-monitoring-enabled type="boolean">true</is-monitoring-enabled>
      <name>Login page</name>
      <status type="integer">1</status>
      <status-changed-on type="datetime">2008-12-29T17:54:18-06:00</status-changed-on>
      <url>http://www.google.com/</url>
    </checkpoint>
    
## Deleting a Checkpoint

    curl -X DELETE -H "X-API-KEY: YOUR-API-KEY" https://www.montastic.com/checkpoints/destroy/156423 
    
Response:

    Status: OK
    
## Getting a List of Checkpoints

    curl -H "X-API-KEY: YOUR-API-KEY" -H 'Accept: application/xml' https://www.montastic.com/checkpoints/index
    
Response:

     Status: OK
     <?xml version="1.0" encoding="UTF-8"?>
     <checkpoints type="array">
       <checkpoint>
         <check-interval-id type="integer">5</check-interval-id>
         <id type="integer">9795</id>
         <is-monitoring-enabled type="boolean">true</is-monitoring-enabled>
         <name></name>
         <status type="integer">1</status>
         <status-changed-on type="datetime">2008-12-29T17:54:18-06:00</status-changed-on>
         <url>http://www.mojohelpdesk.com/</url>
       </checkpoint>
       <checkpoint>
         <check-interval-id type="integer">30</check-interval-id>
         <id type="integer">9794</id>
         <is-monitoring-enabled type="boolean">true</is-monitoring-enabled>
         <name></name>
         <status type="integer">-1</status>
         <status-changed-on type="datetime">2008-06-20T22:07:20-05:00</status-changed-on>
         <url>http://www.metadot.com/s</url>
       </checkpoint>
       <checkpoint>
         <check-interval-id type="integer">30</check-interval-id>
         <id type="integer">9793</id>
         <is-monitoring-enabled type="boolean">true</is-monitoring-enabled>
         <name></name>
         <status type="integer">1</status>
         <status-changed-on type="datetime">2009-01-09T14:01:26-06:00</status-changed-on>
         <url>http://www.metadot.com/</url>
       </checkpoint>
     </checkpoints>

## Updating a Checkpoint  

    curl  -X POST -H "X-API-KEY: YOUR-API-KEY" -H 'Accept: application/xml' -H 'Content-type: application/xml' -d '<checkpoint><name>Montastic.com production</name></checkpoint>' http://www.montastic.com/checkpoints/update/21
    
Response:

    Status: OK
    
## Checkpoint Fields Explanation  
 
 - `url`
  - URL to monitor. E.g. http://www.daskeyboard.com/ or https://bob:secret@login.tesla.com:8080/login
 - `name`
  - Human / friendly name of this checkpoint. E.g. 'Website login page'.
 - `grep-this`
  - Keyword Montastic should look for. E.g. keyboard
 - `grep-presence`
  - true (default) | false: if true, Montastic checks the presence of `grep-this` keyword. If false, Montastic checks that the document does not contain the `grep-this` keyword.
 - `id`
  - id of a checkpoint. This is a unique id assigned automatically at checkpoint creation time.
 - `is-monitoring-enabled`
  - true | false: if true, Montastic monitors the checkpoint on a regular basis. If false, checkpoint is not monitored.
 - `status`
  - -1 | 0 | 1: If -1 checkpoint is in alarm (e.g. website down). 1 means all is OK. 0 means unknown status.
 - `status-changed-on`
  - Date of the last status change.
 - `check-interval-id`
  - Monitoring interval in minutes. Possible values are 5, 10, 30, 60, 180, 360, 1440.
 
