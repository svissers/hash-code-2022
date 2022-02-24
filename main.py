class Skill:
    def __init__(self, name, level):
        self.name = name
        self.level = int(level)


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
        self.duration = int(duration)
        self.best_before = int(best_before)
        self.score = int(score)
        self.requirements = []
        self.start_date = None
        self.persons = []

    def add_skill(self, skill):
        self.requirements.append(skill)

    def tick(self, running_projects):
        pass

class Game:

    def __init__(self):
        self.day = 0

    def tick(self):
        self.day = self.day + 1

        # Iterate over running projects
        #


def solve(persons, projects):
    solved_projects = []
    game = Game()
    running_projects = []

    while len(projects) != 0:

        for project in projects:
            # try to start as many projects with current devs
            # add it to the solved_projects list
            pass

        # game tick
        game.tick(running_projects)

        # score berekenen --> check if project klaar
        # if klaar, delete from lijst

    with open("solution.txt", "w") as f:
        f.write("{}\n".format(str(len(solved_projects))))
        for project in solved_projects:
            f.write("{}\n".format(project.name))

            names = [person.name for person in project.persons]
            f.write(" ".join(names))
            f.write("\n")


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

    nr_of_days = 0

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

    solve(person_list, project_list)


if __name__ == '__main__':
    main()
