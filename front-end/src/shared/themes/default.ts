import { createTheme } from "@mui/material/styles";

const primary = "#ff0000"
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
            styleOverrides: { root: { color: "#333333" } }
        }
    },
    custom: {
        background: "#ededed"
    }
})

export default defaultTheme