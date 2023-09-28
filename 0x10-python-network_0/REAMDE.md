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

#### Task 6
[6-peak.py](6-peak.py) contains a Python function that finds a peak in a list of unsorted integers.
- Prototype: `def find_peak(list_of_integers):`
- Does not import any module
- The algorithm has the lowest complexity
- There may be more than one peak

[6-peak.txt](6-peak.txt) contains the complexity of the algorithm: `O(log(n))`, `O(n)`, `O(nlog(n))` or `O(n2)`


#### Task 7
[100-status_code.sh](100-status_code.sh) is a Bash script that sends a request to a URL passed as an argument, and displays only the status code of the response.
- Does not use any pipe, redirection, etc.
- Does not use `;` and `&&`
- Uses `curl`

#### Task 8
[101-post_json.sh](101-post_json.sh) is a Bash script that sends a JSON `POST` request to a URL passed as the first argument, and displays the body of the response.
- Sends a `POST` request with the contents of a file, passed with the filename as the second argument of the script, in the body of the request
- Uses `curl`
