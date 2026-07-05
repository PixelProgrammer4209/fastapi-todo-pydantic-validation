# Todo CRUD API (with Validation & Error Handling)

An in-memory Todo Management API built with FastAPI, using Pydantic models for request validation and proper HTTP status codes for error handling. Bonus challenges implemented: 
- minimum length check on title
- 422 with custom message for missing required fields

## Setup

```bash
pip install -r requirements.txt
```

## Run

```bash
uvicorn main:app --reload
```

## Usage

| Method | Endpoint              | Description          |
|--------|-----------------------|-----------------------|
| GET    | /todos                | List all todos       |
| GET    | /todos/{id}           | Get a single todo    |
| POST   | /todos                | Create a todo        |
| PUT    | /todos/{id}           | Update a todo        |
| DELETE | /todos/{id}           | Delete a todo        |
| PATCH  | /todos/{id}/complete  | Mark a todo as done  |

## Validation Rules

- `title` — required string, minimum 3 characters
- `checked` — boolean, defaults to `false`
- `priority` — must be `low`, `medium`, or `high`, defaults to `medium`
- `id` — assigned automatically by the server, never sent by the client

## Error Responses

| Status | Meaning                                   |
|--------|--------------------------------------------|
| 201    | Todo created successfully                  |
| 400    | Invalid `priority` value                   |
| 404    | Todo with the given id was not found       |
| 422    | Request body failed validation (bad types, missing/too-short fields) |

