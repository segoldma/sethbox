import json
from collections import defaultdict

def load_json(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)

def get_models(manifest):
    return manifest.get('nodes', {})

def compare_models(current_models, previous_models):
    added_models = []
    removed_models = []
    modified_models = []

    # Identify added and modified models
    for model_name, model_data in current_models.items():
        if model_name not in previous_models:
            added_models.append(model_name)
        else:
            # Compare checksums to identify modified models
            current_checksum = model_data.get('checksum', {}).get('checksum')
            previous_checksum = previous_models[model_name].get('checksum', {}).get('checksum')

            if current_checksum != previous_checksum:
                modified_models.append(model_name)

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
        summary.extend(f"- {model}" for model in modified_models)

    return "\n".join(summary)

def main():
    current_manifest = load_json('target/manifest.json')
    previous_manifest = load_json('artifacts/artifacts/previous_manifest.json')

    current_models = get_models(current_manifest)
    previous_models = get_models(previous_manifest)

    added_models, removed_models, modified_models = compare_models(current_models, previous_models)

    summary = generate_summary(added_models, removed_models, modified_models)

    if summary:
        with open('summary.md', 'w') as file:
            file.write(summary)

    return bool(summary)  # Return True if there are changes, False otherwise

if __name__ == "__main__":
    main()
