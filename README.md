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
