# HIT137_24S2_Group162

## Instructions
1. pull main branch >>> git pull main
2. create a branch >>> git checkout -b ${name}_${student_id}  // eg. git checkout -b James_S000001
3. write your code in the correct directory
4. stage you change >>> git add .
5. commit your change >>> git commit -m "Your code description"
6. push your code >>> git branch --set-upstream-to origin ${your branch name}  // eg. git branch --set-upstream-to origin James_S000001
7. enter your github branch and open a pull request
8. wait for the review

## How to keep your branch up to date and avoid conflicts
1. check main branch update: "git checkout main"
2. If your main branch has commits behind, please type: "git pull"
3. Then merge it into your branch, type "git switch {your branch name}" and "git merge main"
4. Solve conflicts if it warns that there are conflicts
