# Back-End Developer Capstone
META Back-End Developer Course Capstone Project 

## Description
This project demonstrates the functionality of E-commerce application dubbed The Little-Lemon Restaurant

## Follow the steps below to get this App going

### 1. Activate Virtual Environment 

```
pipenv shell
```

```
pipenv install
```

### 2. Install dependencies

```
pipenv install django
```

```
pipenv install mysqlclient
```

### 3. Start the MySQL server  
Start the MySQL command-line client

```
mysql -u root -p 
```

### 4. Perform migrations - ensure you're inside the directory that contains ```manage.py``` file

```
py manage.py makemigrations
```

```
py manage.py migrate
```

### 5. Start the server

```
py manage.py runserver
```

### 6 Run the tests

```
py manage.py test tests
```


## Test API paths using Postman, Insomnia or Browser

### Credentials

```
Username: admin
```
```
Email: admin@littlelemon.com
```
```
Password: lemon@789!
```

### Login using ```djoser``` endpoint
/auth/token/login 

### Make POST request and create new user
/auth/users/ 

### Menu items
/restaurant/menu/
/restaurant/menu/{menuItemId}

### Table booking 
/restaurant/booking/tables/
/restaurant/booking/tables/{bookingId}
