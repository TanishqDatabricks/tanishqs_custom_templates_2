# Advanced Databricks Asset Bundle Template

This is an advanced, production-ready Databricks Asset Bundle template that demonstrates the use of template helpers, variables, and conditional logic based on user choices.

## Features

This template includes:

- **Multiple Resource Types**: Jobs, Delta Live Tables Pipelines
- **Compute Options**: Serverless or Classic compute with configurable cluster sizes
- **Unity Catalog Support**: Optional integration with Unity Catalog
- **Multi-Cloud Support**: AWS, Azure, and GCP configurations
- **Multiple Job Types**: Python, Notebook, DBT, and Spark JAR tasks
- **Pipeline Options**: Python or SQL-based Delta Live Tables
- **Multi-Environment**: Dev, Staging, and Production targets
- **Custom Template Helpers**: Cloud-specific configurations using Go templates

## Template Variables

The template uses the following input variables:

| Variable | Description | Options | Default |
|----------|-------------|---------|---------|
| `project_name` | Name of your project | String (3+ chars) | `my_project` |
| `cloud_provider` | Cloud platform | aws, azure, gcp | `aws` |
| `include_job` | Include a Databricks job | yes, no | `yes` |
| `job_type` | Type of job to create | python, notebook, dbt, spark_jar | `python` |
| `include_pipeline` | Include DLT pipeline | yes, no | `no` |
| `pipeline_language` | Pipeline language | python, sql | `python` |
| `compute_type` | Compute type | serverless, classic | `serverless` |
| `cluster_size` | Cluster size (classic only) | small, medium, large | `small` |
| `enable_unity_catalog` | Use Unity Catalog | yes, no | `yes` |
| `catalog_name` | Unity Catalog catalog | String | `main` |
| `schema_name` | Unity Catalog schema | String | `default` |

## Template Helpers

Custom template helpers defined in `library/helpers.tmpl`:

- `{{template "spark_version" .}}` - Returns appropriate Spark version
- `{{template "node_type" .}}` - Returns cloud-specific node type based on size
- `{{template "num_workers" .}}` - Returns number of workers based on cluster size
- `{{template "catalog_path" .}}` - Returns Unity Catalog path or Hive metastore
- `{{template "autoscale_config" .}}` - Returns autoscaling configuration

## Built-in Helpers Used

- `{{workspace_host}}` - Current workspace URL
- `{{user_name}}` - Current user's name
- `{{is_service_principal}}` - Whether user is a service principal
- `{{if}}`, `{{else}}`, `{{end}}` - Conditional logic
- `{{range}}` - Iteration (demonstrated in configurations)

## Usage

Initialize a new bundle using this template:

```bash
databricks bundle init /path/to/more_complicated_template
```

The CLI will prompt you for all configuration options. Based on your choices, it will generate:

1. **databricks.yml** - Main bundle configuration with multi-environment setup
2. **Job Configuration** (if selected) - Fully configured job with chosen compute type
3. **Pipeline Configuration** (if selected) - DLT pipeline in Python or SQL
4. **Source Files** - Sample code for jobs, notebooks, and pipelines
5. **Custom Helpers** - Reusable template functions

## Project Structure

```
{{.project_name}}/
├── databricks.yml                          # Main bundle config
├── resources/
│   ├── {{.project_name}}_job.yml.tmpl     # Job definition (conditional)
│   └── {{.project_name}}_pipeline.yml.tmpl # Pipeline definition (conditional)
├── src/
│   ├── task.py                             # Python task
│   ├── notebook.py                         # Notebook task
│   ├── dlt_pipeline.py                     # Python DLT pipeline
│   └── dlt_pipeline.sql                    # SQL DLT pipeline
└── library/
    └── helpers.tmpl                        # Custom template helpers
```

## Deployment

After initialization:

```bash
cd {{.project_name}}

# Validate the bundle
databricks bundle validate

# Deploy to dev environment (default)
databricks bundle deploy

# Deploy to staging
databricks bundle deploy -t staging

# Deploy to production
databricks bundle deploy -t prod
```

## Example Scenarios

### Scenario 1: Serverless Python Job with Unity Catalog
- Job Type: Python
- Compute: Serverless
- Unity Catalog: Enabled
- Result: Fast, scalable job using Unity Catalog

### Scenario 2: Classic Compute with DLT Pipeline
- Pipeline Language: SQL
- Compute: Classic (Medium)
- Cloud: AWS
- Result: Simple hello-world DLT pipeline on dedicated compute cluster

### Scenario 3: Multi-Stage Data Processing
- Include Job: Yes (Python)
- Include Pipeline: Yes (Python)
- Unity Catalog: Yes
- Result: Complete data workflow with job and simple hello-world pipeline

## Advanced Features

### Conditional Resource Creation

Resources are only created if selected:

```yaml
{{- if eq .include_job "yes"}}
# Job configuration here
{{- end}}

{{- if eq .include_pipeline "yes"}}
# Pipeline configuration here
{{- end}}
```

### Cloud-Specific Configuration

Node types and attributes adapt to your cloud provider:

```yaml
{{- if eq .cloud_provider "aws"}}
aws_attributes:
  availability: SPOT_WITH_FALLBACK
{{- else if eq .cloud_provider "azure"}}
azure_attributes:
  availability: SPOT_WITH_FALLBACK_AZURE
{{- else if eq .cloud_provider "gcp"}}
gcp_attributes:
  availability: PREEMPTIBLE_WITH_FALLBACK_GCP
{{- end}}
```

### Skip Prompt Logic

Questions are skipped when not relevant:

```json
"skip_prompt_if": {
  "properties": {
    "include_job": {
      "const": "no"
    }
  }
}
```

## Documentation

- [Databricks Asset Bundles](https://docs.databricks.com/dev-tools/bundles/)
- [Go Template Documentation](https://pkg.go.dev/text/template)
- [Template Helpers and Variables](https://docs.databricks.com/dev-tools/bundles/templates#template-helpers-and-variables)

## Support

For issues or questions about this template, please refer to the Databricks documentation or contact your Databricks representative.
