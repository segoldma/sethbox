{{ 
    config(materialized='view')
}}

select
  id as character_id
  , name as character_name
  , episodes as episode_count
  , current_timestamp() as loaded_at


from {{ ref('appearance_counts') }}