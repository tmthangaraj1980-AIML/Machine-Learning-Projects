# 🌍 Country Development Analysis using Hierarchical Clustering

## 📌 Project Overview

This project applies **Hierarchical Agglomerative Clustering** to group countries based on their socio-economic indicators. The objective is to identify countries with similar development characteristics, enabling governments and international organizations to make informed policy and investment decisions.

Unlike K-Means, Hierarchical Clustering does not require predefined centroids. Instead, it builds a hierarchy of clusters using a dendrogram, making it easier to determine the optimal number of clusters.

---

# 🎯 Problem Statement

Governments and international organizations need to identify countries with similar socio-economic conditions to design effective development policies.

Instead of manually analyzing numerous indicators across many countries, Hierarchical Clustering automatically groups countries based on their similarities.

---

# 📂 Dataset

**Dataset Name:** Country-data.csv

The dataset contains socio-economic and health indicators for countries around the world.

### Features

- Country
- Child Mortality
- Exports
- Health Expenditure
- Imports
- Income
- Inflation
- Life Expectancy
- Total Fertility
- GDP per Capita

---

# 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- SciPy
- Jupyter Notebook
- VS Code

---

# 📊 Exploratory Data Analysis (EDA)

The following analyses were performed:

- Dataset Overview
- Missing Value Analysis
- Duplicate Value Check
- Statistical Summary
- Histograms
- Boxplots
- Correlation Heatmap

---

# ⚙️ Data Preprocessing

- Selected numerical features
- Removed country name before clustering
- Standardized features using StandardScaler

---

# 🌳 Hierarchical Clustering

The project uses:

- Agglomerative Hierarchical Clustering
- Ward Linkage
- Euclidean Distance

A dendrogram was used to determine the optimal number of clusters.

---

# 📈 Results

The model grouped countries into **three meaningful clusters**:

### 🔹 Cluster 0 – Developed Countries

- High Income
- High GDP per Capita
- High Life Expectancy
- Low Child Mortality

---

### 🔹 Cluster 1 – Developing Countries

- Moderate Income
- Moderate GDP
- Improving Healthcare
- Moderate Child Mortality

---

### 🔹 Cluster 2 – Underdeveloped Countries

- Low Income
- Low GDP per Capita
- High Child Mortality
- Low Life Expectancy

---

# 💼 Business Insights

The clustering results can help:

- Identify countries requiring economic assistance.
- Support healthcare planning.
- Assist international organizations in resource allocation.
- Compare countries with similar socio-economic conditions.
- Support evidence-based policy decisions.

---

# 📁 Project Structure

```
Country_Development_Analysis_Hierarchical_Clustering/

│── Country_Development_Analysis_Hierarchical_Clustering.ipynb
│── Country-data.csv
│── README.md
│── requirements.txt
```

---

# ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/Country_Development_Analysis_Hierarchical_Clustering.git
```

Navigate to the project folder:

```bash
cd Country_Development_Analysis_Hierarchical_Clustering
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

### Windows

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
source venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Launch Jupyter Notebook:

```bash
jupyter notebook
```

---

# 🚀 Future Improvements

- PCA-based Cluster Visualization
- Silhouette Score Evaluation
- Interactive Dashboard
- Comparison with K-Means and DBSCAN
- Deployment using Streamlit

---

# 👨‍💻 Author

**Thangaraj**

AI/ML Engineer Aspirant

Building real-world Machine Learning projects with Python and Scikit-learn.

---

⭐ If you found this project useful, consider giving it a star!