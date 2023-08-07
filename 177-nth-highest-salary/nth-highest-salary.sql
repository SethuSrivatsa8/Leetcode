CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      WITH CTE AS 
      (
          SELECT *,DENSE_RANK() OVER(ORDER BY SALARY DESC) AS R FROM EMPLOYEE 
      )
      SELECT DISTINCT IFNULL(SALARY,NULL) FROM CTE WHERE R=N
      
  );
END