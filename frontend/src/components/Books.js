import React from 'react'

const BookItem = ({book, deleteBook}) => {
    return (
        <tr>
            <td>{book.id}</td>
            <td>{book.title}</td>
            <td>{book.authors}</td>
            <td><button type='button' onClick={()=>deleteBook(book.id)}>Delete</button></td>
        </tr>
    )
}

const BookList = ({books, deleteBook}) => {
    return (
        <table>
            <thead>
                <th>id</th>
                <th>Название</th>
                <th>Автор</th>
                <th></th>
            </thead>

            <tbody>
                { books.map(
                    (b) => <BookItem book={b} deleteBook={deleteBook} />
                ) }
            </tbody>
        </table>
    )
}

export default BookList