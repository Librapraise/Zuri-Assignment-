class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self,name="Barnes", age=28, tracks=["FE","BE"],score=30.90):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score
    def change_name(self,new_name):
        self.name = new_name

    def change_age(self,new_age):
            self.age = new_age

    def add_track(self,new_track):
        self.tracks = new_track

    def get_score(self):
        if  isinstance(self.age,int):
            print(self.name,self.age,self.tracks,self.score)
        else:
            print('Age must be integer. Try again!')


Barnes = Student(name="Barnes", age=28, tracks=["FE","BE"],score=30.90)

# Expected methods
Barnes.change_name("Praise")
Barnes.change_age(24.78)
Barnes.add_track("UI/UX")
Barnes.get_score()
