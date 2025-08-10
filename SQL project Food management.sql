use daproject;
select * from claims_data;
select * from food_listings_data;
select * from providers_data;
select * from receivers_data;

-- Q.1 How many food providers and receivers are there in each city?
-- For providers
SELECT
  TRIM(BOTH '"' FROM City) AS City,
  COUNT(*) AS providers_count
FROM providers_data
GROUP BY TRIM(BOTH '"' FROM City)
ORDER BY City;

-- For receivers
SELECT
  City,
  COUNT(*) AS receivers_count
FROM receivers_data
GROUP BY City
ORDER BY City;


# Q.2 Which type of food provider contributes the most food?
SELECT
  fl.Provider_Type,
  SUM(fl.Quantity) AS total_quantity
FROM food_listings_data AS fl
GROUP BY fl.Provider_Type
ORDER BY total_quantity DESC
LIMIT 1;


# Q.3 What is the contact information of food providers in a specific city?        i chose 'Lake Andrewmouth' city here 
SELECT
TRIM(BOTH '"' FROM City) AS City,
TRIM(BOTH '"' FROM Name) AS Name,
TRIM(BOTH '"' FROM Type) AS Provider_Type,
TRIM(BOTH '"' FROM Contact) AS Contact
FROM providers_data
WHERE LOWER(TRIM(BOTH '"' FROM City)) = LOWER('Lake Andrewmouth')
ORDER BY Name;


# Q.4 Which receivers have claimed the most food?
-- i chose top 5 receivers here you can get top 10 if you want
SELECT
  r.Receiver_ID,
  r.Name AS receiver_name,
  r.Type AS receiver_type,
  r.City AS receiver_city,
  COUNT(*) AS completed_claims
FROM claims_data AS c
JOIN receivers_data AS r
  ON r.Receiver_ID = c.Receiver_ID
WHERE c.Status = 'Completed'
GROUP BY r.Receiver_ID, r.Name, r.Type, r.City
ORDER BY completed_claims DESC
LIMIT 5;


# Q.5 What is the total quantity of food available from all providers?
SELECT SUM(Quantity) AS total_quantity_available
FROM food_listings_data;


# Q.6 Which city has the highest number of food listings?
SELECT
  Location AS City,
  COUNT(*) AS listings_count
FROM food_listings_data
GROUP BY Location
ORDER BY listings_count DESC
LIMIT 1;


# Q.7 What are the most commonly available food types?
SELECT
  Food_Name,
  COUNT(*) AS listings_count
FROM food_listings_data
GROUP BY Food_Name
ORDER BY listings_count DESC, Food_Name ASC
LIMIT 10;


# Q.8 How many food claims have been made for each food item?
# here Im considering 'completed' claims as claims  (Tip- Just remove WHERE clause from syntax to get Pending+completed+cancelled claims value)
SELECT
fl.Food_Name,
COUNT(*) AS successful_claims_count
FROM claims_data AS c
JOIN food_listings_data AS fl
ON fl.Food_ID = c.Food_ID
WHERE c.Status = 'Completed'
GROUP BY fl.Food_Name
ORDER BY successful_claims_count DESC, fl.Food_Name; 


# Q.9 Which provider has had the highest number of successful food claims?
SELECT
p.Provider_ID,
p.Name AS provider_name,
p.Type AS provider_type,
COUNT(*) AS successful_claims
FROM claims_data AS c
JOIN food_listings_data AS fl
ON fl.Food_ID = c.Food_ID
JOIN providers_data AS p
ON p.Provider_ID = fl.Provider_ID
WHERE c.Status = 'Completed'
GROUP BY p.Provider_ID, p.Name, p.Type
ORDER BY successful_claims DESC
LIMIT 1;


# Q.10 What percentage of food claims are completed vs. pending vs. canceled?
SELECT
Status,
COUNT(*) AS cnt,
ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM claims_data), 2) AS pct
FROM claims_data
GROUP BY Status
ORDER BY cnt DESC;


# Q.11 What is the average quantity of food claimed per receiver?    (Again taken status- completed here)
WITH per_receiver AS (
SELECT
c.Receiver_ID,
r.Name AS receiver_name,
SUM(fl.Quantity) AS total_qty_claimed
FROM claims_data c
JOIN food_listings_data fl ON fl.Food_ID = c.Food_ID
JOIN receivers_data r ON r.Receiver_ID = c.Receiver_ID
WHERE c.Status = 'Completed'
GROUP BY c.Receiver_ID, r.Name
)
SELECT
ROUND(AVG(total_qty_claimed), 2) AS avg_quantity_claimed_per_receiver
FROM per_receiver;


# Q.12 Which meal type (breakfast, lunch, dinner, snacks) is claimed the most?
SELECT
fl.Meal_Type,
COUNT(*) AS completed_claims
FROM claims_data c
JOIN food_listings_data fl ON fl.Food_ID = c.Food_ID
WHERE c.Status = 'Completed'
GROUP BY fl.Meal_Type
ORDER BY completed_claims DESC;


# Q.13 What is the total quantity of food donated by each provider?
SELECT
Provider_ID,
SUM(Quantity) AS total_quantity_donated
FROM food_listings_data
GROUP BY Provider_ID
ORDER BY total_quantity_donated DESC;

# Q.14 Q13) Which cities have the highest total quantity successfully claimed?
SELECT
fl.Location AS City,
SUM(fl.Quantity) AS total_quantity_claimed
FROM claims_data c
JOIN food_listings_data fl
ON fl.Food_ID = c.Food_ID
WHERE c.Status = 'Completed'
GROUP BY fl.Location
ORDER BY total_quantity_claimed DESC, City ASC
LIMIT 10;


# Q.15 How many listings are there per provider type?
SELECT Provider_Type, COUNT(*) AS listings_count
FROM food_listings_data
GROUP BY Provider_Type
ORDER BY listings_count DESC;