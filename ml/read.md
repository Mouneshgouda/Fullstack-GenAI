
### Redis 

## 🔵 1. CREATE

```python
HSET user:1001 name "Alice"
HSET user:1001 email "alice@example.com"
HSET user:1001 age "25"
```
## 🟢 2. READ

```python
# Get everything
HGETALL user:1001

# Get one field
HGET user:1001 email
```

## 🟡 3. UPDATE
```python
HSET user:1001 name "Alice A."     # Update name
HSET user:1001 age "26"          # Update age

-check again
HGETALL user:1001
```

## 🔴 4. DELETE

```python
# Delete one field (like age only)
HDEL user:1001 age

# Delete the entire user
DEL user:1001
```
## ❓ 5. CHECK EXISTENCE redis
```python
EXISTS user:1001   # Returns 1 if exists, 0 if not
```




