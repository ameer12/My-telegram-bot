import subprocess

def run_backlink():
    subprocess.run(["python", "backlink_generator.py"])

def run_ctr():
    subprocess.run(["python", "ctr_simulator.py"])

def run_indexing():
    subprocess.run(["python", "indexing_booster.py"])

def run_content():
    subprocess.run(["python", "content_spawner.py"])

def run_all():
    run_backlink()
    run_ctr()
    run_indexing()
    run_content()

if __name__ == "__main__":
    run_all()
