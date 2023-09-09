## Comands

### Initializate Git 

```git
git init
```

### Tracking the changes

```git
git status
```

### Adding files to stage area

```git
git add 'file_name'
```

### Adding commit with a comment message

```git
git commit -m "comment message"
```

### Verify all commits

```git
git log
```

### Adding all unstage files to stage area

```git
git add .
``` 

### Verify the modifications in a file

```git
git diff "name_file"
``` 

### Rollback the previus version of a file

```git
git checkout "name_file"
``` 

### Link local repository to remote repository

```git
git remote add <name> <url>
``` 

### Send every change in local repository to remote repository

```git
git push -u <remove name> <branch name>
``` 

### Get exacly project files from the remote repository to local

```git
git clone <url>
``` 

### See all branch exists in project repository

```git
git branch
``` 

### Create a new branch using the actual branch

```git
git branch <name>
``` 

### Switch to a branch

```git
git checkout <branch name>
``` 


### Merging a branch with his origin branch

```git
git merge <branch name>
``` 