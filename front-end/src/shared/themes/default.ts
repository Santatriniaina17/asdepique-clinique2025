import { createTheme } from "@mui/material/styles";

const primary = "#0d5f19"
const secondary = "#0000ff"
const defaultTheme = createTheme({
    palette: {
        mode: "light",
        primary: {
            main: primary,
        },
        secondary: {
            main: secondary,
        },
    },
    components: {
        MuiTypography: {
            styleOverrides: { root: { color: "#242424" } }
        }
    },
    custom: {
        background: "#ededed",
        header: "#242424"
    }
})

export default defaultTheme