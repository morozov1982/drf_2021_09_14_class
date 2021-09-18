import React from 'react'

const AuthorItem = ({author}) => {
    return (
        <tr>
            <td>{author.first_name}</td>
            <td>{author.last_name}</td>
            <td>{author.birthday_year}</td>
        </tr>
    )
}

const AuthorList = ({authors}) => {
    return (
        <table>
            <th>Имя</th>
            <th>Фамилия</th>
            <th>Год</th>

            { authors.map(
                (a) => <AuthorItem author={a} />
            ) }
        </table>
    )
}

export default AuthorList