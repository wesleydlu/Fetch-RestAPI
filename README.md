# Fetch Backend Challenge

## Getting Started

This guide helps you test the API with Postman and Uvicorn 

### Required Packages

These are the required packages for the exercise (except for Postman)
- Python 3.8 or higher
- FastAPI
- Uvicorn
- Postman

If not already installed, use the command below for Mac M1 Users

```bash
pip install fastapi uvicorn
```

### Uvicorn

First go to the directory with the exercise and use Uvicorn to run the server.

```bash
cd /pathToYourProjectDirectory
uvicorn fetch:app --reload
```

### Accessing the Server

The base URL for all API requests is: 

```
http://127.0.0.1:8000
```

### Adding a Transaction

**Method**: POST
**URL**: `http://127.0.0.1:8000/add`
**Body** (select raw and set type to JSON):
   ```json
   {
     "payer": "DANNON",
     "points": 5000,
     "timestamp" : "2020-11-02T14:00:00Z"
   }
   ```

### Spending Points

**Method**: POST
**URL**: `http://127.0.0.1:8000/spend`
**Body** (select raw and set type to JSON):
   ```json
   {
     "points": 500
   }
   ```

### Checking Balance

**Method**: GET
**URL**: `http://127.0.0.1:8000/balance`

