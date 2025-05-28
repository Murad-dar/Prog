-- Создание таблицы проектов
CREATE TABLE projects (
    project_id INT PRIMARY KEY AUTO_INCREMENT,
    project_name VARCHAR(255) NOT NULL,
    description TEXT,
    status ENUM('Планируется', 'В работе', 'Завершен', 'Отменен') DEFAULT 'Планируется',
    start_date DATE,
    end_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Создание таблицы исполнителей
CREATE TABLE executors (
    executor_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone VARCHAR(20),
    position VARCHAR(100),
    hire_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Создание таблицы задач
CREATE TABLE tasks (
    task_id INT PRIMARY KEY AUTO_INCREMENT,
    project_id INT,
    executor_id INT,
    task_name VARCHAR(255) NOT NULL,
    description TEXT,
    status ENUM('Не начата', 'В работе', 'Выполнена', 'Отменена') DEFAULT 'Не начата',
    priority ENUM('Низкий', 'Средний', 'Высокий', 'Критический') DEFAULT 'Средний',
    start_date DATE,
    due_date DATE,
    completion_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (executor_id) REFERENCES executors(executor_id) ON DELETE SET NULL
);