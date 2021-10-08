import React from 'react';
import {Link} from "react-router-dom";

const AuthorItem = ({author}) => {
    return (
        <tr>
            <td>{author.first_name}</td>
            <td><Link to={`author/${author.id}`}>{author.last_name}</Link></td>
            <td>{author.birthday_year}</td>
        </tr>
    )
}

const AuthorList = ({authors}) => {
    return (
        <table>
            <thead>
                <th>Имя</th>
                <th>Фамилия</th>
                <th>Год</th>
            </thead>

            <tbody>
                { authors.map(
                    (a) => <AuthorItem author={a} />
                ) }
            </tbody>
        </table>
    )
}

export default AuthorList