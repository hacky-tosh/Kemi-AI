## Kemo-AI


# FastAPI Course Management API

This FastAPI application provides endpoints for managing courses and chapters, including retrieving courses, getting course overviews, retrieving chapter information, and rating chapters.

## Endpoints

### 1. Get All Courses

- **Route**: `/courses`
- **Method**: `GET`
- **Query Parameters**:
  - `sort_by` (optional): Specify the sort order. Can be `alphabetical`, `date`, or `rating`. Default is `alphabetical`.
  - `domain` (optional): Filter courses by domain.
- **Response**: A list of courses, sorted according to the specified criteria.
- **Example**:

  ```http
  GET /courses?sort_by=date&domain=Programming
