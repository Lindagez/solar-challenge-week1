# Building a Lightweight, Insightful GHI Dashboard with Streamlit

Author: <Your Name>  
Repo: <GitHub URL to main branch>  
Live Demo (optional): Streamlit Community Cloud link

> _In this short read, I’ll walk through how I took a CSV of country‑level GHI metrics and turned it into an interactive dashboard that surfaces regional patterns in minutes._

## Why Streamlit for Week 0?
Fast dev, zero boilerplate UI, and a tight feedback loop. The focus stayed on data quality, not pixel‑perfect CSS.

## Data In, Insights Out
- Input: CSV in data/ with country, region, and numeric metrics (e.g., GHI).
- Cleaning: normalize column names; validate required fields; flag missing or implausible values.
- Profiling: df.info(), df.describe(), unique counts by region/country.

## Interactive Elements
- Filters: multiselect regions and countries
- Metrics: choose any numeric column (GHI by default)
- Charts: box/violin/histogram/bar (Plotly)
- Table: Top regions by mean with count/median/std
- Export: download button for the filtered slice

## What I Learned
- Schema validation early prevents broken charts
- Small UX wins (defaults, caching, downloads) improve usability
- Git discipline (tiny PRs) accelerates reviews

## What’s Next
- Country/region ISO normalization and mapping
- CI (lint/test) via GitHub Actions
- Theming and saved filter presets

## Screenshot(s)
![Dashboard](../dashboard_screenshots/screenshot.png)

## How to Run
See README for quickstart.

---

Export: Print to PDF from your browser or use Markdown → PDF tool and upload the PDF to your repo for submission.
