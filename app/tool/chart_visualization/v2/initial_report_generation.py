from app.tool.chart_visualization.python_execute import NormalPythonExecute


class GenerateInitialReport(NormalPythonExecute):
    """A tool for generating initial data analysis reports based on the report
    template and user's input data.
    """

    name: str = "generate_initial_report"
    description: str = (
        "Generates an initial HTML data analysis report based on the report "
        "template and user's input data. After searhing and reading the "
        "report template, you should dynamically adapt the template content "
        "according to user input data, intelligently determine which charts "
        "should be included in the report, and automatically populate the "
        "fillable placeholders with corresponding data.\n\nOutputs: 1) HTML report "
        "file path"
    )

    parameters: dict = {
        "type": "object",
        "properties": {
            "code": {
                "type": "string",
                "description": (
                    "Python code for generating initial HTML data report based on the "
                    "report template and user's input data.\n\n## Output Requirements\n"
                    "1. Generate initial_report.html file\n2. Print the file path: "
                    "print(report_path)\n\n# Notes:\n1. Refer to the searched report templates\n"
                    "2. Complete the applicable placeholders, and leave any unfilled ones "
                    "as '[placeholder: ...]'.\n\n"
                ),
            },
        },
        "required": ["code", "code_type"],
    }
