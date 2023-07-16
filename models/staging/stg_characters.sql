{{
    config(materialized='view')
}}

select
  id as character_id
  , name as character_name
  , description as character_description
  , current_timestamp() as loaded_at
  , 100 as one_hundred
  , 200 as two_hundred

from {{ ref('characters') }}