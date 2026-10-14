"""Exercise lazy imports which are not reached by the CLI's --help branch."""
import pytest

from chromapeak.main import _get_runner


@pytest.mark.parametrize("algorithm", ["xcms", "ms-dial", "pyopenms", "asari"])
def test_algorithm_adapter_can_be_loaded(algorithm):
    assert callable(_get_runner(algorithm))
