def test_dis():
    """"
    test the distance
    """
    try:
        import pytest
        from miniproject import dis
    except ImportError:
        print("It is not correct import")
        return

    data1 = [5,12]
    data2 = [3,4]
    data3 = [6,8]
    assert 13 == dis(data1)
    assert 5 == dis(data2)
    assert 10 == dis(data3)