import {React, useState, useEffect} from 'react'
import Layout from '../components/Layout'

const Home = () => {
    const [suites, setCheckSuites] = useState([])
    
    const loadData = async () => {
        const suites = await fetch("http://localhost:5000/api/check_suites")
            .then(res => res.json())
            .then(res => {
                return res.check_suites.map((suite) => ({name: suite, type: "suite"}))
            })
        setCheckSuites(suites)
    }

    useEffect(() => {
        loadData()
    }, [])


    return (
        <Layout title="Home">
            <h1>This is the main page.</h1>
            <ul>
                {suites.map((suite) => (
                    <li key={suite.name}>
                        {suite.name}
                    </li>
                ))}
            </ul>
        </Layout>
    )
}

export default Home
