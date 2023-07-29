{{
    config(materialized='view')
}}

select
    id as character_id
    , name as character_name
    , traits as personality_traits
    , current_timestamp() as loaded_at

from {{ ref('personality_traits') }}
