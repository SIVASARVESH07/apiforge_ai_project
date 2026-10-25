# Patient Management API

Generated API based on requirements: build  a hospital api for admitting patients,consulting doctors,diagnosis,admitted date 
...

Designed and generated using **APIForge AI** multi-agent framework.

## Getting Started

### 1. Run the Backend Service
```bash
python -m uvicorn app.main:app --reload --port 8000
```

### 2. View Interactive Documentation
- **Swagger UI**: Open `swagger.html` in your browser or visit `http://localhost:8000/docs`
- **Redoc**: Open `redoc.html` in your browser or visit `http://localhost:8000/redoc`
- **API Reference**: Read `API_REFERENCE.md`

### 3. Run Automated Tests
```bash
pytest tests/ -v
```
