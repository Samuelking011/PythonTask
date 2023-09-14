import os
import git

repo = git.Repo.clone_from("git@github.com:AmujoDotun/quiz.git","task2_clone", branch="master")

if os.path.exists("task2_clone/src/main.js"):
    os.remove("task2_clone/src/main.js")
    print("main.js successfully removed")
else:
    print("main.js not found")

if os.path.exists("task2_clone/src/App.vue"):
    os.remove("task2_clone/src/App.vue")
    print("App.vue successfully removed")
else:
    print("App.vue not found")


