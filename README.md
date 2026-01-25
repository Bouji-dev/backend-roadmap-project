## Week 1 – REST API Fundamentals

### Day 1 – HTTP Methods & Status Codes
**Topics covered:**
- HTTP Methods (GET, POST, PUT, PATCH, DELETE)
- REST API basic principles
- API versioning using `/api/v1`
- HTTP Status Codes: 200, 201, 400, 404, 422

**Implemented endpoints:**
- GET /api/v1/users
- GET /api/v1/users/{user_id}

**Key notes:**
- GET requests must not change server state
- POST requests should return 201 Created
- Use 400 for bad requests and 422 for validation errors
