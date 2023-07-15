{{
    config(materialized='view')
}}

select
  id as character_id
  , name as character_name
  , traits as personality_traits
from {{ ref('personality_traits')}}