# Montastic API Documentation

Montastic (www.montastic.com) is a web site monitoring service developed by Metadot. It allows web masters to be alerted if their website goes down or in case certain conditions are met. This document describe its public API.


## About Montastic API

Montastic API is simplistic and very easy to use. Montastic API allows 3rd party developers to build web, desktop, and server applications or simple scripts that can communicate directly with the Montastic service. The communication is done by using `RESTful HTTPS` requests and `XML` responses. 

 - Learn about Montastic at www.montastic.com.

## Authentication

Each API request requires a basic HTTP authentication, which means the presence of username & password is required.

Example:

    curl -H 'Accept: application/xml' -H 'Content-type: application/xml' -u daniel@metadot.com:123456 https://www.montastic.com/checkpoints/index

### Terminology

In Montastic lingo, a `checkpoint` is a URL Montastic service is monitoring.

### Getting a Checkpoint Record  

    curl -H 'Accept: application/xml' -H 'Content-type: application/xml' -u daniel@metadot.com:123456 https://www.montastic.com/checkpoints/show/9795

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

## Creating a New Checkpoint  

    curl -H 'Accept: application/xml' -H 'Content-type: application/xml'  -u billy@example.com:123456 https://www.montastic.com/checkpoints/create -d '<checkpoint><url>http://ww3.test3.com</url></checkpoint>' -X POST
    
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
    
    
## Deleting a Checkpoint

    curl -H 'Accept: application/xml' -H 'Content-type: application/xml'  -u daniel@metadot.com:123456 https://www.montastic.com/checkpoints/destroy/156423 -X DELETE
    
Response:

    Status: OK
    
### Getting a List of Checkpoints

    curl -H 'Accept: application/xml' -H 'Content-type: application/xml' -u daniel@metadot.com:123456 https://www.montastic.com/checkpoints/index
    
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

    curl -H 'Accept: application/xml' -H 'Content-type: application/xml'  -u daniel@metadot.com:123456 http://www.montastic.com/checkpoints/update/21 -d '<checkpoint><name>Montastic.com production</name></checkpoint>' -X POST
    
Response:

    Status: OK
    

## Checkpoint Fields Explanation  
 
 - url
  - URL to monitor. E.g. http://www.daskeyboard.com/ or https://bob:secret@login.ibm.com:8080/login
 - name
  - Human / friendly name of this checkpoint. E.g. 'Website login page'.
 - grep-this
  - Keyword Montastic should check for. E.g. keyboard
 - grep-presence
  - true (default) | false: if true, Montastic checks the presence of <grep-this> keyword. If false, Montastic checks that the document does not contain the <grep-this> keyword.
 - id
  - id of a checkpoint. This is unique number assigned automatically at checkpoint creation time.
 - is-monitoring-enabled
  - true | false: if true, Montastic monitors the checkpoint on a regular basis set by check-interval-id. If false, checkpoint is not monitored.
 - status
  - -1 | 0 | 1: If -1 checkpoint is faulty. 1 means all is OK. 0 means unknown status.
 - status-changed-on
  - Date of the last status change.
 - check-interval-id
  - Monitoring interval in minutes. Possible values are 5, 10, 30, 60, 180, 360, 1440.
 
