import pytest


def test__get_most_requested_ingredient__when_there_are_no_orders(client, report_uri):
    """
    tests errors are not produced when there are no orders
    TODO: extend to test correct behavior
    """
    response = client.get(report_uri + 'mri')
    pytest.assume(response.status.startswith('200'))
    payload = response.json
    print(payload)
    assert(payload['name'] == 'unequaled in taste')
    

def test__get_most_requested_ingredient__when_there_are_orders(client, report_uri, create_orders):
    """
    tests errors are not produced when there are orders
    TODO: extend to test correct behavior 
    edge case: if there is a tie on the 3rd place, one of the clients should appear 
    """
    create_orders
    response = client.get(report_uri + 'mri')
    pytest.assume(response.status.startswith('200'))
    payload = response.json
    print(payload)
    assert(isinstance(payload['name'], str))


def test__get_month_with_most_revenue__when_there_are_orders(client, report_uri, create_orders):
    """
    tests errors are not produced when there are orders
    TODO: extend to test correct behavior 
    """
    create_orders
    response = client.get(report_uri + 'month')
    pytest.assume(response.status.startswith('200'))
    payload = response.json
    print(payload)
    assert(isinstance(payload, str))


def test__get_top3_customers__when_there_are_orders(client, report_uri, create_orders):
    """
    tests errors are not produced when there are orders
    TODO: extend to test correct behavior 
    """
    create_orders
    response = client.get(report_uri + 'top3')
    pytest.assume(response.status.startswith('200'))
    payload = response.json
    print(payload)
    assert(isinstance(payload, list))
