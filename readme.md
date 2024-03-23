# Project Report: Learning Management System (LMS) Backend

## Introduction
The Learning Management System (LMS) backend project aims to provide a platform for managing users, classes, assignments, and questions within an educational setting. This report outlines the design and implementation of the backend infrastructure and APIs for the LMS.

## Project Structure
The project follows a Django project structure, with the main components being models, serializers, views, and URLs.

### Models
- **User**: Represents both teachers and students, with additional fields for role, first name, last name, and profile picture URL.
- **Class**: Represents different classes taught by teachers, with fields for name, teacher, students, start date, description, and subject.
- **Assignment**: Represents assignments posted by teachers for classes, with fields for title, description, due date, class, created by, max points, and submission type.
- **Question**: Represents AI-generated questions for assignments, with fields for text, assignment, and question type.

### Serializers
- Serializers are defined for each model to handle serialization and deserialization of data for API requests and responses.

### Views
- Viewsets are used to define CRUD operations for each model.
- Custom logic is implemented in views to handle permissions and filtering based on user roles.

### URLs
- URLs are configured using Django's URL patterns to map endpoints to viewsets.

## API Endpoints
The following RESTful APIs are implemented using Django REST Framework:
- **User Authentication**: POST `/api-auth/login/` for user authentication.
- **CRUD Operations**:
  - Users: GET, POST, PUT, DELETE `/api/users/`
  - Classes: GET, POST, PUT, DELETE `/api/classes/`
  - Assignments: GET, POST, PUT, DELETE `/api/assignments/`
  - Questions: GET, POST, PUT, DELETE `/api/questions/`

## Request/Response Formats
### Request Formats
- Requests are sent as JSON data in the request body for POST and PUT operations.

### Response Formats
- Responses are returned as JSON data in the response body for all CRUD operations.
- Successful responses include status code 200 (OK).
- Error responses include appropriate status codes (e.g., 400 for bad requests, 401 for unauthorized access) along with error messages.

## Conclusion
The implementation of the LMS backend infrastructure and APIs provides essential functionality for managing users, classes, assignments, and questions. The project adheres to RESTful principles and follows best practices for API design and development.

## Future Enhancements
- Implementation of additional features such as grading and submission tracking.
- Integration with front-end frameworks for building a complete LMS platform.
