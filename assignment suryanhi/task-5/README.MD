# 🚀 Database Optimization: PostgreSQL / MongoDB

This solution focuses on optimizing a **PostgreSQL**   database for better performance through **indexing**, **query optimization**, and **data partitioning**.

---

## Objective

- Improve database read/write efficiency
- Reduce query response times
- Optimize resource usage and scalability

---

##  Optimization Techniques

### 1. Indexing

- **PostgreSQL**: Created B-tree and GIN indexes on frequently queried columns
 
**Benefits:**
- Speeds up `SELECT` operations
- Reduces full-table scans

---

### 2.  Query Optimization

- Analyzed slow queries using `EXPLAIN` and `EXPLAIN ANALYZE` (PostgreSQL)  
- Rewrote suboptimal queries with better filter usage, projections, and joins

---

### 3.  Data Partitioning (Sharding)

- **PostgreSQL**: Used table partitioning for large datasets (e.g., by date)
 

---

##  Example: Query Optimization

### PostgreSQL

####  Before Optimization:
```sql
SELECT * FROM orders WHERE EXTRACT(YEAR FROM order_date) = 2023;
```
#### after optimization
```sql
SELECT * FROM orders WHERE order_date BETWEEN '2023-01-01' AND '2023-12-31';
```