import { React } from 'react'
import './App.css';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom'
import Home from "./pages/Home"
import About from "./pages/About"
import Checks from "./pages/Checks"

function App() {
  return (
    <Router>     
      <Switch>
        <Route path="/checks/:type/:name" component={Checks} />
        <Route path="/about" component={About} />
        <Route exact path="/" component={Home} />
      </Switch>
    </Router>
  )

}
export default App;

  // const [suites, setCheckSuites] = useState([])
  // const [checks, setChecks] = useState([])
  // const [checkTypes, setCheckTypes] = useState([])
  // const [error, setError] = useState(null)

  // useEffect(() => {
  //   // fetch("http://localhost:5000/api/check_suites")
  //   //   .then(res => res.json())
  //   //   .then(res => {
  //   //     console.log(res)
  //   //     const data = res.check_suites.map((suite) => ({name: suite, type: "suite"}))
  //   //     console.log(data)
  //   //     setCheckSuites(data)        
  //   //   },
  //   //   (error) => {
  //   //     setError(error)
  //   //   })
  //   loadData()
  // }, [])

  // const loadData = async () => {
  //   const suites = await fetch("http://localhost:5000/api/check_suites")
  //     .then(res => res.json())
  //     .then(res => {
  //       const data = res.check_suites.map((suite) => ({name: suite, type: "suite"}))
  //       setCheckSuites(data)
  //     })
  //     .catch((err) => setError(err))
  // }

  // if (error) {
  //   return <div>Error: {error.message}</div>
  // } else {
  //   return (
  //     <BrowserRouter>
  //       <div>
  //         <Header />
  //         <div className="container">
  //           <ul>
  //             {suites.map((suite) => (
  //               <li key={suite.name}>
  //                 <CheckCollection collectionName={suite.name} collectionType={suite.type} />
  //               </li>
  //             ))}
  //           </ul>
  //         </div>
  //       </div>
  //     </BrowserRouter>
  //   )
  // }