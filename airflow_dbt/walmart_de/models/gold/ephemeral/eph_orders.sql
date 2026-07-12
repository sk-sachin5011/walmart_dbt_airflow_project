


SELECT
    distinct
    order_id,
    order_customer_id,
    order_store_id,
    order_status,
    total_amount,
    payment_method,
    order_timestamp,
    order_created_timestamp,
    order_updated_timestamp,
    order_processed_at,
    order_is_active,
    current_timestamp() as order_gold_processed_at
FROM
    {{ ref('obt_b') }}