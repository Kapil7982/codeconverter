# Code Conversion and Quality Check Application

This application allows you to convert code from one programming language to another, perform code debugging, and check the quality of the code using the OpenAI GPT-3.5 Turbo model. It provides a simple API for developers to interact with these features.

## Getting Started

Follow the steps below to set up and run the application on your local machine.

### Prerequisites

Before you begin, make sure you have the following software installed:

- Python : [[Download and install Node.js](https://nodejs.org/](https://www.python.org/downloads/))
- flask: Install flask

### Installation

1. Clone this repository to your local machine:

```bash
   git clone <https://github.com/Kapil7982/codeconverter.git>
```

### API Endpoints
Code Conversion
Endpoint: /api/convert
Method: POST
Request Body:
```bash
   {
     "code": "Your code here",
     "targetLanguage": "Target language"
   }
```
Response
```bash
   {
     "output": "Converted code"
   }
```

Code Debugging
Endpoint: /api/debug
Method: POST
Request Body:
```bash
   {
     "code": "Your code here",
    "targetLanguage": "Target language
   }
```
Response
```bash
   {
     "debuggingOutput": "Debugged code"
   }
```

Code Quality Check
Endpoint: /api/quality
Method: POST
Request Body:
```bash
   {
     "code": "Your code here",
    "targetLanguage": "Target language"
   }
```
Response
```bash
   {
    "qualityOutput": "Quality assessment result"
   }
```
### Customization
You can customize the behavior of the code conversion, debugging, and quality check by adjusting parameters like Temperature, Maximum Length, Stop Sequences, and Top P in the app.py file.

![image](https://github.com/Kapil7982/codeconverter/assets/103938868/d3681ff7-2f79-4a4c-8dca-127d696f0e25)

