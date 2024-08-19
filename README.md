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


### 3.  Get Chapter Information

- **Route**: `/course-chapter`
- **Method**: `GET`
- **Query Parameters**:
  `course_name` (required): The name of the course that contains the chapter.
  `chapter_name` (required): The name of the chapter to retrieve.
- **Example**:

  ```http
GET /course-chapter?course_name=AI%20Basics&chapter_name=Introduction%20to%20AI




### 4.  Get Chapter Information

- **Route**: `/course-rate`
- **Method**: `POST`
- **Query Parameters**:
 `course_name` (required): The name of the course containing the chapter.
 `chapter_name` (required): The name of the chapter to rate.
 `positive` (required): A boolean value indicating if the rating is positive (true) or negative (false).

- **Response**: A message indicating the rating update status, along with the updated chapter and course ratings.

- **Example**:

  ```http
POST /course-rate?course_name=Computer%20Vision%20Course&chapter_name=Introduction%20to%20Neural%20Networks&positive=false
  



