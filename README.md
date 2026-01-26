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
- Use 400 for bad requests 


### Day 2 – RESTful Design & Validation
**Topics covered:**
- RESTful route design principles
- Proper HTTP method usage for resources
- Request vs Response schemas
- Pydantic validation (EmailStr, Field constraints)
- Business logic errors vs validation errors
- Difference between 400 Bad Request and 422 Validation Error

**Implemented endpoints:**
- POST /api/v1/users
- PUT /api/v1/users/{user_id}

**Key notes:**
- Validation errors (422) are handled automatically by FastAPI/Pydantic
- Business rules should return 400 Bad Request
- Input and output schemas must be separated


### Day 3 – Pagination, Filtering & Query Parameters
**Topics covered:**
- Pagination concepts and importance
- Page-based pagination strategy
- Query parameters validation using FastAPI
- Filtering and sorting via query params
- Difference between validation errors and business logic errors

**Implemented endpoint:**
- GET /api/v1/users

**Key notes:**
- Pagination is mandatory for production-ready APIs
- Offset is calculated using (page - 1) * page_size
- Query parameter validation errors return 422
- Business rule violations return 400
