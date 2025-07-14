
# perennial fastapi

Implement search api for the employee search directory.

important points:
1. Documentation: design and installation document is present there for to dive into more deep: documents/design_and_installtion.md
2. Documentation: some of the FAQs asked for AI tool and processes is present inside documents/FAQs.text
3. intial setup, apis, and testcase are defined. please refer setup and installation steps(mentioned below)

**setup and Installation**
1. Clone the Repository
   ```bash
   git clone https://github.com/rathorharish07/perennial-fastapi
   cd perennial-fastapi

2. Build and Start the Containers
   ```bash
   docker-compose up -d --build
   
3. Access the Application
   ```bash
    FastAPI application: http://localhost:8000/health-check
    Swagger UI: http://localhost:8000/docs
    ReDoc: http://localhost:8000/redoc
    Openapi json: http://localhost:8000/openapi.json

4. At http://0.0.0.0:8000/v1/employee/search you will have the **search api** with all possible filter or check on swagger UI for better visualization(http://localhost:8000/docs)

5. To execute the test suite within the containerized environment:
   ```bash
    docker-compose run --rm web pytest -v

6. Stop and Remove Containers
   ```bash
    docker-compose down

**Note**

    1. Dockerfile and docker-compose.yml define your container environment.
    2. main.py initializes FastAPI, includes routers, and sets up Redis rate limiter.
    3. requirements.txt lists Python dependencies.
    4. .dockerignore excludes files from the Docker build context.
    5. test cases and api rate limiting is implemented
