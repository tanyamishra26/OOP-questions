# TechWorld, a technology training center, wants to allocate courses for instructors. An instructor is identified by name, technology skills, experience and average feedback. An instructor is allocated a course, if he/she satisfies the below two conditions:
# eligibility criteria:
# if experience is more than 3 years, average feedback should be 4.5 or more
# if experience is 3 years or less, average feedback should be 4 or more
# he/she should posses the technology skill for the course
# Identify the class name and attributes to represent instructors. Write a Python program to implement the class chosen with its attributes and methods.
# Note:
# Consider all instance variables to be private and methods to be public.
# An instructor may have multiple technology skills, so consider instance variable, technology_skill to be a list.
# check_eligibility(): Return true if eligibility criteria is satisfied by the instructor. Else, return false
# allocate_course(technology): Return true if the course which requires the given technology can be allocated to the instructor. Else, return false.
# Represent a few objects of the class, initialize instance variables using setter methods, invoke appropriate methods and test your program.



class Instructor:
    def __init__(self,name,skill,experience,feedback):
        self.__name=name
        self.__technology_skills=skill
        self.__experience=experience
        self.__feedback=feedback
    def check_eligibility(self):
        if (self.__experience>3 and self.__feedback>=4.5) or (self.__experience<3 and self.__feedback>=4):
            return True
        else:
            return False
    
    def allocate_course(self,technology):
        if self.check_eligibility() and technology in self.__technology_skills:
            return True
        else:
            return False
    def get_name(self):
        return self.__name
    def get_technology_skills(self):
        return self.__technology_skills
    def get_experience(self):
        return self.__experience
    def get_feedback(self):
        return self.__feedback
    def set_name(self,name):
        self.__name=name
    def set_technology_skills(self,skill):
        self.__technology_skills=skill
    def set_experience(self,experience):
        self.__experience=experience
    def set_feedback(self,feedback):
        self.__feedback=feedback
        
instructor1=Instructor("John","Python",5,4.5)
print(instructor1.check_eligibility())
print(instructor1.allocate_course("Java"))
print(instructor1.get_name())
print(instructor1.get_technology_skills())
print(instructor1.get_experience())
print(instructor1.get_feedback())
instructor1.set_name("Jane")
instructor1.set_technology_skills(["Java","C++"])
instructor1.set_experience(2)
instructor1.set_feedback(4.2)
print(instructor1.get_name())
print(instructor1.get_technology_skills())
print(instructor1.get_experience())
print(instructor1.get_feedback())

    