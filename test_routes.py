from fastapi.testclient import TestClient
from app.main import app
from pymongo import MongoClient

client = TestClient(app)
mongo_client = MongoClient("mongodb+srv://ashu:KCL566yash@cosmocloud.sqt8n68.mongodb.net/")
db = mongo_client['test_db']

def setup_module(module):
    db.courses.delete_many({})
    db.courses.insert_many([
        {
            "name": "Highlights of Calculus",
            "date": 1530133200,
            "description": "Highlights of Calculus is a series of short videos that introduces the basic ideas of calculus — how it works and why it is important. The intended audience is high school students, college students, or anyone who might need help understanding the subject.\nIn addition to the videos, there are summary slides and practice problems complete with an audio narration by Professor Strang. You can find these resources to the right of each video.",
            "domain": ["mathematics"],
            "chapters": [
                {"name": "Gil Strang's Introduction to Calculus for Highlights for High School", "text": "Highlights of Calculus"},
                {"name": "Big Picture of Calculus", "text": "Highlights of Calculus"},
                {"name": "Big Picture: Derivatives", "text": "Highlights of Calculus"},
                {"name": "Max and Min and Second Derivative", "text": "Highlights of Calculus"},
                {"name": "The Exponential Function", "text": "Highlights of Calculus"},
                {"name": "Big Picture: Integrals", "text": "Highlights of Calculus"},
                {"name": "Derivative of sin x and cos x", "text": "Highlights of Calculus"},
                {"name": "Product Rule and Quotient Rule", "text": "Highlights of Calculus"},
                {"name": "Chains f(g(x)) and the Chain Rule", "text": "Highlights of Calculus"},
                {"name": "Limits and Continuous Functions", "text": "Highlights of Calculus"},
                {"name": "Inverse Functions f ^-1 (y) and the Logarithm x = ln y", "text": "Highlights of Calculus"},
                {"name": "Derivatives of ln y and sin ^-1 (y)", "text": "Highlights of Calculus"},
                {"name": "Growth Rate and Log Graphs", "text": "Highlights of Calculus"},
                {"name": "Linear Approximation/Newton's Method", "text": "Highlights of Calculus"},
                {"name": "Power Series/Euler's Great Formula", "text": "Highlights of Calculus"},
                {"name": "Differential Equations of Motion", "text": "Highlights of Calculus"},
                {"name": "Differential Equations of Growth", "text": "Highlights of Calculus"},
                {"name": "Six Functions, Six Rules, and Six Theorems", "text": "Highlights of Calculus"}
            ]
        },
        {
            "name": "Introduction to Programming",
            "date": 1659906000,
            "description": "An introduction to programming using a language called Python. Learn how to read and write code as well as how to test and \"debug\" it. Designed for students with or without prior programming experience who'd like to learn Python specifically. Learn about functions, arguments, and return values (oh my!); variables and types; conditionals and Boolean expressions; and loops. Learn how to handle exceptions, find and fix bugs, and write unit tests; use third-party libraries; validate and extract data with regular expressions; model real-world entities with classes, objects, methods, and properties; and read and write files. Hands-on opportunities for lots of practice. Exercises inspired by real-world programming problems. No software required except for a web browser, or you can write code on your own PC or Mac.",
            "domain": ["programming"],
            "chapters": [
                {"name": "This is CS50x 2022, now in 4K HDR", "text": "Introduction to Programming"},
                {"name": "CS50 2021 in HDR - Lecture 0 - Scratch", "text": "Introduction to Programming"},
                {"name": "CS50 2021 in HDR - Lecture 1 - C", "text": "Introduction to Programming"},
                {"name": "CS50 2021 in HDR - Lecture 2 - Arrays", "text": "Introduction to Programming"},
                {"name": "CS50 2021 in HDR - Lecture 3 - Algorithms", "text": "Introduction to Programming"},
                {"name": "CS50 2021 in HDR - Lecture 4 - Memory", "text": "Introduction to Programming"},
                {"name": "CS50 2021 in HDR - Lecture 5 - Data Structures", "text": "Introduction to Programming"},
                {"name": "CS50 2021 in HDR - Lecture 6 - Python", "text": "Introduction to Programming"},
                {"name": "CS50 2021 in HDR - Lecture 7 - SQL", "text": "Introduction to Programming"},
                {"name": "CS50 2021 in HDR - Cybersecurity", "text": "Introduction to Programming"},
                {"name": "CS50 2021 in HDR - Lecture 8 - HTML, CSS, JavaScript", "text": "Introduction to Programming"},
                {"name": "CS50 2021 in HDR - Lecture 9 - Flask", "text": "Introduction to Programming"},
                {"name": "CS50 2021 in HDR - Lecture 10 - Emoji", "text": "Introduction to Programming"}
            ]
        },
        {
            "name": "Computer Vision Course",
            "date": 1502398800,
            "description": "Computer Vision has become ubiquitous in our society, with applications in search, image understanding, apps, mapping, medicine, drones, and self-driving cars. Core to many of these applications are visual recognition tasks such as image classification, localization and detection. Recent developments in neural network (aka “deep learning”) approaches have greatly advanced the performance of these state-of-the-art visual recognition systems. This lecture collection is a deep dive into details of the deep learning architectures with a focus on learning end-to-end models for these tasks, particularly image classification. From this course, students will learn to implement, train and debug their own neural networks and gain a detailed understanding of cutting-edge research in computer vision.\n",
            "domain": ["computer vision", "artificial intelligence"],
            "chapters": [
                {"name": "Introduction to Convolutional Neural Networks for Visual Recognition", "text": "Computer Vision Course. CS231n L1 History of computer vision"},
                {"name": "Image Classification", "text": "Computer Vision Course"},
                {"name": "Loss Functions and Optimization", "text": "Computer Vision Course. CS231n L3 Regularization and optimization"},
                {"name": "Introduction to Neural Networks", "text": "Computer Vision Course. CS231n L4 Neural networks and backpropagation"},
                {"name": "Convolutional Neural Networks", "text": "Computer Vision Course"},
                {"name": "Training Neural Networks I", "text": "Computer Vision Course. CS231n L6 CNN architectures"},
                {"name": "Training Neural Networks II", "text": "Computer Vision Course. CS231n L7 Training neural networks"},
                {"name": "Deep Learning Software", "text": "Computer Vision Course. CS231n L8 Visualizing and understanding"},
                {"name": "Recurrent Neural Networks", "text": "Computer Vision Course. CS231n L9 Object detection and image segmentation"},
                {"name": "CNN Architectures", "text": "Computer Vision Course. CS231n L10 Recurrent neural networks"},
                {"name": "Detection and Segmentation", "text": "Computer Vision Course. CS231n L11 Attention and transformers"},
                {"name": "Detection and Segmentation", "text": "Computer Vision Course. CS231n L12 Video understanding"},
                {"name": "Visualizing and Understanding", "text": "Computer Vision Course. CS231n L13 Generative models"},
                {"name": "Generative Models", "text": "Computer Vision Course. CS231n L14 Self-supervised learning"},
                {"name": "Deep Reinforcement Learning", "text": "Computer Vision Course"},
                {"name": "Efficient Methods and Hardware for Deep Learning", "text": "Computer Vision Course"},
                {"name": "Adversarial Examples and Adversarial Training", "text": "Computer Vision Course"}
            ]
        },
        {
            "name": "Introduction to Deep Learning",
            "date": 1653512400,
            "description": "Course lectures for MIT Introduction to Deep Learning.",
            "domain": ["artificial intelligence"],
            "chapters": [
                {"name": "MIT Introduction to Deep Learning", "text": "Introduction to Deep Learning. Deep Learning Lesson 1"},
                {"name": "Recurrent Neural Networks and Transformers", "text": "Introduction to Deep Learning"},
                {"name": "Convolutional Neural Networks", "text": "Introduction to Deep Learning. Deep Learning Lesson 3"},
                {"name": "Deep Generative Modeling", "text": "Introduction to Deep Learning. Deep Learning Lesson 4"}
            ]
        }
    ])

def test_get_courses():
    response = client.get("/courses")
    assert response.status_code == 200
    assert len(response.json()) == 4  


def test_search_courses_by_domain():
    response = client.get("/courses", params={"domain": "mathematics"})
    assert response.status_code == 200
    courses = response.json()
    assert len(courses) == 1
    assert courses[0]["name"] == "Highlights of Calculus"
    
    
    
def test_get_course_by_name():
    response = client.get("/course-overview?course_name=Highlights%20of%20Calculus")
    assert response.status_code == 200
    course = response.json()
    assert course["name"] == "Highlights of Calculus"
    assert len(course["chapters"]) == 18  
    
