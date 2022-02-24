# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Skill:
    def __init__(self, name, level):
        self.name = name
        self.level = level


class Person:
    def __init__(self, name):
        self.name = name
        self.skills = []
        self.current_project = None

    def add_skill(self, skill):
        self.skills.append(skill)


class Project:
    def __init__(self, name, duration, score, best_before):
        self.name = name
        self.duration = duration
        self.best_before = best_before
        self.score = score
        self.requirements = []

    def add_skill(self, skill):
        self.requirements.append(skill)


def solve(persons, projects):
    pass


def main():
    person_list = []
    project_list = []

    infile = "input_data/a_an_example.in.txt"
    with open(infile) as f:
        lines = f.readlines()

    contributors, projects = lines[0].split(" ")

    line = 1
    for i in range(int(contributors)):
        name, skillnr = lines[line].split(" ")
        contributor = Person(name)
        for j in range(int(skillnr)):
            line += 1
            skill_name, skill_level = lines[line].split(" ")
            skill = Skill(skill_name, int(skill_level))
            contributor.add_skill(skill)
        line += 1
        person_list.append(contributor)

    for i in range(int(projects)):
        project_name, days, score, before, nr_roles = lines[line].split(" ")
        project = Project(project_name, days, score, before)
        for j in range(int(nr_roles)):
            line += 1
            skill_name, skill_level = lines[line].split(" ")
            skill = Skill(skill_name, int(skill_level))
            project.add_skill(skill)
        line += 1
        project_list.append(project)


    print(contributors)

    solve(person_list, project_list)



if __name__ == '__main__':
    main()

