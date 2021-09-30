import React from 'react';
import { useParams } from "react-router-dom";

const BookItem = ({book}) => {
    return (
        <tr>
            <td>{book.id}</td>
            <td>{book.title}</td>
            <td>{book.authors}</td>
        </tr>
    )
}

const AuthorBookList = ({books}) => {
    let { id } = useParams();

    let filtered_books = books.filter((book) => book.authors.includes(parseInt(id)))

    return (
        <table>
            <th>id</th>
            <th>Название</th>
            <th>Автор</th>

            { filtered_books.map(
                (b) => <BookItem book={b} />
            ) }
        </table>
    )
}

export default AuthorBookList