import React from 'react'
import { useParams } from 'react-router'
import Layout from '../components/Layout'

const Checks = () => {
    let { type, name } = useParams()
    console.log(type)
    console.log(name)
    return (
        <Layout>
            <div>
                <h1>Checks Page</h1>
                <h2>{type}</h2>
                <h3>{name}</h3>
            </div>
        </Layout>
    )
}

export default Checks