import { useMemo } from "react"
import { ThemeProvider as MuiThemeProvider, createTheme } from "@mui/material/styles"
import { useAppSelector } from "../../../app/store/hooks"
import type { ThemeProviderType } from "../types"

const ThemeProvider: ThemeProviderType = ({ children }) => {
    const currentTheme = useAppSelector(stat => stat.theme)

    const muiTheme = useMemo(() => {
        return createTheme(currentTheme)
    }, [currentTheme])

    return (
        <MuiThemeProvider theme={muiTheme}>
            {children}
        </MuiThemeProvider>
    )
}

export { ThemeProvider }
