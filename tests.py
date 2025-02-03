from main import BooksCollector
import pytest


class TestBooksCollector:

    @pytest.mark.parametrize('book_name',['Самое большое название книги, которое было',''])
    def test_add_new_book_add_invalid_len_name(self,book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert collector.get_books_genre().get(book_name,False)==False

    @pytest.mark.parametrize('book_name',['A','Гарри Поттер','Название,которое состоит из 39 символов'])
    def test_add_new_book(self,book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert len(collector.get_books_genre())==1

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Му-му')
        collector.add_new_book('Город N')
        assert len(collector.get_books_genre())==2

    def test_set_book_genre(self):
        collector = BooksCollector()
        book_name='Гарри Потер'
        genre_name='Фантастика'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name,genre_name)
        assert collector.get_book_genre(book_name)==genre_name

    def test_set_book_genre_set_invalid_genre(self):
        collector = BooksCollector()
        book_name='В бой идут одни старики'
        genre_name='Военные'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name,genre_name)
        assert len(collector.get_book_genre(book_name))==0

    def test_get_book_genre(self):
        collector = BooksCollector()
        book_name = 'Десять негретят'
        genre_name = 'Детективы'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name,genre_name)
        assert collector.get_book_genre(book_name)==genre_name

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Антошка')
        collector.set_book_genre('Антошка','Мультфильмы')
        collector.add_new_book('Колобок')
        collector.set_book_genre('Колобок', 'Мультфильмы')
        assert len(collector.get_books_with_specific_genre('Мультфильмы'))==2

    @pytest.mark.parametrize('book_name',['Гарри Поттер часть 1','Гарри Поттер часть 2','Гарри Поттер часть 3'])
    def test_get_books_genre(self,book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name,'Фантастика')
        assert collector.get_books_genre().get(book_name)==collector.books_genre.get(book_name)

    @pytest.mark.parametrize('book_name,genre_name',[
        ['Остров сокровищ','Мультфильмы'],
        ['Полицеский с рублевки','Комедии']
    ])
    def test_get_books_for_children(self,book_name,genre_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name,genre_name)
        assert len(collector.get_books_for_children())==1

    @pytest.mark.parametrize('book_name,genre_name',[
        ['Пила','Ужасы'],
        ['Дарья Донцова','Детективы']
    ])
    def test_get_books_for_children_neg(self,book_name,genre_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name,genre_name)
        assert len(collector.get_books_for_children())==0

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        book_name = 'Приключение незнайки'
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        assert ''.join(collector.get_list_of_favorites_books())==book_name

    def test_add_book_in_favorites_add_two_equal_books(self):
        collector = BooksCollector()
        book_name = 'Волшебник изумрудного города'
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.add_book_in_favorites(book_name)
        assert len(collector.get_list_of_favorites_books())==1

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        book_name = 'Волшебник изумрудного города 2'
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.delete_book_from_favorites(book_name)
        assert len(collector.get_list_of_favorites_books())==0

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        book_name = 'Волшебник изумрудного города 3'
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        check_get_list_of_favorites_books = len(collector.get_list_of_favorites_books())
        assert check_get_list_of_favorites_books==1

