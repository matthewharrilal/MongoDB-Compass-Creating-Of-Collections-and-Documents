from pymongo import MongoClient
import json


if __name__ == '__main__':
    course_dictionary = {"subject": "Science",
                        "course_id": 38428,
                        "students": ["Matthew","Shannon Dougherty", "Corey", "Steven Spielberg"]}
    client = MongoClient('mongodb://localhost:27017/')
    # This essentially creates our database
    db = client["courses"]
    # This is what is going to be creating our collection within the database
    subject_courses = db.subject_courses
    subject_courses.drop()
    #  Now that we have a collection we have to be able to create the documents that populate the collection
    subject_courses.insert_one(course_dictionary)

    #We are going to create another document that serves as another documents
    second_course_dictionary = {"name": "Social Studies",
                                "course_id": 32334,
                                "students": ["Matthew", "Corey", "Rohan"]}
    third_course_dictionary = {"name": "Economics",
                              "course_id": 36248,
                              "students": ["Matthew", "Other People", "Corey", "Nick Swift"]}
    #In this line of code we are essentially inserting another document into our collection
    subject_courses.insert_one(second_course_dictionary)
    subject_courses.insert_one(third_course_dictionary)
