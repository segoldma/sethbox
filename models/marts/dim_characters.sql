{{
    config(
        materialized='table'
    )
}}

with characters as (
    select * from {{ ref('stg_characters') }}
)

, personality_traits as (
    select * from {{ ref('stg_personality_traits') }}
)

, appearance_counts as (
    select * from {{ ref('stg_appearance_counts') }}
)

, final as (
    select
        characters.character_id
        , characters.character_name
        , characters.character_description
        , personality_traits.personality_traits
        , appearance_counts.episode_count
        , characters.loaded_at
        , 1 as numb

    from characters
    left join personality_traits
        on characters.character_id = personality_traits.character_id
    left join appearance_counts
        on characters.character_id = appearance_counts.character_id
)

select * from final
