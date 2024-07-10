-- models/profiles/production_table_profile.sql
{{ 
  dbt_profiler.get_profile(relation=ref('dim_characters'), 
    exclude_measures=[
      "avg",
      "std_dev_population",
      "std_dev_sample"
    ] 
  )
}}
