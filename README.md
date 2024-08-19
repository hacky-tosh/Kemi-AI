# Kemo-AI


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




  
### 2. Get Course Overview

- **Route**: `/course-overview`
- **Method**: `GET`
- **Query Parameters**:
   `course_name` (required): The name of the course to retrieve.
- **Example**:

  ```http
  GET /course-overview?course_name=Python%20Programming



