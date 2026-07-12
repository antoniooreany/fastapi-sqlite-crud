# Authentication

The project uses JWT-based authentication to protect selected API routes.

## Authentication flow

1. A user submits credentials to the login endpoint.
2. The application verifies the credentials.
3. If authentication succeeds, the server returns a JWT access token.
4. The client sends the token in the `Authorization: Bearer <token>` header.
5. Protected endpoints validate the token before granting access.

## Typical login request

```http
POST /token
Content-Type: application/x-www-form-urlencoded

username=example&password=secret
```

## Typical authenticated request

```http
GET /items/
Authorization: Bearer <access_token>
```

## Notes

- Passwords should be stored as hashes, not plain text.
- Tokens should only be issued after successful credential verification.
- Protected endpoints should reject missing, invalid, or expired tokens.
