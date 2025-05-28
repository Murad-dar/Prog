-- Задачи с информацией о проекте и исполнителе
SELECT 
    t.task_name,
    t.description,
    t.status,
    t.priority,
    p.project_name,
    CONCAT(e.first_name, ' ', e.last_name) as executor_name,
    e.position
FROM tasks t
JOIN projects p ON t.project_id = p.project_id
JOIN executors e ON t.executor_id = e.executor_id;

-- Количество задач по проектам
SELECT 
    p.project_name,
    COUNT(t.task_id) as tasks_count,
    SUM(CASE WHEN t.status = 'Выполнена' THEN 1 ELSE 0 END) as completed_tasks
FROM projects p
LEFT JOIN tasks t ON p.project_id = t.project_id
GROUP BY p.project_id, p.project_name;

-- Загруженность исполнителей
SELECT 
    CONCAT(e.first_name, ' ', e.last_name) as executor_name,
    e.position,
    COUNT(t.task_id) as total_tasks,
    SUM(CASE WHEN t.status = 'В работе' THEN 1 ELSE 0 END) as active_tasks
FROM executors e
LEFT JOIN tasks t ON e.executor_id = t.executor_id
GROUP BY e.executor_id, e.first_name, e.last_name, e.position
ORDER BY active_tasks DESC;

-- Просроченные задачи
SELECT 
    t.task_name,
    p.project_name,
    CONCAT(e.first_name, ' ', e.last_name) as executor_name,
    t.due_date,
    DATEDIFF(CURDATE(), t.due_date) as days_overdue
FROM tasks t
JOIN projects p ON t.project_id = p.project_id
JOIN executors e ON t.executor_id = e.executor_id
WHERE t.due_date < CURDATE() AND t.status != 'Выполнена'
ORDER BY days_overdue DESC;

-- Статистика по приоритетам задач
SELECT 
    priority,
    COUNT(*) as task_count,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM tasks), 2) as percentage
FROM tasks
GROUP BY priority
ORDER BY 
    CASE priority
        WHEN 'Критический' THEN 1
        WHEN 'Высокий' THEN 2
        WHEN 'Средний' THEN 3
        WHEN 'Низкий' THEN 4
    END;