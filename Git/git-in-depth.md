# Git In Depth

`git clone <URL>`

1. What: Copies repository from remote location to local machine.
2. Why: So you can have a working copy offline, and also if you aren't doing branching, you can test out changes to code without messing up the "stable" code.
3. How: I'm not actually sure the mechanics of it, but I know it copies a folder with the repository into the directory you are at in the CLI, so you don't need an extra folder first, and you can use different ways to do it, including URLs and SSH if that is set up.

`git add .` or `git add <filepath>`

1. What: Add all files with changes (add .) or a single file/folder to the list of things to send back to the remote repository with a `git push <origin> <branch>`.
2. Why: You are confident this code is (currently) at a stable state (especially if going to main), or you want to make sure your branch changes get backed up off your local machine so you still save all your work even if something happens to your local machine.
3. How: Again, didn't really retain specifics, but I think it essential checks the state of the last pushed file against how it currently is and adds only the changes to the file, not replacing the entire file.
4. Notes: Any added files will get the same commit notes, so don't batch send if you want to document individual file changes with commit messages.

`git commit -m "Message"`

1. What: Attaches a message to all the added files.
2. Why: So you know what was changed most recently in the file. Ideally don't batch send commit messages.
3. How: Again, not sure.

`git push <origin> <branch>`

1. What: Pushes all the stages files from `git add` back to the remote repository.
2. Why: So you don't lose those changes if something happens to your local machine.
3. How: Magic
