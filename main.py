class Skill:
    def __init__(self, name, level):
        self.name = name
        self.level = int(level)


class Person:
    def __init__(self, name):
        self.name = name
        self.skills = []
        self.current_project = None
        self.current_skill = None

    def add_skill(self, skill):
        self.skills.append(skill)

    def set_project(self, project, project_skill):
        self.current_project = project
        for skill in self.skills:
            if skill.name == project_skill.name:
                self.current_skill = skill

    def release_project(self):
        self.current_project = None

    def finish_project(self):
        self.current_skill.level = self.current_skill.level + 1
        self.current_skill = None

    def busy(self):
        return self.current_project is not None

    def has_skill(self, other_skill, persons):
        if not self.busy():
            for skill in self.skills:
                if skill.name == other_skill.name and skill.level == other_skill.level:
                    return True
        return False

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

    def tick_stijn(self, day):
        if self.start_date is not None:
            self.duration -= 1
            if self.duration == 0:
                for person in self.persons:
                    person.release_project()
                return True
            else:
                return False

    def can_start(self, persons):
        for skill in self.requirements:
            for person in persons:
                if person.has_skill(skill, self.persons):
                    person.set_project(self, skill)
                    self.persons.append(person)

        if len(self.persons) == len(self.requirements):
            return True
        for person in self.persons:
            person.release_project()
        return False

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
        self.day += 1

        # Iterate over running projects
        for project in running_projects[:]:
            if project.tick():
                self.score = self.score + project.get_score(self.day)
                running_projects.remove(project)


def solve(persons, projects):
    solved_projects = []
    game = Game()
    running_projects = []
    tick = 0

    while len(projects) != 0:

        for project in projects:
            # try to start as many projects with current devs
            # add it to the solved_projects list
            if project.can_start(persons):
                project.start_date = tick
                solved_projects.append(project)

        # game tick

        for project in projects[:]:
            # tick == true ==> done
            if project.tick(tick):
                projects.remove(project)

        tick += 1

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
