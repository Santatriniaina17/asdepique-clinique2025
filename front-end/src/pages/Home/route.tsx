import { PATHS } from "../../app/routes/paths"
import Home from "./Home"

const name = "home"
const path = PATHS.home
const route = {
    path,
    element: <Home/>
}

export { name, path, route }