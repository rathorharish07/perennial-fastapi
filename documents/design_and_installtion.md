**perennial-fastapi**:
    It is a clean, modular FastAPI application using Redis and Docker Compose, designed for high performance, maintainability, and ease of development.

**Architecture & Directory Structure**

        test_assi/
        ├── apps/
           ├── employeee/    # employeee related router and views like search endpoint
        ├── config/           # configured settings.py etc
        ├── main.py           # FastAPI app setup, includes routers, DI
        ├── database.py       # database setup
        ├── conftest.py       # test cases related fixture and setup  
        ├── Dockerfile        # Defines image build
        ├── docker-compose.yml# Orchestrates services: web + Redis
        ├── requirements.txt  # Python dependencies
        └── .dockerignore     # Excludes development artifacts

**Key Components:**

    1. FastAPI + Pydantic
        * FastAPI uses Python’s async/await, type hints, and Pydantic for validation.
        * Pydantic models ensures data types are enforced, and OpenAPI schemas are auto-generated for interactive documentation (Swagger UI, ReDoc) 

    2. Dependency Injection
        * Dependencies like get_db and Redis client are injected using FastAPI’s Depends, enabling modularity and ease of testing.
        * Modular design keeps route handlers focused, with business logic and data access handled separately.

    3. Docker & Docker Compose
        * Dockerfile uses python:3.13-slim with layered installations,optimized caching etc.
        * docker-compose.yml sets up Redis and Live-reloading FastAPI service (uvicorn --reload), enabling rapid development workflows.
        * Redis is containerized with health checks, and the web service depends on Redis readiness.
    4. database
        * Intially I have used default sqlite database but we can configure and use other more reliable database like postgres, mysql and mongodb etc.
    5. Testcase
        * testcase is implemented as per the TDD approach using pytest module.

**Rate limiting**

    An appropriate rate-limiting system as possible to prevent the user from spamming the API using fastapi_limiter module.

**Testing Strategy**

    * Tests use pytest and pytest-asyncio with an in-memory SQLite database.
    * httpx.AsyncClient with ASGITransport manager ensures full route coverage, including startup/shutdown logic.
    * Tests reside alongside modules (e.g., apps/employees/tests), mirroring project structure and making CI integration straightforward.

**Config & Environment**

    * Configuration is managed via Pydantic BaseSettings, with type-safe fields for DEBUG, REDIS_HOST, and REDIS_PORT.
    * .env file support allows seamless switching between environments.
    * .dockerignore excludes sensitive or unnecessary files like .env, test.db, .egg-info, keeping Docker builds clean.

**Summary**

    The architecture adopts clean design principles and modern tooling:
        1. Modular routers and services enable scalable, maintainable growth.
        2. Dependency injection with testable, isolated units simplifies testing and reuse.
        3. Docker setup is optimized for dev and production readiness.
        4. Pydantic + FastAPI offers type safety, validation, and auto-documentation.
        5. Comprehensive testing fosters confidence and continuous integration compatibility.


