










SELECT
    distinct
    store_id,
    store_name,
    store_city,
    store_country,
    store_province,
    store_is_active,
    store_created_timestamp,
    store_updated_timestamp,
    store_processed_at,
    current_timestamp() as store_gold_processed_at
FROM
    {{ ref('obt_b') }}