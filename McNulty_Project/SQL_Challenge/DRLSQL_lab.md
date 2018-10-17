# SQL Lab

_Structured Query Language_ (SQL) is a useful [declarative language](http://en.wikipedia.org/wiki/Declarative_programming) for working with data. It is usually supported (with some variation) by relational databases. The tutorialspoint [SQL Quick Guide](http://www.tutorialspoint.com/sql/sql-quick-guide.htm) is a handy cheat sheet for a lot of the syntax. As a data user, access to data will usually consist of a more or less complicated `SELECT` statement.

For joining data with SQL, this [Visual Explanation of SQL Joins](http://blog.codinghorror.com/a-visual-explanation-of-sql-joins/) is quite good. One thing to note is that "join" will also often be known as "merge" in statistical software.

This lab uses the SQL playground provided in-browser by [W3Schools](http://www.w3schools.com/). Click [W3Schools SQL playground](http://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all) to go straight to the playground.

This is a pre-populated data environment with nothing to install and no risk of breaking anything. The data there is from a commonly-used example database ([info](http://northwinddatabase.codeplex.com/)). Nice!


## Guided

Let's walk through a few examples:

1) Retrieve all Customers from Madrid

```sql
SELECT
    * 
FROM
    Customers
WHERE
    City='Madrid';
```

2) How many customers are there in each city?

```sql
SELECT
    City, COUNT(*)
FROM
    Customers
GROUP BY
    City;
```

3) What is the most common city for customers? (And can you make it easy to find the correct answer?)

```sql
SELECT
    City, COUNT(*) AS count 
FROM
    Customers 
GROUP BY
    City 
ORDER BY
    count DESC;
```

4) What category has the most products?

```sql
SELECT * FROM Products
JOIN Categories ON Products.CategoryID = Categories.CategoryID

SELECT CategoryName, Count(*) AS CountVal FROM Products
JOIN Categories ON Products.CategoryID = Categories.CategoryID
GROUP BY CategoryName

SELECT CategoryName, Count(*) AS CountVal FROM Products
JOIN Categories ON Products.CategoryID = Categories.CategoryID
GROUP BY CategoryName
ORDER BY CountVal DESC
```

You can comment in SQL by using /* and */

## Practice

 * Which customers are from the UK?
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

 * What is the name of the customer who has the most orders?
 ```sql
SELECT Customers.CustomerName, Orders.CustomerID, Count() AS CountVal FROM [Orders]
JOIN Customers ON Customers.CustomerID = Orders.CustomerID
GROUP BY Orders.CustomerID, Customers.CustomerName
ORDER BY CountVal DESC
```
Ernst Handel   

 * Which supplier has the highest average product price?
 ```sql
SELECT Suppliers.SupplierName, AVG(Products.Price) AS PriceAve FROM Products
JOIN Suppliers ON Suppliers.SupplierID = Products.SupplierID
GROUP BY Suppliers.SupplierID
ORDER BY PriceAve DESC
LIMIT 1;
```
Aux joyeux ecclésiastiques	($140.75)    
 * How many different countries are all the customers from? (*Hint:* consider [DISTINCT](http://www.w3schools.com/sql/sql_distinct.asp).)
 ```sql
 SELECT DISTINCT Country FROM [Customers]
 21    
 ```
 * What category appears in the most orders?
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
 * What was the total cost for each order?
 ```sql
SELECT Orders.OrderID, SUM(OrderDetails.Quantity*Products.Price) AS Cost
FROM
	Orders
    JOIN Products     ON OrderDetails.OrderID = Orders.OrderID
    JOIN OrderDetails ON OrderDetails.ProductID = Products.ProductID
GROUP BY Orders.OrderID
ORDER BY Cost DESC;
```
 * Which employee made the most sales (by total cost)?
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
 * Which employees have BS degrees? (*Hint:* look at the [LIKE](http://www.w3schools.com/sql/sql_like.asp) operator.)
```sql
SELECT * FROM [Employees]
WHERE Notes LIKE '%BS%'
```
Janet Leverling   
Steven Buchanan   
 * Which supplier of three or more products has the highest average product price? (*Hint:* look at the [HAVING](http://www.w3schools.com/sql/sql_having.asp) operator.)
 ```sql
SELECT SupplierName, COUNT(Products.SupplierID), AVG(Products.Price) AS AvePrice
FROM
	Suppliers
    JOIN Products     ON Suppliers.SupplierID = Products.SupplierID
GROUP BY SupplierName
HAVING COUNT(Products.SupplierID) >= 3;
```
Tokyo Traders ($46) 
