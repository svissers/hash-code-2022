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

    def finish_project(self):
        pass


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

    def get_score(self, day):
        return 5


    def tick(self, curr_day) -> bool:
        assert self.start_date is not None

        if self.duration <= curr_day - self.start_date:
            # Update person skill set and free() person
            for person in self.persons:
                person.finish_project()

            # remove persons en reset start date
            self.persons = []
            self.start_date = None

            return True

        return False

class Game:

    def __init__(self):
        self.day = 0
        self.score = 0

    def tick(self, running_projects):
        self.day = self.day + 1

        # Iterate over running projects
        for project in running_projects[:]:
            if project.tick():
                score = score + project.get_score(day)
                running_projects.remove(project)




def solve(persons, projects, days):
    current_day = 0

    game = Game()
    running_projects = []

    while len(projects) != 0:

        for project in projects:
            # try to start as many projects with current devs
            pass

        # game tick
        game.tick(running_projects)

        # score berekenen --> check if project klaar
        # if klaar, delete from lijst


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
        nr_of_days = max(nr_of_days, int(days))

    solve(person_list, project_list, nr_of_days)


if __name__ == '__main__':
    main()
