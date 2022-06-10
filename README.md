# Best practices for using an IDE with Databricks

This repository is a companion for the example article "Use an IDE with Databricks" for [AWS](https://docs.databricks.com/dev-tools/ide-how-to.html), [Azure](https://docs.microsoft.com/azure/databricks/dev-tools/ide-how-to), and [GCP](https://docs.gcp.databricks.com/dev-tools/ide-how-to.html). 

This example features the use of Visual Studio Code, Python, `dbx` by Databricks Labs (for [AWS](https://docs.databricks.com/dev-tools/dbx.html), [Azure](https://docs.microsoft.com/azure/databricks/dev-tools/dbx), and [GCP](https://docs.gcp.databricks.com/dev-tools/dbx.html)), `pytest`, and GitHub Actions.

You can adapt this example for use with other Python-compatible IDEs such as PyCharm, IntelliJ IDEA with the Python plugin, and Eclipse with the PyDev plugin.

Going through the example, you will use your IDE to:

* Get data from the [owid/covid-19-data](https://github.com/owid/covid-19-data) repo in GitHub.
* Filter the data for a specific ISO country code.
* Create a pivot table from the data.
* Perform data cleansing on the data.
* Modularize the code logic into reusable functions.
* Unit test the functions.
* Provide `dbx` project configurations and settings to enable the code to write the data to a Delta table in a remote Databricks workspace.

The only time you need to use the Databricks user interface for this example is to see the results of writing the data to your Databricks workspace. (And even then, you can use the Databricks Jobs REST API or the Databricks Jobs CLI for [AWS](https://docs.databricks.com/data-engineering/jobs/jobs.html), [Azure](https://docs.microsoft.com/azure/databricks/data-engineering/jobs/jobs), or [GCP](https://docs.gcp.databricks.com/data-engineering/jobs/jobs.html) to get some high-level information about those data writes programmatically.) Otherwise, you can complete all of these development tasks from within your favorite Python-compatible IDE.

The example is hands-on. We recommend working through the example article to learn how to apply these techniques to your own Databricks development tasks from within your favorite Python-compatible IDE.
