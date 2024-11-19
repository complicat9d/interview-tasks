from unittest import mock
from unittest.mock import MagicMock
from task2.main import get_next_page, write_to_file


def test_get_next_page_with_next_page():
    mock_page = MagicMock()
    mock_a_tag = MagicMock()
    mock_a_tag.text = "Следующая страница"
    mock_a_tag.__getitem__.return_value = "/page2"

    mock_page.find_all.return_value = [mock_a_tag]

    result = get_next_page(mock_page)

    assert result == "/page2", "Next page URL was not extracted correctly."


@mock.patch("builtins.open", new_callable=mock.mock_open)
def test_write_to_file(mock_open):
    mock_dict = {"A": 5, "B": 3}

    write_to_file(mock_dict)

    mock_open.assert_called_with("beasts.csv", mode="w")

    mock_file = mock_open()

    mock_file.write.assert_any_call("A,5\r\n")
    mock_file.write.assert_any_call("B,3\r\n")
