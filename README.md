# Streamlit-Dashboard for Data Analysis

This project showcases an interactive dashboard built with Streamlit and Python, powered by SQL queries from a MySQL database. It visualizes insights using dynamic charts and filters.

## Features
- 15+ SQL queries across multiple tables
- Interactive filters for user-driven analysis
- Plotly charts for visual storytelling
- Modular code structure with `app.py` and `app2.py`

## Tools Used
- Python
- Streamlit
- MySQL
- Plotly
- Pandas

# 🥗 Food Donation Dashboard with Streamlit & SQL

This project presents a data-driven dashboard for managing and analyzing food donations using Python, Streamlit, and MySQL. It enables food providers and receivers to coordinate effectively, reduce wastage, and improve distribution through interactive visualizations and SQL-powered insights.

---

## 🚀 Project Overview

The dashboard is built to:
- Analyze food donation patterns across cities and providers.
- Track claims and distribution efficiency.
- Provide real-time filtering and contact access for coordination.
- Support CRUD operations for managing food listings.

---

## 📊 Approach & Workflow

### 1. Data Preparation
- Cleaned and structured datasets containing food donation records.
- Ensured consistency in formatting and schema alignment.

### 2. Database Creation
- Stored data in MySQL tables for providers, receivers, food listings, and claims.
- Implemented CRUD operations to update, add, and remove records.

### 3. Data Analysis
- Executed 15+ SQL queries to uncover trends in food wastage, availability, and claims.
- Generated insights for better food distribution strategies.

### 4. Application Development
- Built a Streamlit-based interface to:
  - Display results of all SQL queries.
  - Filter data by city, provider, food type, and meal type.
  - Show contact details for direct coordination.

### 5. Deployment
- Deployed the Streamlit app for real-time interaction and accessibility.

---

## 🧱 Data Architecture

### 📦 Data Storage
- MySQL database with structured tables for:
  - Providers
  - Receivers
  - Food Listings
  - Claims

### 🔄 Processing Pipeline
- SQL queries for trend analysis and reporting.
- Python for data handling and visualization.

### 🖥️ Deployment
- Streamlit app for user interaction and dashboard display.

---

## 📁 Datasets Used

| Dataset Name         | Description                                                                 |
|----------------------|-----------------------------------------------------------------------------|
| `providers_data.csv` | Details of food providers (ID, name, type, city, contact)                   |
| `receivers_data.csv` | Details of food receivers (ID, name, type, city, contact)                   |
| `food_listings_data.csv` | Available food items (ID, name, quantity, expiry, location, type, meal) |
| `claims_data.csv`    | Food claims made by receivers (ID, food ID, receiver ID, status, timestamp) |

---

## ❓ Key Questions Answered

### 🏢 Providers & Receivers
- How many providers and receivers are in each city?
- Which provider type contributes the most food?
- Who are the top receivers based on claims?

### 🍽️ Food Listings
- What is the total quantity of food available?
- Which city has the most listings?
- What are the most common food types?

### 📦 Claims & Distribution
- How many claims per food item?
- Which provider has the most successful claims?
- What percentage of claims are completed vs. pending vs. canceled?

### 📈 Insights
- Average quantity claimed per receiver.
- Most claimed meal type.
- Total food donated by each provider.

---

## ✅ Results

- Fully functional Streamlit dashboard with:
  - Filters by location, provider, food type, and meal type.
  - Contact details for coordination.
  - CRUD operations for food listings and claims.
  - Display of all 15 SQL queries and their outputs.

- SQL-powered analysis revealing:
  - Top contributing providers.
  - High-demand cities.
  - Trends in food wastage and distribution.

---

## 📐 Evaluation Metrics

- Completeness of SQL database.
- Accuracy of SQL queries.
- Functionality of CRUD operations.
- User-friendliness of the Streamlit interface.

---

## 🛠️ Tech Stack

| Category         | Tools / Technologies                          |
|------------------|-----------------------------------------------|
| Programming      | Python                                        |
| Data Analysis    | SQL (MySQL), Pandas                           |
| Visualization    | Streamlit, Plotly                             |
| Dashboarding     | Streamlit                                     |
| Version Control  | Git, GitHub                                   |

---

## 📦 Deliverables

- Cleaned and structured datasets.
- SQL queries for trend analysis.
- Streamlit dashboard for interactive exploration and reporting.

---

## 📌 Tags

`Python` `SQL` `Streamlit` `Data Analysis` `Food Management` `Dashboard` `MySQL`

---

## 📸 Screenshots (Optional)

You can add screenshots of your dashboard here once uploaded.

---

## 🙌 Acknowledgments

Built with passion to reduce food wastage and improve distribution efficiency. Inspired by real-world challenges in food logistics and community support.

