import React from "react"

function RecipeCard({recipe}) {

return(

<div className="card">

<img src={recipe.image} alt="" />

<h3>{recipe.title}</h3>

<p>{recipe.category}</p>

</div>

)

}

export default RecipeCard