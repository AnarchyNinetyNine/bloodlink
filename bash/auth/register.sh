#!/bin/bash
# POST request to register user

if [ $# -ne 5 ]; then
  echo "Usage: <script> <name> <role> <phone_number> <email> <password>"
  exit 1
fi

curl -X POST http://localhost:5001/api/v1/auth/hospital/register \
-H "Content-Type: application/json" \
-d "{\"name\": \"$1\", \"role\": \"$2\", \"email\": \"$3\", \"phone_number\": \"$4\", \"password\": \"$5\"}"
