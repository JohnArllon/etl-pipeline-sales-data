## 🚀 Business Problem
Companies often have raw sales data that is inconsistent and difficult to analyze.

This pipeline transforms raw data into structured, analysis-ready datasets.

# 🚀 ETL Pipeline - Sales Data

## 📌 Overview

This project is a complete ETL (Extract, Transform, Load) pipeline built with Python.

It demonstrates how raw data can be transformed into structured data for analysis and decision-making.

---

## 🧠 Objective

* Extract raw sales data from CSV
* Clean and transform the data
* Load it into a database for analysis

---

## 🛠️ Tech Stack

* Python
* Pandas
* SQLAlchemy
* SQLite

---

## 📂 Project Structure

```
etl-pipeline-sales-data/
│
├── data/
│   ├── raw/
│   ├── processed/
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│
├── main.py
├── requirements.txt
```

---

## 🔄 Pipeline Steps

### 1. Extract

Reads raw data from CSV file

### 2. Transform

* Removes null values
* Converts data types
* Creates new columns (total = price * quantity)

### 3. Load

Stores cleaned data into SQLite database

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
python main.py
```

---

## 📊 Output

* Clean dataset stored in SQLite (`sales.db`)
* Ready for analysis and visualization

---

## 🚀 Future Improvements

* Automate pipeline execution
* Integrate with APIs
* Add data visualization (Power BI / Streamlit)

---

## 📸 Pipeline Execution

![Pipeline](assets/pipeline.png)

---

## 👨‍💻 Author

John Arllon Batista
[LinkedIn](https://www.linkedin.com/in/john-arllon-batista/)
