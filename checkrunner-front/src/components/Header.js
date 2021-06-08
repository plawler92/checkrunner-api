import React from 'react'
import { Link } from 'react-router-dom'


const Header = () => {
    return (
        <header>
            <ul>
                <li>
                    <Link to="/">Home</Link>
                </li>
                <li>
                    <Link to="/about">About</Link>
                </li>
                <li>
                    <Link to="/checks/suite/maintenance">Checks</Link>
                </li>
                {/* <li>
                    <Link to="/suites/">Test</Link>
                </li> */}
            </ul>
        </header>
    )
}

export default Header
