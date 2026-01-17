# AutoFIleCreation
<<<<<<< HEAD
A simple Python script that creates automated files every 1st of the month with the name of the month and sub files with A-Z files

I created it for a company I used to work for. We kept our clients' documents in files every month, and it took a significant amount of time to manually create folders for each month and letter when the month ended.
Please feel free to use it and contribute it if you'd like.


run:
  -Clone the repo
  -cd AutoFileCreation
  -Python CreateFolders.py

Run with Docker:
  docker pull alexanrosmo/CreateFile:latest
  docker run CreateFile:latest
=======
A simple Python script that automatically creates folders for each month and subfolders A-Z, intended to run every 1st of the month.

I originally created this for a company i worked for, where we needed to organize client documents by month. Manually creating folders for each month and letter at the end of the month took too much time.

##Run locally

1.Clone the repo:

```bash
git clone https://github.com/AlexandrosMo/AutoFIleCreation.git
cd AutoFileCreation
```
2. Activate your virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate
.venv\Scripts\activate #for Windows
```
3.Run the script:

```bash
python CreateFolders.py

---

###Run With Docker
```
1. Pull the image
```bash

docker pull alexandrosmo/createfiles:latest
```
2. Run the container:
```bash
docker run alexandrosmo/createfiles:latest

```

thank you for your time.
>>>>>>> 84de515 (Readme changes)
