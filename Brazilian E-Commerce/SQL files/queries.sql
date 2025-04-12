--Query to find english category and count of products from them
SELECT product_category_name_english, p_gr.count
 FROM product_category_name_translation as pt
JOIN (
	SELECT product_category_name, COUNT(product_id) as "count" 
	 FROM products
	GROUP BY product_category_name) as p_gr 
ON pt.product_category_name = p_gr.product_category_name
ORDER BY count DESC;

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