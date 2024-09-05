{{
    config(materialized='view')
}}

select
    id as writer_id
    , name as writer_name
    , current_timestamp() as loaded_at

from {{ ref('writers') }}
