
from main import read_route,greet


def test_greet():
    result = greet("Grade", 18)

    expected = {"message": "Hello!", "additional_info": "You have passed the exam."}

 
    print(f"Expected result: {expected}")
    print(f"Actual result: {result}")
    assert result == expected

def test_read_route():
    result=read_route()
    expected = {"message":"Hello, FastAPI"}
    print(f"Expected result: {expected}")
    print(f"Actual result: {result}")
    assert result==expected