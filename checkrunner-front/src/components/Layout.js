import React from 'react'
import Header from './Header'

export const Layout = ({title, children}) => {
    return (
        <div>
            <Header />
            <main>
                {children}
            </main>
            {/* <Footer /> */}
        </div>
    )
}

export default Layout;