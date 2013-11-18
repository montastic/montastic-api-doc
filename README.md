montastic-api-doc
=================

This is the official Montastic API documentation.

Learn about Montastic at www.montastic.com.


Montastic API allows 3rd party developers to build web and desktop applications which can communicate directly with Montastic. The communication is done by using RESTful HTTPS requests and XML responses.

## Authentication

Each API request requires a basic HTTP authentication, which means the presence of username & password is required.
Example:

    curl -H 'Accept: application/xml' -H 'Content-type: application/xml' -u daniel@metadot.com:123456 https://www.montastic.com/checkpoints/index
    
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

