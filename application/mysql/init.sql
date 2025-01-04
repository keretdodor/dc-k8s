
CREATE TABLE IF NOT EXISTS employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    role VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

INSERT INTO employees (name, role) VALUES 
    ('John Doe', 'Software Engineer'),
    ('Jane Smith', 'Product Manager'),
    ('Mike Johnson', 'DevOps Engineer'),
    ('Sarah Williams', 'Data Scientist'),
    ('Alex Brown', 'UI/UX Designer');