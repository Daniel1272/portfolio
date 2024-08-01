/* --------------------
   Case Study Questions
   --------------------*/

-- 1. What is the total sales amount by month?
-- 2. Which products are the most popular by revenue?
-- 3. Which products are the most popular by quantity sold?
-- 4. Who are the most valuable customers (by total purchase amount)?
-- 5. Which employees generate the highest revenue?
-- 6. What is the average order value by customer?

-- 1. What is the total sales amount by month?
select TO_CHAR(order_date, 'YYYY-MM') AS month,
sum((unit_price-(unit_price*discount)) * quantity) as sales
from orders
join order_details using(order_id)
group by month
order by month

-- 2. Which products are the most popular by revenue?
select product_name,
sum((order_details.unit_price-(order_details.unit_price*discount)) * quantity) as TotalProductSales
from products
join order_details using(product_id)
group by product_id
order by TotalProductSales Desc

-- 3. Which products are the most popular by quantity sold?
select product_name,
sum(quantity) as TotalQuantitySold
from products
join order_details using(product_id)
group by product_id
order by TotalQuantitySold Desc

-- 4. Who are the most valuable customers (by total purchase amount)?
select company_name,
sum((unit_price-(unit_price*discount)) * quantity) as TotalProductSales
from customers
join orders using(customer_id)
join order_details using(order_id)
group by customer_id 
order by TotalProductSales desc

-- 5. Which employees generate the highest revenue?
select employee_id,first_name,last_name,
sum((unit_price-(unit_price*discount)) * quantity) as TotalProductSales
from employees 
join orders using (employee_id)
join order_details using (order_id)
group by employee_id
order by TotalProductSales desc

-- 6. What is the average order value by customer?

select customer_id,company_name,
avg(quantity*(unit_price-(unit_price*discount))) as Avg_Order_Value
from order_details
join orders using (order_id)
join customers using (customer_id)
group by customer_id,company_name
order by customer_id



