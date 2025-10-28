# ML Model Deployment with FastAPI & Docker

This repository demonstrates a production-ready workflow for deploying machine learning models as REST APIs using FastAPI and Docker. It showcases best practices for ML model serving, API development, and containerization.

## Project Overview

This project implements a machine learning service that predicts Titanic passenger survival probability. It demonstrates:

- **Production-Grade API Development**: Using FastAPI for high-performance, async-capable API endpoints
- **ML Model Serving**: Efficiently serving predictions from a pre-trained Titanic survival prediction model
- **Containerization**: Docker-based deployment for consistent environments and easy scaling
- **API Documentation**: Auto-generated interactive API documentation with OpenAPI/Swagger
- **Error Handling**: Robust error handling and input validation using Pydantic schemas
- **CORS Support**: Configured Cross-Origin Resource Sharing for web client access
- **Health Checks**: API health monitoring endpoint with version tracking

## Project Structure
```
├── Dockerfile              # Docker configuration file
├── README.md              # Project documentation
└── titanic_model_api/     # Main application directory
    ├── requirements.txt   # Python dependencies
    ├── titanic_model-0.0.1-py3-none-any.whl  # Packaged ML model
    └── app/              # FastAPI application
        ├── __init__.py
        ├── api.py        # API route definitions
        ├── config.py     # Configuration settings
        ├── main.py      # FastAPI app initialization
        └── schemas/      # Pydantic models/schemas
            ├── __init__.py
            ├── health.py # Health check schemas
            └── predict.py # Prediction request/response schemas
```

Modern ML DevOps: Scalable, cloud-ready ML service for real-time inference

Interactive API docs: Built-in Swagger/OpenAPI support

## Technical Details

### API Endpoints

1. **Health Check** (`GET /api/v1/health`)
   - Monitors API health status
   - Returns API and model versions
   - Useful for deployment monitoring

2. **Prediction** (`POST /api/v1/predict`)
   - Accepts passenger features in JSON format
   - Returns survival prediction and probability
   - Includes input validation and error handling

### Key Components

1. **FastAPI Application** (`app/main.py`)
   - FastAPI application configuration
   - CORS middleware setup
   - API routing and endpoint definitions
   - HTML landing page

2. **API Logic** (`app/api.py`)
   - Prediction endpoint implementation
   - Data preprocessing using pandas
   - Model inference integration
   - Error handling and response formatting

3. **Data Schemas** (`app/schemas/`)
   - Pydantic models for request/response validation
   - Input data validation rules
   - Standardized API responses

4. **Docker Configuration** (`Dockerfile`)
   - Python 3.10 base image
   - Dependencies installation
   - Application deployment setup
   - Port configuration (8001)

### Features

- **FastAPI Framework**
  - High-performance, async-capable REST API
  - Automatic OpenAPI/Swagger documentation
  - Built-in request/response validation
  - Modern Python type hints and Pydantic models

- **Docker Integration**
  - Containerized deployment
  - Consistent environment management
  - Easy scaling and orchestration
  - Isolated runtime environment

- **ML Model Serving**
  - Pre-trained Titanic survival model
  - Efficient prediction serving
  - Input data preprocessing
  - Error handling for invalid inputs

Getting Started : 

## Requirements

- Python 3.8+ (3.10 recommended)
- Docker
- FastAPI
- Pandas
- NumPy
- Pydantic
- uvicorn (for local development)

## Installation

1. Clone this repository and access the project directory:
```bash
git clone https://github.com/deebak4064/Dockerize-ML-applications-using-FastAPI.git
cd Dockerize-ML-applications-using-FastAPI
```

2. Build the Docker image:
```bash
docker build -t fastapi-ml-app .
```

3. Run the Docker container:
```bash
docker run -p 8000:8000 fastapi-ml-app
```

API Usage : 

## API Usage Guide

### Prediction Endpoint

Send a POST request to `/api/v1/predict` with passenger features:

| Feature | Description | Type | Values |
|---------|------------|------|--------|
| pclass | Passenger Class | integer | 1, 2, or 3 |
| sex | Gender | string | "male" or "female" |
| age | Age in Years | float | Any positive number |
| sibsp | Number of Siblings/Spouses Aboard | integer | 0 or positive number |
| parch | Number of Parents/Children Aboard | integer | 0 or positive number |
| fare | Ticket Fare in GBP | float | Any positive number |

## Example:
```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{"pclass": 1, "sex": "female", "age": 22, "sibsp": 0, "parch": 0, "fare": 71}'
```

Expected response:
```json
{
    "prediction": 1,
    "probability": 0.965
}
```
## Development and Testing

### Local Development
```bash
# Install dependencies
pip install -r titanic_model_api/requirements.txt

# Run the FastAPI application
uvicorn app.main:app --reload --port 8001
```

### Testing the API
1. Using curl:
```bash
curl -X POST "http://localhost:8001/api/v1/predict" \
  -H "Content-Type: application/json" \
  -d '{"pclass": 1, "sex": "female", "age": 22, "sibsp": 0, "parch": 0, "fare": 71}'
```

2. Using Python requests:
```python
import requests
import json

url = "http://localhost:8001/api/v1/predict"
data = {
    "pclass": 1,
    "sex": "female",
    "age": 22,
    "sibsp": 0,
    "parch": 0,
    "fare": 71
}

response = requests.post(url, json={"inputs": [data]})
print(json.dumps(response.json(), indent=2))
```

## Interactive Documentation
Once the server is running, you can access:
- Swagger UI documentation at: http://localhost:8001/docs
  - Interactive API testing interface
  - Detailed request/response schemas
  - Try-it-out functionality
- ReDoc documentation at: http://localhost:8001/redoc
  - Clean, responsive documentation
  - Detailed API specifications
  - Easy-to-read format

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author
Developed and maintained by Deebak Kumar K

## LinkedIn : linkedin.com/in/deebak-kumar-k-632b96285

## GitHub : https://github.com/deebak4064/Project-works

## License
This repository is licensed under the MIT License



