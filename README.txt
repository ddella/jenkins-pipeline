# New GitHub repo
Make sure the directory `jenkins-pipeline` doesn't exist. Step 3 will create the local directory.

1. Use the web interface an GitHub and create the repo:
2. cd ~/Training/Kubernetes/debian11-k8s-cluster/Jenkins/
3. git clone https://github.com/ddella/jenkins-pipeline
4. cd jenkins-pipeline

# *** Sync files *** from ~/Training/SSL-TLS/Git-OpenSSL-Cheatsheet/OpenSSL
git add --all
git commit -m "Initial commit"
git push -u origin main

# If you get this error:
# Updates were rejected because the tip of your current branch is behind
git push -f

# Remove .DS_Store
git rm --cached -f .DS_Store
---------------------------------------------------
