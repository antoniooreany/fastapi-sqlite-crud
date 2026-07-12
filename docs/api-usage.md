# API Usage

This section shows a few typical request patterns for working with the API.

## Create an access token

```bash
curl -X POST "http://127.0.0.1:8000/token" ^
  -H "Content-Type: application/x-www-form-urlencoded" ^
  -d "username=example&password=secret"
```

## List items

```bash
curl -X GET "http://127.0.0.1:8000/items/" ^
  -H "Authorization: Bearer <access_token>"
```

## Create an item

```bash
curl -X POST "http://127.0.0.1:8000/items/" ^
  -H "Content-Type: application/json" ^
  -H "Authorization: Bearer <access_token>" ^
  -d '{"title":"Example item","description":"Created from API usage example"}'
```

## Suggested usage

For interactive exploration, use Swagger UI at `/docs`. For quick manual verification during development, `curl` examples like the ones above are usually enough.
