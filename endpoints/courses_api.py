from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(tags=["Courses"], prefix="/api/v1/courses")


class Course(BaseModel):
    id: int
    title: str
    description: str
    price: float
    currency: str
    starting_at: str
    rating: int

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 3,
                    "title": "Programavimas Java",
                    "description": "Kompiliuojama kalba",
                    "price": 22.01,
                    "currency": "eur",
                    "starting_at": "2023-01-11",
                    "rating": 2
                }
            ]
        }
    }


courses_db = [
    Course(id=1,
           title="Python",
           description="Python programavimas",
           price=2.4,
           currency="eur",
           starting_at="2023-09-22",
           rating=5),
    Course(id=1,
           title="C++",
           description="C++ programavimas",
           price=2.5,
           currency="eur",
           starting_at="2023-09-23",
           rating=4)
]


@router.head("/")
@router.get("/")
async def get_all_courses():
    return courses_db


@router.post("/add")
async def create_new_course(course: Course):
    courses_db.append(course)
    return course


@router.get("{courses_id}")
async def get_course_by_id(course_id: int):
    return courses_db[get_first_course(course_id)]


def get_first_course(course_id: int):
    for index, course in enumerate(courses_db):
        if course.id == course_id:
            return index
    return -1
