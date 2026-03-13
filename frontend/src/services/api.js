import axios from "axios"

const API = axios.create({
    baseURL: "http://127.0.0.1:8000/api/"
})

export const getRecipes = () => API.get("recipes/")
export const downloadRecipes = () => API.get("download/")
export const importRecipes = (data) => API.post("import/", data)

export default API