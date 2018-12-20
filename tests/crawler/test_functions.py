import pytest
from crawler.views import format_response, format_error_response


@pytest.mark.parametrize("code, data, msg", [
    (200, {}, "Successfully"),
    (201, {}, "Successfully Created"),
])
def test_format_response(code, data, msg):
    response = format_response(code, data, msg)
    assert response.status_code == code
    data_ = response.data
    assert data_['message'] == msg
    assert data_['data'] == data


@pytest.mark.parametrize("code, msg", [
    (401, "Failed"),
    (404, "Bad Request"),
])
def test_format_error_response(code, msg):
    response = format_error_response(code, msg)
    assert response.status_code == code
    data = response.data

    assert data['message'] == msg
