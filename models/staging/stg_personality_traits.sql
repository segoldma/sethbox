{{
    config(materialized='view')
}}

select
  id as character_id
  , name as character_name
  , personality_traits
from {{ ref('appearance_counts')}}