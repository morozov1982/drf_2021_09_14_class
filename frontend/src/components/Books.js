import React from 'react'

const BookItem = ({book}) => {
    return (
        <tr>
            <td>{book.id}</td>
            <td>{book.title}</td>
            <td>{book.authors}</td>
        </tr>
    )
}

const BookList = ({books}) => {
    return (
        <table>
            <thead>
                <th>id</th>
                <th>Название</th>
                <th>Автор</th>
            </thead>

            <tbody>
                { books.map(
                    (b) => <BookItem book={b} />
                ) }
            </tbody>
        </table>
    )
}

export default BookList