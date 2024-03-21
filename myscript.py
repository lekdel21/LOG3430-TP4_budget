import os

def run_command(command):
    return os.popen(command).read().strip()

def start_bisect(bad_revision, good_revision):
    os.system(f"git bisect start {bad_revision} {good_revision}")

def run_bisect():
    os.system(f"git bisect run python manage.py test")

# Main
if __name__ == "__main__":
    bad_revision = "c1a4be04b972b6c17db242fc37752ad517c29402"
    good_revision = "e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c"

    start_bisect(bad_revision, good_revision)
    run_bisect()