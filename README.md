# Data Engineering I - project
University project for Data Engineering I course. The project aims to apply our
knowledge gained during the course and create a scalable data engineering solution needed for analyzing
the dataset.
### Data set
We have chosen Reddit's comment data set which can be found [here](https://files.pushshift.io/reddit/comments/). It consists of comments stored in JSON format. 
### Questions we want to answer
Using our solution we would like to answer 5 following questions:
- What are the most frequently used words?
- Does majority of the comments have positive or negative sentiment? 
- How does the trend regarding the subredits change ? 
- ... 
### How to work with this repo
These are general guidlines the most important are first three. I think four and five wont be very handy as I do not think there would be a lot of merge conflicts. 
1. Commit frequently as we will host the code on the remote server that can crush.
2. There should be one branch for code that creates spark cluster. 
3. Create one branch per question so we can easily merged all code with minimized amount of conflicts. Use `checkout -b <new-branch-name>` to create branch locally and when pushing create corespondent branch on the remote with command `git push -u origin <new-branch-name>`. Merging can be done via the web Github UI. 
4. Remeber to keep commit messages clean and consice. 
5. We can merge our own branches, however if there are conflicts and we are not sure how to handle those then we should talk to someone.

P.S. Very usefull command is `git stash` that saves any changes in local stash and reverts back to last commit so you have clean working tree, and `git stash apply` to bring back previously backed-up changes.    
