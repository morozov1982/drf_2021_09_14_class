import React from 'react';
import axios from 'axios';
import {HashRouter, Route, Link, Switch, Redirect, BrowserRouter} from "react-router-dom";
import AuthorList from './components/Authors';
import BookList from "./components/Books";
import AuthorBookList from "./components/AuthorBooks";

const NotFound = ({location}) => {
    return (<div>Страница с адресом: {location.pathname} не найдена!</div>)
}

class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'authors': [],
            'books': [],
        }
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/authors/')
            .then(response => {
                const authors = response.data
                this.setState({
                    'authors': authors
                })
            })
            .catch(error => console.log(error))
        axios.get('http://127.0.0.1:8000/api/books/')
            .then(response => {
                const books = response.data
                this.setState({
                    'books': books
                })
            })
            .catch(error => console.log(error))
    }

    render() {
        return (
            <div>
                <BrowserRouter>
                    <nav>
                        <ul>
                            <li><Link to='/'>Авторы</Link></li>
                            <li><Link to='/books'>Книги</Link></li>
                        </ul>
                    </nav>

                    <Switch>
                        <Route exact path='/' component={() => <AuthorList authors={this.state.authors}/>} />
                        <Route exact path='/books' component={() => <BookList books={this.state.books}/>} />
                        <Route path='/author/:id' component={() => <AuthorBookList books={this.state.books}/>} />
                        <Redirect from='/authors' to='/' />
                        <Route component={NotFound} />
                    </Switch>
                </BrowserRouter>
            </div>
        )
    }
}

export default App;
