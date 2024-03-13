CREATE USER 'root' @'%' IDENTIFIED WITH mysql_native_password BY 'secret';

GRANT ALL PRIVILEGES ON *.* to 'root' @'%';

CREATE DATABASE `sqlqlchemy` DEFAULT CHARACTER SET utf8mb4;

CREATE DATABASE `streamlit` DEFAULT CHARACTER SET utf8mb4;

CREATE DATABASE `test` DEFAULT CHARACTER SET utf8mb4;

FLUSH PRIVILEGES;
