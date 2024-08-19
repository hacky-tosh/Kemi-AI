from fastapi import APIRouter, HTTPException, Query
from typing import List
from app.db import db
from app.models import Course, Chapter

course_router = APIRouter()



# Endpoint to get all courses and filter them by domain, alphabetical order, or rating
# (e.g., /courses?sort_by=date&domain=Programming)
# (e.g., /courses?sort_by=rating)
# (e.g., /courses?sort_by=alphabetical)
@course_router.get("/courses", response_model=List[Course])
def get_courses(sort_by: str = "alphabetical", domain: str = None):
    sort_options = {
        "alphabetical": ("name", 1),
        "date": ("date", -1),
        "rating": ("ratings.average", -1)
    }
    sort_field, sort_order = sort_options.get(sort_by, ("name", 1))

    query = {}
    if domain:
        query["domain"] = domain

    courses = list(db.courses.find(query).sort(sort_field, sort_order))
    return courses



# Endpoint to get the overview of a course by its name 
# (e.g., /course-overview?course_name=Python%20Programming)
@course_router.get("/course-overview", response_model=Course)
def get_course_overview(course_name: str = Query(..., description="Name of the course")):
    course = db.courses.find_one({"name": course_name})
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return course



# Endpoint to get the information of a chapter by its name and course name
# (e.g., /course-chapter?course_name=AI%20Basics&chapter_name=Introduction%20to%20AI)
@course_router.get("/course-chapter", response_model=Chapter)
def get_chapter_info(course_name: str = Query(...), chapter_name: str = Query(...)):
    course = db.courses.find_one({"name": course_name})
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")

    for chapter in course["chapters"]:
        if chapter["name"] == chapter_name:
            return chapter
    raise HTTPException(status_code=404, detail="Chapter not found")


# Endpoint to rate a chapter of a course
# (`positive` is a boolean that indicates whether the rating is positive or negative)
# (e.g., /course-rate?course_name=Computer%20Vision%20Course&chapter_name=Introduction%20to%20Neural%20Networks&positive=false)
@course_router.post("/course-rate")
def rate_chapter(course_name: str, chapter_name: str, positive: bool):
    course = db.courses.find_one({"name": course_name})
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")

    chapter_found = False
    for chapter in course["chapters"]:
        if chapter["name"] == chapter_name:
            chapter_found = True

            # Initializing ratings if not present
            if "ratings" not in chapter:
                chapter["ratings"] = {"positive": 0, "negative": 0, "average": 0}

            # Updating chapter ratings
            if positive:
                chapter["ratings"]["positive"] += 1
            else:
                chapter["ratings"]["negative"] += 1

            # Recalculating average rating for the chapter
            chapter["ratings"]["average"] = (
                chapter["ratings"]["positive"] - chapter["ratings"]["negative"]
            )

            # Updating chapter ratings in the database
            db.courses.update_one(
                {"name": course_name, "chapters.name": chapter_name},
                {"$set": {"chapters.$.ratings": chapter["ratings"]}}
            )

            # Recalculating average rating for the course
            total_positive = 0
            total_negative = 0
            for ch in course["chapters"]:
                if "ratings" in ch:
                    total_positive += ch["ratings"].get("positive", 0)
                    total_negative += ch["ratings"].get("negative", 0)
            course["average_rating"] = total_positive - total_negative

            # Updating course average rating in the database
            db.courses.update_one(
                {"name": course_name},
                {"$set": {"average_rating": course["average_rating"]}}
            )

            return {
                "message": "Rating updated successfully",
                "ratings": chapter["ratings"],
                "average_rating": course["average_rating"]
            }

    if not chapter_found:
        raise HTTPException(status_code=404, detail="Chapter not found")