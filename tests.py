from main import BooksCollector
import pytest

class TestBooksCollector:

    def test_books_collector_init(self):
        collector = BooksCollector()
        assert collector.books_genre == {}
        assert collector.favorites == []
        assert collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        assert collector.genre_age_rating == ['Ужасы', 'Детективы']

    def test_add_new_book_valid_name(self):
        collector = BooksCollector()
        collector.add_new_book('Книга1')
        assert 'Книга1' in collector.books_genre
        assert collector.books_genre['Книга1'] == ''

    def test_add_new_book_len_name_zero(self):
        collector = BooksCollector()
        collector.add_new_book('')
        assert not collector.books_genre

    def test_add_new_book_len_name_over_forty(self):
        collector = BooksCollector()
        collector.add_new_book('qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfg')
        assert not collector.books_genre

    def test_add_new_book_name_double(self):
        collector = BooksCollector()
        collector.add_new_book('Книга1')
        collector.add_new_book('Книга1')
        assert len(collector.books_genre) == 1

    def test_set_book_genre_valid_name(self):
        collector = BooksCollector()
        collector.add_new_book('Книга1')
        collector.set_book_genre('Книга1', 'Фантастика')
        assert collector.books_genre['Книга1'] == 'Фантастика'

    def test_set_book_genre_invalid_name(self):
        collector = BooksCollector()
        collector.add_new_book('Книга1')
        collector.set_book_genre('Книга1', 'Боевик')
        assert collector.books_genre['Книга1'] == ''

    def test_get_book_genre_existent_book(self):
        collector = BooksCollector()
        collector.add_new_book('Книга1')
        collector.set_book_genre('Книга1', 'Фантастика')
        assert collector.get_book_genre('Книга1') == 'Фантастика'

    def test_get_books_with_specific_genre_multiple_books(self):
        collector = BooksCollector()
        collector.add_new_book("Книга1")
        collector.add_new_book("Книга2")
        collector.add_new_book("Книга3")
        collector.set_book_genre("Книга1", "Фантастика")
        collector.set_book_genre("Книга2", "Фантастика")
        collector.set_book_genre("Книга3", "Детективы")
        assert collector.get_books_with_specific_genre("Фантастика") == ["Книга1", "Книга2"]

    def test_get_books_genre_return_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга1')
        collector.set_book_genre('Книга1', 'Фантастика')
        assert collector.get_books_genre() == {'Книга1': 'Фантастика'}

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book("Книга1")
        collector.add_new_book("Книга2")
        collector.add_new_book("Книга3")
        collector.set_book_genre("Книга1", "Фантастика")
        collector.set_book_genre("Книга2", "Ужасы")
        collector.set_book_genre("Книга3", "Мультфильмы")
        assert collector.get_books_for_children() == ["Книга1", "Книга3"]

    def test_add_book_in_favorites_valid_book(self):
        collector = BooksCollector()
        collector.add_new_book("Книга1")
        collector.add_book_in_favorites("Книга1")
        assert "Книга1" in collector.favorites

    def test_delete_book_from_favorites_exist_book(self):
        collector = BooksCollector()
        collector.add_new_book("Книга1")
        collector.add_book_in_favorites("Книга1")
        collector.delete_book_from_favorites("Книга1")
        assert collector.favorites == []

    def test_delete_book_from_favorites_nonexistent_book(self):
        collector = BooksCollector()
        collector.delete_book_from_favorites("Книга1")
        assert collector.favorites == []

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book("Книга1")
        collector.add_new_book("Книга2")
        collector.add_book_in_favorites("Книга1")
        collector.add_book_in_favorites("Книга2")
        assert collector.get_list_of_favorites_books() == ["Книга1", "Книга2"]

