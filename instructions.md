I'm a product manager at Databricks. We're in the process of adding custom bundle templates to Databricks Asset Bundles in the Workspace. These were previously accessible via the CLI, but now we're exposing them in the UI.

I want to test that complicated templates work as expected, can you please modify the databricks asset bundle custom template "more_complicated_template" to have template helpers and variables as defined in the documentation here: https://docs.databricks.com/aws/en/dev-tools/bundles/templates#template-helpers-and-variables? Note that our templates are based on Go templates: https://pkg.go.dev/text/template. 

I've attached both docs as a PDF: dabs_template_docs and go_template_docs respectively.

Make the template aligned with real-world scenarios where users might want asset bundle templates, i.e. include options like "should this template have a job?", "should it have a pipeline"? Ask whether the user should use serverless or classic and configure the template accordingly. You can refer to the existing cluster configuration for what it should look like if the user does have a cluster.

Please walk me through the changes once done.

