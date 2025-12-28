# Shared Folder Aging & Risk Identification System

## Business Problem
Shared folders in enterprise environments often accumulate inactive documents,
creating operational and compliance risk.

## Objective
Scan shared folders, identify PDF files, calculate the oldest modified date per folder,
and flag high-risk inactive folders.

## Technology Stack
- Python
- Pandas
- OS module
- DateTime

## How It Works
1. Traverse shared folders
2. Filter PDF files
3. Extract modified timestamps
4. Identify oldest modified date
5. Flag folders based on inactivity threshold

## Output
A CSV report containing:
- Folder name
- Oldest modified date
- Days inactive
- Risk flag

## AI Readiness
This solution is designed to evolve into an AI-based system by adding
machine learning models to predict inactivity trends.
