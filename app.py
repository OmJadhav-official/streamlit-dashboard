import streamlit as st
import mysql.connector
import pandas as pd

# 🔌 Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Pass@3457",
    database="daproject"
)
cursor = conn.cursor()

st.title("Food Donation Dashboard 🍽️")

# 📊 Define questions and queries
questions = [
    "1. Number of Providers by Type",
    "2. Number of Receivers by Type",
    "3. Most Listed Food Items",
    "4. Claims Status Distribution",
    "5. Claims per Receiver",
    "6. Listings per Provider",
    "7. Total Quantity of Food Listed",
    "8. Total Claims Made",
    "9. Providers by City",
    "10. Receivers by City",
    "11. Listings Over Time",
    "12. Claims Over Time",
    "13. Top Providers by Quantity",
    "14. Top Receivers by Claims",
    "15. Most Claimed Food Items"
]

query_list = [
    ("Result", "SELECT Type, COUNT(*) AS count FROM providers_data GROUP BY Type ORDER BY count DESC"),
    ("Result", "SELECT Type, COUNT(*) AS count FROM receivers_data GROUP BY Type ORDER BY count DESC"),
    ("Result", "SELECT Food_Name, COUNT(*) AS listings FROM food_listings_data GROUP BY Food_Name ORDER BY listings DESC"),
    ("Result", "SELECT Status, COUNT(*) AS count FROM claims_data GROUP BY Status"),
    ("Result", "SELECT Receiver_ID, COUNT(*) AS claims FROM claims_data GROUP BY Receiver_ID ORDER BY claims DESC"),
    ("Result", "SELECT Provider_ID, COUNT(*) AS listings FROM food_listings_data GROUP BY Provider_ID ORDER BY listings DESC"),
    ("Result", "SELECT SUM(Quantity) AS total_quantity FROM food_listings_data"),
    ("Result", "SELECT COUNT(*) AS total_claims FROM claims_data"),
    ("Result", "SELECT City, COUNT(*) AS providers FROM providers_data GROUP BY City"),
    ("Result", "SELECT City, COUNT(*) AS receivers FROM receivers_data GROUP BY City"),
    ("Result", "SELECT Expiry_Date, COUNT(*) AS listings FROM food_listings_data GROUP BY Expiry_Date ORDER BY Expiry_Date"),
    ("Result", "SELECT Timestamp, COUNT(*) AS claims FROM claims_data GROUP BY Timestamp ORDER BY Timestamp"),
    ("Result", "SELECT Provider_ID, SUM(Quantity) AS total_quantity FROM food_listings_data GROUP BY Provider_ID ORDER BY total_quantity DESC"),
    ("Result", "SELECT Receiver_ID, COUNT(*) AS total_claims FROM claims_data GROUP BY Receiver_ID ORDER BY total_claims DESC"),
    ("Result", "SELECT Food_ID, COUNT(*) AS claim_count FROM claims_data GROUP BY Food_ID ORDER BY claim_count DESC")
]


# 🧭 Create tabs for each question
tabs = st.tabs(questions)

for i in range(len(questions)):
    with tabs[i]:
        st.subheader(questions[i])
        for label, sql in [query_list[i]]:
            try:
                cursor.execute(sql)
                data = cursor.fetchall()
                columns = [desc[0] for desc in cursor.description]
                df = pd.DataFrame(data, columns=columns)
                st.dataframe(df)
            except Exception as e:
                st.error(f"Error executing query: {e}")

# ✅ Close connection
cursor.close()
conn.close()
