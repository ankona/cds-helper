from datetime import datetime

import pytest

from cdshelper.core.core import (
    CdsDataRequest,
    CdsMonthlyDataRequest,
)


@pytest.fixture
def test_request() -> CdsDataRequest:
    """Create a `CdsDataRequest` for use in tests where specific attributes
    aren't needed."""
    request = CdsDataRequest(
        dataset="mock-dataset",
        start_date=datetime(2017, 1, 1),
        end_date=datetime(2017, 2, 1),
        data_type="mock-datatype",
        variables=["mock-variable"],
    )
    return request


@pytest.fixture
def test_monthly_request(test_request: CdsDataRequest) -> CdsMonthlyDataRequest:
    return CdsMonthlyDataRequest(
        "2017",
        "01",
        ["01", "02", "03"],
        ["01:00", "02:00", "03:00"],
        test_request,
    )
