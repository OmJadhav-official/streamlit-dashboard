import streamlit as st
import mysql.connector
import pandas as pd
import plotly.express as px

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

        # 🔹 Chart: Providers by Type
        if questions[i] == "1. Number of Providers by Type":
            cursor.execute(query_list[i][1])
            data = cursor.fetchall()
            df = pd.DataFrame(data, columns=["Type", "Count"])
            st.dataframe(df)
            st.bar_chart(df.set_index("Type"))

        # 🔹 Chart: Claims Status Distribution
        elif questions[i] == "4. Claims Status Distribution":
            cursor.execute(query_list[i][1])
            data = cursor.fetchall()
            df = pd.DataFrame(data, columns=["Status", "Count"])
            st.dataframe(df)
            fig = px.pie(df, names="Status", values="Count", title="Claims Status Distribution")
            st.plotly_chart(fig, use_container_width=True)

        # 🔹 Filter: Claims Over Time
        elif questions[i] == "12. Claims Over Time":
            date_range = st.date_input("Select date range", [])
            query = "SELECT Timestamp, COUNT(*) AS claims FROM claims_data"
            if date_range and len(date_range) == 2:
                query += f" WHERE Timestamp BETWEEN '{date_range[0]}' AND '{date_range[1]}'"
            query += " GROUP BY Timestamp ORDER BY Timestamp"
            cursor.execute(query)
            data = cursor.fetchall()
            df = pd.DataFrame(data, columns=["Date", "Claims"])
            st.line_chart(df.set_index("Date"))

        # 🔹 Filter: Receivers by City
        elif questions[i] == "10. Receivers by City":
            cursor.execute("SELECT DISTINCT City FROM receivers_data")
            cities = [row[0] for row in cursor.fetchall()]
            selected_city = st.selectbox("Select City", ["All"] + cities)
            query = "SELECT City, COUNT(*) AS receivers FROM receivers_data"
            if selected_city != "All":
                query += f" WHERE City = '{selected_city}'"
            query += " GROUP BY City"
            cursor.execute(query)
            data = cursor.fetchall()
            df = pd.DataFrame(data, columns=["City", "Receivers"])
            st.dataframe(df)

        # 🔹 Default: Table view
        else:
            label, sql = query_list[i]
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
