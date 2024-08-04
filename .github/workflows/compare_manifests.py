import json
import jsondiff
from collections import defaultdict

def load_json(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)

def get_models(manifest):
    return manifest.get('nodes', {})

def compare_models(current_models, previous_models):
    added_models = []
    removed_models = []
    modified_models = defaultdict(lambda: {'added_columns': [], 'removed_columns': [], 'modified_columns': []})

    # Identify added and modified models
    for model_name, model_data in current_models.items():
        if model_name not in previous_models:
            added_models.append(model_name)
        else:
            # Compare columns
            current_columns = model_data.get('columns', {})
            previous_columns = previous_models[model_name].get('columns', {})

            # Find added, removed, and modified columns
            for column_name, column_data in current_columns.items():
                if column_name not in previous_columns:
                    modified_models[model_name]['added_columns'].append(column_name)
                elif current_columns[column_name]['data_type'] != previous_columns[column_name]['data_type']:
                    modified_models[model_name]['modified_columns'].append(column_name)

            for column_name in previous_columns:
                if column_name not in current_columns:
                    modified_models[model_name]['removed_columns'].append(column_name)

    # Identify removed models
    for model_name in previous_models:
        if model_name not in current_models:
            removed_models.append(model_name)

    return added_models, removed_models, modified_models

def generate_summary(added_models, removed_models, modified_models):
    summary = []

    if added_models:
        summary.append("### Added Models")
        summary.extend(f"- {model}" for model in added_models)

    if removed_models:
        summary.append("\n### Removed Models")
        summary.extend(f"- {model}" for model in removed_models)

    if modified_models:
        summary.append("\n### Modified Models")
        for model, changes in modified_models.items():
            summary.append(f"- {model}")
            if changes['added_columns']:
                summary.append("  - **Added Columns**:")
                summary.extend(f"    - {column}" for column in changes['added_columns'])
            if changes['removed_columns']:
                summary.append("  - **Removed Columns**:")
                summary.extend(f"    - {column}" for column in changes['removed_columns'])
            if changes['modified_columns']:
                summary.append("  - **Modified Columns**:")
                summary.extend(f"    - {column}" for column in changes['modified_columns'])

    return "\n".join(summary)

def main():
    current_manifest = load_json('target/manifest.json')
    previous_manifest = load_json('artifacts/artifacts/previous_manifest.json')

    current_models = get_models(current_manifest)
    previous_models = get_models(previous_manifest)

    added_models, removed_models, modified_models = compare_models(current_models, previous_models)

    summary = generate_summary(added_models, removed_models, modified_models)

    with open('summary.md', 'w') as file:
        file.write(summary)

if __name__ == "__main__":
    main()
