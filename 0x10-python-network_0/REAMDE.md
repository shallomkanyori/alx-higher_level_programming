## Python - Network #0

#### Task 0
[0-body_size.sh](0-body_size.sh) is a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
- The size is displayed in bytes
- Uses `curl`

#### Task 1
[1-body.sh](1-body.sh) is a Bash script that takes in a URL, sends a `GET` request to the URL, and displays the body of the response
- Displays only body of a `200` status code response
- Uses `curl`

#### Task 2
[2-delete.sh](2-delete.sh) is a Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response.
- Uses `curl`

#### Task 3
[3-methods.sh](3-methods.sh) is a Bash script that takes in a URL and displays all HTTP methods the server will accept.
- Uses `curl`

#### Task 4
[4-header.sh](4-header.sh) is a Bash script that takes in a URL as an argument, sends a `GET` request to the URL, and displays the body of the response
- Sends a header variable `X-School-User-Id` with the value `98`
- Uses `curl`

#### Task 5
[5-post_params.sh](5-post_params.sh) is a Bash script that takes in a URL, sends a `POST` request to the passed URL, and displays the body of the response
- The variable `email` is sent with the value `test@gmail.com`
- The variable `subject` is sent with the value `I will always be here for PLD`
- Uses `curl`
