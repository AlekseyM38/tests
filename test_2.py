import code_for_test_2


def test_top_mentors():
    expected_result = "Александр: 10 раз(а), Евгений: 5 раз(а), Максим: 4 раз(а)"
    result = code_for_test_2.top_3_mentors()
    assert result == expected_result
