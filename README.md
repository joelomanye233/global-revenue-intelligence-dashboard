#  Global Revenue Intelligence Dashboard

An interactive, analytics-driven dashboard built with **Python and Streamlit** to analyze multi-year revenue performance across company branches.
Designed to mirror real-world financial and business intelligence workflows used in consulting, analytics, and finance teams.

---

##  Project Overview

The **Global Revenue Intelligence Dashboard** enables users to:

* Upload structured revenue datasets (CSV)
* Analyze performance across **branches, months, and years**
* Compare **actual vs. expected revenue**
* Identify **overperforming and underperforming branches**
* Visualize insights with modern, executive-ready charts

This project focuses on **data cleaning, analytics logic, and decision-making**, not just visualization.

---

##  Key Features

###  Revenue Performance Analysis

* Branch-level revenue aggregation
* Monthly and yearly filtering
* Automatic performance classification:

  * 🟢 Above Expected
  * 🟡 Meets Expected
  * 🔴 Below Expected

###  Interactive Visualizations

* Bar charts for branch comparisons
* Line charts for revenue trends over time
* Color-coded performance indicators
* KPI summary cards for executive insights

###  Scenario & Forecast Analysis

* User-defined **expected revenue input**
* Real-time recalculation of performance status
* Helps simulate planning and budgeting scenarios

---

##  Tech Stack

* **Python**
* **Streamlit** – interactive web dashboard
* **Pandas** – data cleaning and analytics
* **Plotly** – modern, interactive charts
* **NumPy** – numerical operations

---

##  Project Structure

```text
global-dashboard/
│
├── app.py               # Main Streamlit application
├── test_data.csv        # Sample dataset for testing
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## ▶️ How to Run Locally

### 1️⃣ Clone or Download the Repository

```bash
git clone https://github.com/YOUR_USERNAME/global-dashboard.git
cd global-dashboard
```

### 2️⃣ Open in VS Code

Open the folder in VS Code.

---

### 3️⃣ Install Dependencies

Open a new terminal in VS Code and run:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

---

### 4️⃣ Run the Application

```bash
python -m streamlit run app.py
```

The app will open automatically in your browser at:

```
http://localhost:8501
```

---

##  Sample Dataset Format

Your CSV file **must contain these columns**:

```text
Date,Branch,Revenue
2023-01-01,New York Branch,$120000
2023-01-01,Chicago Branch,$98000
2023-02-01,New York Branch,$135000
```

* **Date** → YYYY-MM-DD format
* **Branch** → Company branch name
* **Revenue** → Currency-formatted values

---

## 📌 Use Cases

* Financial performance analysis
* Branch-level KPI monitoring
* Budget planning & forecasting
* Business intelligence dashboards
* Portfolio project for data, analytics, and finance roles

---

## Resume-Ready Impact

* Built a production-style analytics dashboard with **end-to-end data workflow**
* Automated revenue performance analysis across **multi-year datasets**
* Applied real-world **expected vs. actual variance analysis**
* Delivered executive-ready insights through interactive visuals

---

##  Future Enhancements

* Inflation-adjusted revenue analysis
* Year-over-year growth metrics
* Export insights to CSV / PDF
* Authentication & role-based views
* Cloud deployment (Streamlit Cloud / AWS)

---

##  Contact

**Joel Omanye Thompson**
📧 [joelomanye23@gmail.com](mailto:joelomanye23@gmail.com)
🔗 [LinkedIn](https://www.linkedin.com/in/joel-thompson233/)

---

 *If you’re a recruiter or hiring manager, feel free to explore the dashboard locally or reach out for a walkthrough.*





