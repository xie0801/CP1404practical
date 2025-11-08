"""
CP1404/CP5632 Practical
project_management.py
Read and manage a list of software projects.
"""

from project import Project


def load_projects(filename):
    """Load projects from a file and return a list of Project objects."""
    projects = []
    with open(filename, "r") as in_file:
        in_file.readline()  # Skip header line
        for line in in_file:
            parts = line.strip().split('\t')
            name = parts[0]
            start_date = parts[1]
            priority = int(parts[2])
            cost_estimate = float(parts[3])
            completion_percentage = int(parts[4])
            project = Project(name, start_date, priority, cost_estimate, completion_percentage)
            projects.append(project)
    return projects


def display_projects(projects):
    """Display incomplete and complete projects, sorted by priority."""
    incomplete = [p for p in projects if not p.is_complete()]
    complete = [p for p in projects if p.is_complete()]

    print("Incomplete projects:")
    for project in sorted(incomplete):
        print(f"  {project}")

    print("Complete projects:")
    for project in sorted(complete):
        print(f"  {project}")


def add_new_projects():
    """Prompt user to enter new projects, return as list of Project objects."""
    new_projects = []
    print("\nAdd new projects (leave name empty to finish):")
    while True:
        name = input("Name: ")
        if not name:
            break
        start_date = input("Start date (dd/mm/yyyy): ")
        try:
            priority = int(input("Priority: "))
            cost_estimate = float(input("Cost estimate: $"))
            completion_percentage = int(input("Percent complete: "))
            new_project = Project(name, start_date, priority, cost_estimate, completion_percentage)
            new_projects.append(new_project)
        except ValueError:
            print("Invalid input. Skipping this entry.")
    return new_projects


def save_projects(filename, projects):
    """Save a list of Project objects to a file."""
    with open(filename, "w") as out_file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
        for project in projects:
            print(f"{project.name}\t{project.start_date}\t{project.priority}"
                  f"\t{project.cost_estimate}\t{project.completion_percentage}", file=out_file)


def main():
    """Main entry point of the project management program."""
    filename = "projects.txt"
    projects = load_projects(filename)
    print("Projects loaded.\n")
    display_projects(projects)

    new_projects = add_new_projects()
    if new_projects:
        projects.extend(new_projects)
        print("\nNew projects added.")
        display_projects(projects)
        save_projects(filename, projects)
        print(f"\nProjects saved to {filename}.")


if __name__ == '__main__':
    main()
