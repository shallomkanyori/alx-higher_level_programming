## Python - Network #1

#### Task 0
[0-hbtn_status.py](0-hbtn_status.py) is a Python script that fetches `https://alx-intranet.hbtn.io/status`
- Uses the package `urllib` only
- The body of the response is displayed formatted
- Uses a `with` statement

#### Task 1
[1-hbtn_header.py](1-hbtn_header.py) is a Python script that takes in a URL, sends a request to the URL and displays the value of the `X-Request-Id` variable found in the header of the response.
- Uses the packages `urllib` and `sys` only
- The value of this variable is different for each request
- Does not check arguments passed (number or type)
- Uses a `with` statement

#### Task 2
[2-post_email.py](2-post_email.py) is  a Python script that takes in a URL and an email, sends a `POST` request to the passed URL with the email as a parameter, and displays the body of the response (decoded in `utf-8`)
- The email is sent in the `email` variable
- Uses the packages `urllib` and `sys` only
- Does not check arguments passed (number or type)
- Uses a `with` statement

#### Task 3
[3-error_code.py](3-error_code.py) is a Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in `utf-8`).
- Manages `urllib.error.HTTPError` exceptions and prints: `Error code: ` followed by the HTTP status code
- Uses the packages `urllib` and `sys` only
- Does not check arguments passed (number or type)
- Uses a `with` statement

#### Task 4
[4-hbtn_status.py](4-hbtn_status.py) is a Python script that fetches `https://alx-intranet.hbtn.io/status`
- Uses the package `requests` only
- The body of the response is displayed formatted

#### Task 5
[5-hbtn_header.py](5-hbtn_header.py) is a Python script that takes in a URL, sends a request to the URL and displays the value of the `X-Request-Id` varible in the response header.
- Uses the packages `requests` and `sys` only
- The value of this variable is different for each request
- Does not check arguments passed (number or type)

#### Task 6
[6-post_email.py](6-post_email.py) is  a Python script that takes in a URL and an email, sends a `POST` request to the passed URL with the email as a parameter, and displays the body of the response.
- The email is sent in the `email` variable
- Uses the packages `requests` and `sys` only
- Does not check arguments passed (number or type)

#### Task 7
[7-error_code.py](7-error_code.py) is a Python script that takes in a URL, sends a request to the URL and displays the body of the response.
- If the HTTP status code is greater than or equal to 400, prints: `Error code: ` followed by the HTTP status code
- Uses the packages `requests` and `sys` only
- Does not check arguments passed (number or type)

#### Task 8
[8-json_api.py](8-json_api.py) is a Python script that takes in a letter and sends a `POST` request to `http://0.0.0.0:5000/search_user` with the letter as a parameter.
- The letter is sent in the variable `q`
- If no argument is given, sets `q=""`
- If the response body is properly JSON formatted and not empty, displays the `id` and `name` as: `[<id>] <name>`
- Otherwise:
	- Displays `Not a valid JSON` if the JSON is invalid
	- Displays `No result` if the JSON is empty
- Uses the packages `requests` and `sys` only

#### Task 9
[10-my_github.py](10-my_github.py) is a Python script that takes a user's GitHub credentials (username and password) and uses the GitHub API to display their `id`.
- Uses Basic Authentication with a personal access token as password to access to the user's information (only `read:user` permission is needed)
- The first argument is the user's `username`
- The second argument is the user's `password`/PAT
- Uses the packages `requests` and `sys` only
- Does not check arguments passed (number or type)


#### Task 10
[100-github_commits.py](100-github_commits.py) is a Python script that takes 2 arguments in order to solve the following challenge: List 10 commits (from the most recent to oldest) of a repository using the GitHub API. Print the commits as: `<sha>: <author name>` (one per line)
- The first argument is the `repository name`
- The second argument is the `owner name`
- Uses the packages `requests` and `sys` only
- Does not check arguments passed (number or type)
