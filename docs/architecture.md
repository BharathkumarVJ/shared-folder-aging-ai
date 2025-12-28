# Solution Architecture

## Overview
This solution scans shared folders to identify inactive PDF documents and
generate a folder aging risk report.

## Flow
1. Input: Shared folder path
2. Processing: Scan subfolders and PDF files
3. Logic: Identify oldest modified date per folder
4. Output: CSV report with risk classification
5. Future: ML model for predictive risk analysis

## Deployment
- Scheduled batch job
- Central server execution
- Dashboard integration

