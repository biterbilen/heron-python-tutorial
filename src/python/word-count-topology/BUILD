python_library(
    name = "spouts-bolts-py",
    sources=globs('*.py', exclude=[['word_count_topology.py']]),
)

python_binary(
    name = "word-count-topology",
    source='word_count_topology.py',
    dependencies = [
        ':spouts-bolts-py',
        '3rdparty/python:heronpy',
        '3rdparty/python:six',
    ],
)
