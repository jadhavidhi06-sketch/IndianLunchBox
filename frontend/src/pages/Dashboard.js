import React, {useEffect, useState} from "react"
import {getRecipes} from "../services/api"
import RecipeCard from "../components/RecipeCard"

function Dashboard(){

const [recipes,setRecipes] = useState([])

useEffect(()=>{

getRecipes().then(res=>{
setRecipes(res.data)
})

},[])

return(

<div className="dashboard">

<h1>Welcome to IndianLunchBox 🍛</h1>

<div className="grid">

{recipes.map(recipe=>(
<RecipeCard recipe={recipe}/>
))}

</div>

</div>

)

}

export default Dashboard