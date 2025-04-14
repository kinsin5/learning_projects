### Currently creating database in postgres

Below our schema we need to create SQL Database for that so we can easily import our data

![image](https://github.com/user-attachments/assets/7a47d158-8dae-4920-92ba-5b606c119fe8)

## Analyzing data with SQL with some CTE:
```sql
--Finding top 3 products in their category in sales
WITH prods AS (
    SELECT 
        p.product_id,
        p.product_category_name,
        ROUND(SUM(oi.price)) AS sales,
        ROW_NUMBER() OVER (PARTITION BY p.product_category_name ORDER BY SUM(oi.price) DESC) AS rn
    FROM products p
    JOIN order_items oi ON p.product_id = oi.product_id
    GROUP BY p.product_id, p.product_category_name
)

SELECT 
    pr.product_id,
    pt.product_category_name_english AS "Category",
    pr.sales AS "Sales",
	pr.rn AS "Rank"
FROM prods pr
JOIN product_category_name_translation pt
    ON pt.product_category_name = pr.product_category_name
WHERE pr.rn <= 3;
```
![image](https://github.com/user-attachments/assets/3b913d53-1a7b-4faf-b73f-94f0321f329c)
### Using some of Window functions
```sql
--Fiding best reviewed products
SELECT 
	pr.product_id,
	AVG(review_score) "Review Score",
	COUNT(pr.product_id) Reviews,
	RANK() OVER (PARTITION BY NULL ORDER BY AVG(review_score) DESC) as review_rank
 FROM products pr
JOIN order_items oi ON pr.product_id = oi.product_id
JOIN orders ord ON ord.order_id = oi.order_id
JOIN reviews rv ON ord.order_id = rv.order_id
GROUP BY pr.product_id
HAVING COUNT(pr.product_id) >= 50
ORDER BY review_rank ASC;
```

![image](https://github.com/user-attachments/assets/806574ce-aa38-4000-bb72-fdd464394565)
