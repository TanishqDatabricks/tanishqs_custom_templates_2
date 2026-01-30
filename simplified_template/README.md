# Simplified Databricks Asset Bundle Template

A streamlined Databricks Asset Bundle template that focuses on essential features without multi-cloud complexity.

## Features

This simplified template includes:

- **Job Support**: Python and Notebook tasks
- **Delta Live Tables**: Simple hello-world pipelines in Python or SQL
- **Compute Options**: Serverless or Classic compute (AWS default)
- **Unity Catalog Support**: Optional integration
- **Multi-Environment**: Dev, Staging, and Production targets

## Differences from Advanced Template

This template is simpler in these ways:
- **Single Cloud**: AWS-only configurations (no Azure/GCP options)
- **Fewer Job Types**: Only Python and Notebook (no DBT or Spark JAR)
- **Simple Pipelines**: Hello-world style DLT pipelines instead of complex examples
- **Fewer Variables**: Streamlined configuration options

## Template Variables

| Variable | Description | Options | Default |
|----------|-------------|---------|---------|
| `project_name` | Name of your project | String (3+ chars) | `my_project` |
| `include_job` | Include a Databricks job | yes, no | `yes` |
| `job_type` | Type of job to create | python, notebook | `python` |
| `include_pipeline` | Include DLT pipeline | yes, no | `no` |
| `pipeline_language` | Pipeline language | python, sql | `python` |
| `compute_type` | Compute type | serverless, classic | `serverless` |
| `cluster_size` | Cluster size (classic only) | small, medium, large | `small` |
| `enable_unity_catalog` | Use Unity Catalog | yes, no | `yes` |
| `catalog_name` | Unity Catalog catalog | String | `main` |
| `schema_name` | Unity Catalog schema | String | `default` |

## Pipeline Examples

### Python Pipeline
Creates two simple DLT tables:
- `hello_world_data`: Basic table with word pairs
- `hello_world_message`: Combines words into messages

### SQL Pipeline
Same structure using SQL syntax for DLT definitions.

## Usage

Initialize a new bundle:

```bash
databricks bundle init /path/to/simplified_template
```

Deploy:

```bash
cd <project_name>
databricks bundle validate
databricks bundle deploy
```

## When to Use This Template

Use this template when:
- You're deploying on AWS
- You need Python or Notebook jobs
- You want simple, easy-to-understand pipelines
- You don't need DBT or multi-cloud support

For more advanced features, use the `more_complicated_template` instead.
