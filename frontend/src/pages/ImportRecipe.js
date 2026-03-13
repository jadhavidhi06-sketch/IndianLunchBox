import React, {useState} from "react"
import {importRecipes} from "../services/api"

function ImportRecipe(){

const [file,setFile] = useState()

const upload = () => {

const formData = new FormData()

formData.append("file",file)

importRecipes(formData)

}

return(

<div>

<h2>Import Recipes</h2>

<input type="file" onChange={(e)=>setFile(e.target.files[0])} />

<button onClick={upload}>Upload</button>

</div>

)

}

export default ImportRecipe