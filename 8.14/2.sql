SELECT name FROM SalesPerson
WHERE sales_id NOT IN (
    SELECT DISTINCT sales_id FROM Orders
    INNER JOIN Company ON Orders.com_id = Company.com_id
    WHERE Company.name = 'RED'
);
