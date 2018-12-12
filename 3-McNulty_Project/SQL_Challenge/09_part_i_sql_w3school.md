# Challenge Set 9
## Part I: W3Schools SQL Lab 

*Introductory level SQL*

--

This challenge uses the [W3Schools SQL playground](http://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all). Please add solutions to this markdown file and submit.   

1. Which customers are from the UK?
 ```sql
SELECT CustomerName FROM Customers
WHERE Country = 'UK';
```
Around the Horn   
B's Beverages   
Consolidated Holdings   
Eastern Connection   
Island Trading   
North/South   
Seven Seas Imports   

2. What is the name of the customer who has the most orders?
 ```sql
SELECT Customers.CustomerName, Orders.CustomerID, Count() AS CountVal FROM [Orders]
JOIN Customers ON Customers.CustomerID = Orders.CustomerID
GROUP BY Orders.CustomerID, Customers.CustomerName
ORDER BY CountVal DESC
```
Ernst Handel   

3. Which supplier has the highest average product price?
 ```sql
SELECT Suppliers.SupplierName, AVG(Products.Price) AS PriceAve FROM Products
JOIN Suppliers ON Suppliers.SupplierID = Products.SupplierID
GROUP BY Suppliers.SupplierID
ORDER BY PriceAve DESC
LIMIT 1;
```
Aux joyeux ecclésiastiques	($140.75)   

4. How many different countries are all the customers from? (*Hint:* consider [DISTINCT](http://www.w3schools.com/sql/sql_distinct.asp).)
 ```sql
 SELECT DISTINCT Country FROM [Customers]     
 ```
 21   
 
5. What category appears in the most orders?
 ```sql
 SELECT CategoryName, Count(OrderDetails.OrderID) AS Cnt
FROM
	Categories
    JOIN Products ON Categories.CategoryID = Products.CategoryID
    JOIN OrderDetails ON OrderDetails.ProductID = Products.ProductID
GROUP BY CategoryName
ORDER BY Cnt DESC
LIMIT 1;
```
Dairy Products (100) 

6. What was the total cost for each order?
 ```sql
SELECT Orders.OrderID, SUM(OrderDetails.Quantity*Products.Price) AS Cost
FROM
	Orders
    JOIN Products     ON OrderDetails.OrderID = Orders.OrderID
    JOIN OrderDetails ON OrderDetails.ProductID = Products.ProductID
GROUP BY Orders.OrderID
ORDER BY Cost DESC;
```
Several records   

7. Which employee made the most sales (by total cost)?
 ```sql
SELECT Employees.FirstName, Employees.LastName,
    SUM(OrderDetails.Quantity*Products.Price) AS Cost
FROM
	Employees
    JOIN Orders       ON Orders.EmployeeID = Employees.EmployeeID
    JOIN OrderDetails ON OrderDetails.OrderID = Orders.OrderID
    JOIN Products     ON OrderDetails.ProductID = Products.ProductID
GROUP BY Employees.EmployeeID
ORDER BY Cost DESC
LIMIT 1;
```
Margaret Peacock ($105,696.50)   

8. Which employees have BS degrees? (*Hint:* look at the [LIKE](http://www.w3schools.com/sql/sql_like.asp) operator.)
```sql
SELECT * FROM [Employees]
WHERE Notes LIKE '%BS%'
```
Janet Leverling   
Steven Buchanan 

9. Which supplier of three or more products has the highest average product price? (*Hint:* look at the [HAVING](http://www.w3schools.com/sql/sql_having.asp) operator.)
 ```sql
SELECT SupplierName, COUNT(Products.SupplierID), AVG(Products.Price) AS AvePrice
FROM
	Suppliers
    JOIN Products     ON Suppliers.SupplierID = Products.SupplierID
GROUP BY SupplierName
HAVING COUNT(Products.SupplierID) >= 3;
```
Tokyo Traders ($46) 
