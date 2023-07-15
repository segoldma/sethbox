{{
    config(materialized='view')
}}

select
  id as character_id
  , name as character_name
  , description as character_description

from {{ ref('characters') }}