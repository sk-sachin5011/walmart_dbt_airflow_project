






SELECT
    distinct
    employee_id,
    employee_first_name,
    employee_last_name,
    employee_store_id,
    employee_email,
    employee_job_title,
    employee_salary
    employee_is_active,
    employee_created_timestamp,
    employee_processed_at,
    employee_updated_timestamp,
    current_timestamp() as employee_gold_processed_at
FROM
    {{ ref('obt_b') }}