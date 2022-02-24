class Skill:
    def __init__(self, name, level):
        self.name = name
        self.level = int(level)

    def __eq__(self, other):
        return self.name == other.name

    def is_good_enough(self, other, persons):
        if self.name == other.name:
            if self.level >= other.level:
                return True
        # TODO Check mentor
        return False

    def __repr__(self):
        return "{} level {}".format(self.name, str(self.level))


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
            if skill == project_skill:
                self.current_skill = skill

    def release_project(self):
        self.current_project = None

    def finish_project(self):
        self.current_skill.level = self.current_skill.level + 1
        self.current_skill = None
        self.current_project = None

    def busy(self):
        return self.current_project is not None

    def has_skill(self, other_skill, persons):
        if not self.busy():
            for skill in self.skills:
                if skill.is_good_enough(other_skill, persons):
                    return True
        return False

    def __repr__(self):
        return "person {}".format(self.name)


class Project:
    def __init__(self, name, duration, score, best_before):
        self.name = name
        self.duration = int(duration)
        self.best_before = int(best_before)
        self.score = int(score)
        self.requirements = []
        self.start_date = None
        self.persons = []

    def start(self, day):
        self.start_date = day

    def add_skill(self, skill):
        self.requirements.append(skill)

    # def tick_stijn(self, day):
    #     if self.start_date is not None:
    #         self.duration -= 1
    #         if self.duration == 0:
    #             for person in self.persons:
    #                 person.release_project()
    #             return True
    #         else:
    #             return False

    def can_start(self, persons):
        for skill in self.requirements:
            for person in persons:
                if not person.busy():
                    if person.has_skill(skill, self.persons):
                        person.set_project(self, skill)
                        self.persons.append(person)

        if len(self.persons) == len(self.requirements):
            return True
        for person in self.persons:
            person.release_project()
        self.persons = []
        return False

    def get_score(self, day):
        return 5

    def tick(self, curr_day) -> bool:
        assert self.start_date is not None

        if self.duration <= curr_day - self.start_date:
            # Update person skill set and free() person
            for person in self.persons:
                person.finish_project()
            return True
        return False

    def __repr__(self):
        return "project {}".format(self.name)


class Game:
    def __init__(self, projects, persons):
        self.day = 0
        self.score = 0
        self.projects = projects
        self.running_projects = []
        self.solved_projects = []
        self.persons = persons

    def tick(self):
        for project in self.projects[:]:
            if project.can_start(self.persons):
                project.start(self.day)
                self.running_projects.append(project)
                self.solved_projects.append(project)
                self.projects.remove(project)

        self.day += 1

        # Iterate over running projects
        for project in self.running_projects[:]:
            if project.tick(self.day):
                self.score += project.get_score(self.day)
                self.running_projects.remove(project)

    def write_output(self, file):
        with open(file, "w") as f:
            f.write("{}\n".format(str(len(self.solved_projects))))
            for project in self.solved_projects:
                f.write("{}\n".format(project.name))

                names = [person.name for person in project.persons]
                f.write(" ".join(names))
                f.write("\n")


def solve(persons, projects):
    solved_projects = []
    game = Game(projects, persons)

    while len(game.projects) != 0:
        game.tick()

    game.write_output("solution.txt")


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
