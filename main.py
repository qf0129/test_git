from git import Repo
import os


root_dir = os.getcwd()

print root_dir
repo = Repo(root_dir)

master_last_commit = repo.heads.master.repo.iter_commits().next()

diffs = repo.index.diff(master_last_commit)
for d in diffs:
    print d.change_type, d.a_path

import pdb;pdb.set_trace()

print 123

