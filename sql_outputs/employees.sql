```sql
-- Create employee table
CREATE TABLE employee (
  id INT AUTO_INCREMENT,
  name VARCHAR(255),
  role VARCHAR(255),
  salary DECIMAL(10, 2),
  PRIMARY KEY (id)
);

-- Insert 3 employees
INSERT INTO employee (name, role, salary)
VALUES
  ('John Doe', 'Developer', 50000.00),
  ('Jane Doe', 'Manager', 80000.00),
  ('Bob Smith', 'Developer', 60000.00);

-- Create view avg_salary_per_role
CREATE VIEW avg_salary_per_role AS
SELECT 
  role,
  AVG(salary) AS avg_salary
FROM 
  employee
GROUP BY 
  role;
```