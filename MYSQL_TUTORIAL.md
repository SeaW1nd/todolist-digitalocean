
# MySQL Tutorial

This tutorial will guide you through the process of installing and configuring MySQL. You can choose between a local installation or using Docker. Detailed steps are provided for both methods.

## Local Installation (Ubuntu)

### Step 1: Install MySQL Server

```sh
$ sudo apt install mysql-server
```

### Step 2: Check MySQL Server Status

```sh
$ sudo service mysql status
```

### Step 3: Configure MySQL to Grant Access to Root Without a Password

1. Open the MySQL configuration file for editing:

    ```sh
    $ sudo nano /etc/mysql/my.cnf
    ```

2. Add the following line under the `[mysqld]` section:

    ```ini
    [mysqld]
    skip-grant-tables
    ```

### Step 4: Restart MySQL Service and Access MySQL

1. Restart the MySQL service:

    ```sh
    $ sudo service mysql restart
    ```

2. Access MySQL as root:

    ```sh
    $ mysql -u root
    ```

### Step 5: Update Root User Authentication

1. Switch to the MySQL database:

    ```sql
    mysql> USE mysql;
    ```

2. Update the root user's authentication string:

    ```sql
    mysql> UPDATE user SET authentication_string='' WHERE User='root';
    ```

3. Flush privileges:

    ```sql
    mysql> FLUSH PRIVILEGES;
    ```

4. Exit MySQL:

    ```sql
    mysql> EXIT;
    ```

### Step 6: Remove the Configuration Change

1. Open the MySQL configuration file for editing:

    ```sh
    $ sudo nano /etc/mysql/my.cnf
    ```

2. Remove or comment out the line added in Step 3:

    ```ini
    # [mysqld]
    # skip-grant-tables
    ```

### Step 7: Restart MySQL Service

```sh
$ sudo service mysql restart
```

### Step 8: Access MySQL Server with Root

```sh
$ mysql -u root -p
```

- When prompted for a password, just press Enter.

### Step 9: Execute Setup SQL Script

```sql
mysql> (Type all commands in setup.sql)
```

## MySQL Tutorial for Windows

This tutorial provides step-by-step instructions for installing and configuring MySQL on a Windows system.

### Step 1: Download MySQL Installer

1. Go to the official [MySQL downloads page](https://dev.mysql.com/downloads/installer/).
2. Download the `MySQL Installer` for Windows.

### Step 2: Install MySQL

1. Run the downloaded `mysql-installer-web-community-<version>.exe` file.
2. Follow the installation wizard:
    - Choose the setup type. For most users, "Developer Default" is recommended.
    - Click "Next" and then "Execute" to install the required components.

### Step 3: Configure MySQL Server

1. After installation, the MySQL Installer will launch the configuration wizard.
2. Configure the following:
    - **Config Type**: Choose "Development Machine".
    - **Connectivity**: Make sure the port is set to `3306`.
    - **Authentication Method**: Choose "Use Strong Password Encryption".
3. Set the root password and create additional user accounts if necessary.
4. Complete the configuration steps and start the MySQL Server.

### Step 4: Verify MySQL Server Installation

1. Open the Command Prompt.
2. Check the MySQL service status:

    ```sh
    sc query MySQL
    ```

3. Log in to MySQL using the command line:

    ```sh
    mysql -u root -p
    ```

4. Enter the root password when prompted.

### Step 5: Secure MySQL Installation

1. Run the MySQL secure installation script:

    ```sh
    mysql_secure_installation
    ```

2. Follow the prompts to improve the security of your MySQL installation:
    - Set a root password.
    - Remove anonymous users.
    - Disallow root login remotely.
    - Remove test database and access to it.
    - Reload privilege tables.

### Step 6: Create a New Database and User

1. Log in to MySQL:

    ```sh
    mysql -u root -p
    ```

2. Create a new database:

    ```sql
    CREATE DATABASE todolist;
    ```

3. Create a new user and grant privileges:

    ```sql
    CREATE USER 'todolist'@'localhost' IDENTIFIED BY 'Todolist<123456789';
    GRANT ALL PRIVILEGES ON todolist.* TO 'todolist'@'localhost' WITH GRANT OPTION;
    FLUSH PRIVILEGES;
    ```

## Using Docker

### Step 1: Create a Dockerfile

Create a `Dockerfile` with the following content:

```Dockerfile
# Use the official MySQL image from Docker Hub
FROM mysql:latest

# Set the root password for MySQL
ENV MYSQL_ROOT_PASSWORD=password

# Expose port 3306 for external communication
EXPOSE 3306

# Start MySQL service
CMD ["mysqld", "--bind-address=0.0.0.0"]
```

### Step 2: Build Docker Image

```sh
$ docker build -t mysql_server .
```

### Step 3: Run Docker Container

```sh
$ docker run -d -p <PORT>:3306 --name mysql_container mysql_server
# Replace <PORT> with the desired port number
```

### Step 4: Identify Container ID

```sh
$ docker ps -a
```

### Step 5: Access MySQL Inside Container

```sh
$ docker exec -it CONTAINER_ID_OR_NAME mysql -uroot -p
# Password: password
mysql> (Copy all commands in setup.sql)
```

### Important Notes

1. Replace 'localhost' with '%' in MySQL Docker configuration because the Docker container runs on a different IP than 127.0.0.1.
2. If you accidentally execute the `setup.sql` script with 'localhost', undo with the following commands:

    ```sql
    mysql> UPDATE mysql.user SET Host='%' WHERE User='todolist';
    mysql> REVOKE ALL PRIVILEGES ON todolist.* FROM 'todolist'@'localhost';
    mysql> GRANT ALL PRIVILEGES ON todolist.* TO 'todolist'@'%' WITH GRANT OPTION;
    mysql> FLUSH PRIVILEGES;
    mysql> -- Verify
    mysql> SELECT Host, User FROM mysql.db WHERE Db='todolist';
    ```

## Testing MySQL Connection with Python

Create a Python script to test the connection:

```python
import mysql.connector

# Define the connection parameters
host = 'localhost'
port = 3306  # This is the port mapped to MySQL in the Docker container
user = 'todolist'
password = 'Todolist<123456789'  # Change this to your MySQL root password

try:
    # Connect to the MySQL server
    connection = mysql.connector.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database='todolist'
    )

    if connection.is_connected():
        print("Successfully connected to MySQL server")

        # Get the MySQL server version
        cursor = connection.cursor()
        cursor.execute("SELECT VERSION()")
        version = cursor.fetchone()[0]
        print("MySQL server version:", version)

        # Close cursor and connection
        cursor.close()
        connection.close()
        print("Connection closed")

except mysql.connector.Error as error:
    print("Failed to connect to MySQL server:", error)
```
### ChatGPT can make mistakes. Check important info. Low-level tutorial in "mysql-tutorial.txt"
