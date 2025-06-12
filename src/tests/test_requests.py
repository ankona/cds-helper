from cdshelper.core.core import CdsDataRequest


def test_monthly_generator(test_request: CdsDataRequest) -> None:
    assert test_request
