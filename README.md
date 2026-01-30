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


### Day 4 – Global Error Handling & Custom Exceptions

**Topics covered:**
- Global error handling in FastAPI
- Designing and using custom application exceptions
- Standardizing API error response format
- Separating business errors from HTTP layer concerns

**Implemented endpoints / components:**
- Base custom exception class
- NotFoundException
- Global exception handler
- Unified API error response schema

**Key notes:**
- Centralized error handling improves maintainability and readability
- Business logic should not raise HTTPException directly
- Consistent error responses simplify frontend error handling


### Day 5 – Service Layer & Dependency Injection

**Topics covered:**
- Service layer concept in backend architecture
- Separating business logic from API endpoints
- Dependency Injection using FastAPI Depends
- Refactoring endpoints for better testability

**Implemented endpoints / components:**
- UserService
- Dependency provider (get_user_service)
- Refactored user endpoint using service layer

**Key notes:**
- Service layer is framework-independent and reusable
- Dependency injection makes unit testing and mocking easier
- Existing endpoints were refactored instead of duplicated


### Day 6: Testing FastAPI with pytest

**Topics Covered:**
- Introduction to API testing in FastAPI
- Using pytest as a test runner
- FastAPI TestClient and its dependency on httpx
- Writing a basic API test for a GET endpoint
- Understanding test failures (404 vs 200)
- Running tests inside a virtual environment

**What Was Implemented:**
- Created the first API test for the users endpoint
- Used FastAPI TestClient to simulate HTTP requests
- Executed tests using `python -m pytest`
- Installed missing testing dependencies (pytest, httpx)
- Analyzed a failing test and understood why it fails

**Key Learnings:**
- TestClient relies on Starlette and httpx internally
- Tests must be executed with the same Python interpreter as the venv
- A failing test is valuable feedback, not an error
- 404 responses usually indicate routing or prefix issues

**How to Run Tests:**
- python -m pytest


### Day 7: Weekly Review and Refactoring Mindset

**Topics Covered:**
- Reviewing the project structure after one week
- Understanding test failures and debugging strategies
- Refactoring mindset vs adding new features
- Importance of service layer and dependency injection
- Interview-oriented thinking for backend developers

**What Was Reviewed:**
- FastAPI routing and prefixes
- Service and dependency separation
- API testing strategy
- Test failure analysis (404 vs 200)

**Key Learnings:**
- A clean architecture makes debugging easier
- Tests help validate behavior, not just correctness
- Dependency injection enables proper mocking
- Backend development is about long-term maintainability


## Week 2: PostgreSQL + SQLAlchemy (Real Production Setup)

### Day 1: PostgreSQL and SQLAlchemy Fundamentals

**Topics Covered:**
- Introduction to databases in backend systems
- PostgreSQL overview and production use cases
- ORM concept and why SQLAlchemy is used
- Core SQLAlchemy concepts (Engine, Session, Model)

**Implementation:**
- Initialized database module structure
- Created SQLAlchemy Declarative Base
- Configured database engine and session factory
- Defined initial User database model

**Key notes:**
- Databases provide persistent storage
- PostgreSQL is a production-ready relational database
- SQLAlchemy abstracts SQL into Python objects
- Engine manages database connections
- Session represents a transactional unit of work


### Day 2: SQLAlchemy Session Lifecycle + FastAPI Dependency Injection

**Topics**
- SQLAlchemy session concept and responsibilities
- Database session lifecycle
- Common mistakes with global sessions
- Dependency Injection in FastAPI
- Using yield-based dependencies for cleanup

**Implementation**
- Extended database session configuration
- Implemented get_db dependency with proper lifecycle handling
- Injected database session into API routes using Depends
- Prepared API routes for future database operations

**Key Points**
- Sessions must be short-lived and request-scoped
- Global sessions can cause concurrency and memory issues
- FastAPI manages dependency lifecycles automatically
- Using yield ensures proper cleanup after each request
- Dependency injection improves testability and decoupling
