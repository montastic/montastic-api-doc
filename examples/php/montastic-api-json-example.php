<?php
// 
// This PHP script fetches a JSON array of URLs monitored by Montastic
//

// Make sure cURL for PHP is installed.
// Init cURL
$curl = curl_init();

// Set URL
curl_setopt($curl, CURLOPT_URL, "https://www.montastic.com/checkpoints");

// Get is set as default so no need to set it
// curl_setopt($curl, CURLOPT_CUSTOMREQUEST, "GET");

// Set email and password
curl_setopt($curl, CURLOPT_USERPWD, "bob@marley.com:reggaerules");

// Ask cURL to return the result as a string
curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);

// Add a http header to enable JSON response
$headers = array("Accept: application/json");
curl_setopt($curl, CURLOPT_HTTPHEADER, $headers);

// Fetch data and decode JSON response into an array
$response = json_decode(curl_exec($curl), true);

// Check for error
$httpcode = curl_getinfo($curl, CURLINFO_HTTP_CODE);
if ($httpcode == 401) {
    printf("Authentication error: %s\n", $httpcode);
    exit(-1);
} else if ($httpcode != 200){
    # Other error
    printf("API call error HTTP code: %s\n", $httpcode);
    exit(-1);
}

#
# All OK, let's display the result
#
 
# TO DEBUG: use var_dump to see all data
# var_dump($response);

foreach ($response as $checkpoint) {
    if ($checkpoint['status'] == 1) {
        print "OK   ";
    } else if ($checkpoint['status'] == -1){
        print "DOWN ";
    } else {
        print "UNKNOWN STATUS ";
    }
    
    printf("%s\n", $checkpoint['url']);
}

// ==> OUTPUT
//DOWN http://www.borkensite.com
//OK   http://www.metadot.com
//OK   http://www.mysite.com/apage.html
//OK   http://www.daskeyboard.com/
//OK   https://app.myawesomeapp.com/

?>