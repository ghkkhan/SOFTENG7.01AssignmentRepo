import pytest
import System

# Tests if the program can handle a correct Username 

# Passes
def test_login(grading_system):
    users = grading_system.users
    username = 'akend3'
    password =  '123454321'
    grading_system.login(username,password)
    if users[username]['role'] != 'student':
        assert False
    # else asserts true!

#test the check_password function
#should pass 
def test_check_password(grading_system):
    if(grading_system.check_password("cmhbf5", "best-ta") == True):
        assert False
    if(grading_system.check_password('cmhbf5', 'bestta') == True):
        assert False
    if(grading_system.check_password('cmhbf5', 'best TA') == True):
        assert False
    if(grading_system.check_password('cmhbf5', 'bestTA') == False):
        assert False
    # else assert true!


# checks the change_grade function... fails
def test_change_grade(grading_system):
    grading_system.login("saab", 'boomr345')
    grading_system.usr.change_grade('akend3', 'comp_sci',  'assignment1', '33') # this function fails because the 'grade' is hardcoded... '33' is ignored
    users = grading_system.users
    if users['akend3']['courses']['comp_sci']['assignment1']['grade'] != 33:
        assert False

# checks the create_assignment function... with an invalid date...
# test fails... the function should never create an assignment with an invalid date
def test_create_assignment(grading_system):
    grading_system.login('saab', 'boomr345')
    user = grading_system.usr
    user.create_assignment('assignment3', 'invalid_date', 'comp_sci')
    courses = grading_system.courses
    if courses['comp_sci']['assignments']['assignment3']['due_date'] == 'invalid_date':
        assert False

# add_student() function tester
#Passes
def test_add_student(grading_system):
    grading_system.login('saab','boomr345')
    user = grading_system.usr
    user.add_student('hdjsr7', 'comp_sci')
    users = grading_system.users
    if 'comp_sci' in users['hdjsr7']['courses']:
        assert True
    else:
        assert False

#tests if students can be dropped... passes
def test_drop_student(grading_system):
    grading_system.login('saab','boomr345')
    user = grading_system.usr
    user.drop_student('akend3', 'comp_sci')
    users = grading_system.users
    if 'comp_sci' in users['akend3']['courses']:
        assert False

# tests the submition function...
# passes...
def test_submit_assignment(grading_system):
    grading_system.login('akend3', "123454321")
    user = grading_system.usr
    user.submit_assignment('databases', 'assignment1', "assignment 1 is done", '1/1/19')
    users = grading_system.users
    if users['akend3']['courses']['databases']['assignment1']['submission_date'] != '1/1/19':
        assert False

#tests the check_ontime function.......
#returns false...
def test_check_ontime(grading_system):
    grading_system.login('akend3', '123454321')
    user = grading_system.usr
    if user.check_ontime('1/4/99', '1/5/20') == True: # shouldn't return on time!
        assert False

#checks the check_grades function...
# asserts false...
def test_check_grades(grading_system):
    grading_system.login('hdjsr7', 'pass1234')
    user = grading_system.usr
    grades = user.check_grades('comp_sci')
    if grades != 'N/A':
        assert False

# tests the view_assignment function... and fails
def test_view_assignments(grading_system):
    grading_system.login('akend3', '123454321')
    user = grading_system.usr
    assignments = user.view_assignments('databases')
    if len(assignments) != 2: # databases has 2 assignments...
        assert False

# additional 5 tests...
# tests to see if the login function correctly handles an empty username... it doesnt
def test_empty_user_name_login(grading_system):
    username = ''
    password =  'random'
    grading_system.login(username,password) # A KEYERROR!!!
    if users[username]['role'] == 'student':
        assert False
    # else asserts true!

# checks to see if add_student can handle a student that doesn't exist...
def test_empty_add_student(grading_system):
    grading_system.login('saab','boomr345')
    user = grading_system.usr
    user.add_student('hkg8b', 'comp_sci')
    users = grading_system.users
    if 'comp_sci' in users['hkg8b']['courses']:
        assert True
    else:
        assert False

# next up is droping a student that doesn't exist...
def test_dropping_empty_student(grading_system):
    grading_system.login('saab','boomr345')
    user = grading_system.usr
    user.drop_student('hkg8b', 'comp_sci')
    users = grading_system.users
    if 'hkg8b' in users:
        assert False

# change grade function, but the assignment doesnt exist
#fails test
def test_change_grade_assignment_doesnt_exist(grading_system):
    grading_system.login("saab", 'boomr345')
    grading_system.usr.change_grade('akend3', 'databases',  'assignment99', '33') # this function fails because the 'grade' is hardcoded... '33' is ignored
    users = grading_system.users
    if users['akend3']['courses']['comp_sci']['assignment1']['grade'] != 33:
        assert False

#tests the submit assignment function again... but with an assignment that doesn't exist
def test_submit_assignment_that_doesnt_exist(grading_system):
    grading_system.login('akend3', "123454321")
    user = grading_system.usr
    user.submit_assignment('databases', 'assignment99', "assignment 1 is done", '1/1/19')
    users = grading_system.users
    if users['akend3']['courses']['databases']['assignment1']['submission_date'] != '1/1/19':
        assert False

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem