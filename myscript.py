import os

def run_command(command):
    return os.popen(command).read().strip()

def start_bisect(bad_revision, good_revision):
    os.system(f"git bisect start {bad_revision} {good_revision}")

def run_bisect():
    os.system(f"git bisect run python manage.py test")

# Main
if __name__ == "__main__":
    bad_revision = input("Entrez la révision mauvaise : ")
    good_revision = input("Entrez la révision bonne : ")

    start_bisect(bad_revision, good_revision)
    run_bisect()