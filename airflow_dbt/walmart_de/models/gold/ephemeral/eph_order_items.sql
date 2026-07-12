




SELECT
    distinct
    order_item_id,
    order_item_product_id,
    quantity,
    unit_price,
    line_amount,
    order_item_created_timestamp,
    order_item_updated_timestamp,
    order_item_is_active,
    order_item_processed_at,
    current_timestamp() as order_gold_processed_at
FROM
    {{ ref('obt_b') }}