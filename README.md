# AutoFIleCreation
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
