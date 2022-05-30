# Code for testing love score function

from den_package.love import love_score

def test_love_score():
    results = love_score('Henry', 'Ahmed')
    assert type(results) == str
