from git import Repo

#integrar git con python; hacer un commit cada vez que se copie la web;

# FUNCIONA EL repositorio desde python:
# https://blog.balasundar.com/automate-git-operations-using-python


import shutil
import os
import random
import string

directory_path = os.getcwd()
parent_path = os.path.abspath(os.path.join(directory_path, os.pardir))

print("My current directory is : " + directory_path)
print("Parent directory is : " + parent_path)

folder_name = os.path.basename(directory_path)
print("folder_name: " + directory_path)

src_path = directory_path + "\\_site"
dst_path = parent_path + "\\s.ln_blog_prod\\_site"

if os.path.exists(dst_path):
    shutil.rmtree(dst_path)

shutil.copytree(src_path, dst_path)

print('Copied')

repo = Repo(parent_path + '/s.ln_blog_prod')

# List all branches
for branch in repo.branches:
    print(branch)

def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

rand_commit_m = randomword(8)

# To checkout to a branch:
repo.git.checkout('master')

#add files
repo.git.add(all=True)

# Check differences between current files and last commit
diff = repo.git.diff(repo.head.commit.tree)
print(diff)

# Commit
repo.index.commit(rand_commit_m)