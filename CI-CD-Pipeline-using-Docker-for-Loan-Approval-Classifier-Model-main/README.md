# Loan Approval Classifier with CI/CD Pipeline

A production-ready machine learning system that automates loan approval decisions using a sophisticated classifier model, complete with a robust CI/CD pipeline and containerized deployment.

## 🎯 Project Overview

This project implements an end-to-end machine learning pipeline for loan approval classification, featuring:

- FastAPI-based REST API for real-time predictions
- Containerized deployment using Docker
- Automated CI/CD pipeline with GitHub Actions
- AWS-based cloud deployment
- Comprehensive testing suite
- Production-ready code structure

## 🏗️ Architecture

The system is built with a microservices architecture:

1. **ML Model Service**: Handles prediction logic and model management
2. **API Service**: Provides RESTful endpoints for client interactions
3. **CI/CD Pipeline**: Automates testing, building, and deployment
4. **Container Registry**: Manages Docker images
5. **Cloud Deployment**: Hosts the application on AWS

## 🛠️ Tech Stack

- **Machine Learning**: scikit-learn, pandas, numpy
- **API Framework**: FastAPI
- **Containerization**: Docker
- **CI/CD**: GitHub Actions
- **Cloud**: AWS (EC2, API Gateway)
- **Testing**: pytest
- **Code Quality**: black, flake8, mypy

## 📁 Project Structure

```
.
├── src/                      # Machine Learning Model Source
│   ├── config/              # Configuration management
│   ├── datasets/            # Dataset storage
│   ├── processing/          # Data processing modules
│   ├── trained_models/      # Saved model artifacts
│   └── pipeline.py          # Training pipeline
├── src_api/                 # API Service
│   ├── app/
│   │   ├── api/            # API endpoints
│   │   ├── schemas/        # Pydantic models
│   │   └── main.py         # FastAPI application
│   └── requirements.txt     # API dependencies
├── tests/                   # Test suite
├── requirements/            # Project dependencies
├── Dockerfile              # Container configuration
└── setup.py               # Package setup
```

## 🚀 Quick Start

1. **Clone the Repository**
   ```bash
   git clone https://github.com/deebak4064/CI-CD-Pipeline-using-Docker-for-Loan-Approval-Classifier-Model.git
   cd CI-CD-Pipeline-using-Docker-for-Loan-Approval-Classifier-Model
   ```

2. **Set Up Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements/requirements.txt
   ```

3. **Run Locally**
   ```bash
   uvicorn src_api.app.main:app --reload
   ```

4. **Build and Run with Docker**
   ```bash
   docker build -t loan-classifier .
   docker run -p 8001:8001 loan-classifier
   ```

## 🔄 API Endpoints

- `POST /api/v1/predict`: Get loan approval prediction
  ```json
  {
    "Gender": "Male",
    "Married": "Yes",
    "Dependents": "2",
    "Education": "Graduate",
    "Self_Employed": "No",
    "ApplicantIncome": 5000,
    "CoapplicantIncome": 1500,
    "LoanAmount": 125000,
    "Loan_Amount_Term": 360,
    "Credit_History": 1,
    "Property_Area": "Urban"
  }
  ```

- `GET /api/v1/health`: Service health check
- `GET /docs`: Interactive API documentation

## 🚦 CI/CD Pipeline

Our GitHub Actions workflow automates:

1. Code quality checks
2. Unit tests
3. Integration tests
4. Docker image building
5. Security scanning
6. AWS deployment

## 📊 Model Performance

The loan approval classifier achieves:
- Accuracy: 85%
- Precision: 83%
- Recall: 87%
- F1 Score: 85%

## 🔒 Security Features

- Containerized deployment with non-root user
- Rate limiting
- CORS protection
- Input validation
- Error handling
- Secure environment variable management

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📝 License

This project is licensed under the [MIT License](LICENSE).

## 📧 Contact

For questions or feedback, reach out on [LinkedIn](https://linkedin.com/in/deebak-kumar-k-632b96285).


