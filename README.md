# Mutual Fund API
This is a simple API that provides mutual fund data. It uses RapidAPI to fetch the data.

## Run the API
Make sure you have poetry installed. If not, install it using the following command:
```bash
pip install poetry
```

Then, install the dependencies using the following command:
```bash
poetry install
```

Finally, run the API using the following command:
```bash
poetry run start
```

## Endpoints
### GET /mutual-funds
This endpoint returns a list of mutual funds. You can filter the mutual funds by passing the `scheme_type` query parameter.
```bash
curl --location 'http://localhost:8000/mutual-funds?scheme_type=Open'
```
### POST /register
This endpoint allows you to register a new user. You need to pass the `username` and `password` in the request body.
```bash
curl --location 'http://localhost:8000/register' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username": "john",
    "full_name": "John Doe",
    "password": "John@123",
    "email": "john1@gmail.com"
}'
```
### POST /login
This endpoint allows you to login. You need to pass the `username` and `password` in the request body.

```bash
curl --location 'http://localhost:8000/login' \
--header 'Content-Type: application/json' \
--data-raw '{
    "password": "John@123",
    "email": "john1@gmail.com"
}'
```