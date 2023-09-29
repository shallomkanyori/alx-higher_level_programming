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
