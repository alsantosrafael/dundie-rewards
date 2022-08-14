MARKER = """\
unit: Marks unit tests
integration: Marks integration tests
high: High Priority
medium: Medium Priority
low: Low Priority
"""


def pytest_configure(config):
    map(
        lambda line: config.addininvalue_line("markers", line),
        MARKER.split("\n"),
    )
