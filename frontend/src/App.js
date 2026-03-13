import React from "react"
import {BrowserRouter,Routes,Route} from "react-router-dom"
import "./App.css"

import Sidebar from "./components/Sidebar"
import Dashboard from "./pages/Dashboard"
import ImportRecipe from "./pages/ImportRecipe"

function App(){

return(

<BrowserRouter>

<Sidebar/>

<Routes>

<Route path="/" element={<Dashboard/>}/>
<Route path="/import" element={<ImportRecipe/>}/>

</Routes>

</BrowserRouter>

)

}

export default App