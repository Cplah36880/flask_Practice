import pytest

pytestmark = pytest.mark.skip(
    reason="MongoDB service is not available on the Jenkins CI server."
)
