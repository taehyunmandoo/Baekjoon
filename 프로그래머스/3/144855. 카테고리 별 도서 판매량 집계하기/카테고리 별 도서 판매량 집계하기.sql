SELECT A.category, SUM(B.sales)
FROM book A JOIN book_sales B
ON A.book_id = B.book_id
WHERE DATE_FORMAT(B.sales_date, '%Y-%m') = '2022-01'
GROUP BY A.category
ORDER BY A.category