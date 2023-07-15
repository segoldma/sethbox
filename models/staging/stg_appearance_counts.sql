{{ 
    config(materialized='view')
}}

select
  id as character_id
  , name as character_name
  , episodes as episode_count

from {{ ref('appearance_counts') }}