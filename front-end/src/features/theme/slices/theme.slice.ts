import { createSlice, type PayloadAction } from '@reduxjs/toolkit';
import type { Theme } from '@mui/material/styles';
import defaultTheme from "../../../shared/themes/default";

const THEME_KEY = "theme"

const initialState: Theme = JSON.parse(localStorage.getItem(THEME_KEY) ?? JSON.stringify(defaultTheme))

const themeSlice = createSlice({
    name: 'theme',
    initialState,
    reducers: {
        setTheme: (_, action: PayloadAction<Theme>) => {
            localStorage.setItem(THEME_KEY, JSON.stringify(action.payload))
            return action.payload
        },
    },
})

export const { setTheme } = themeSlice.actions
export default themeSlice.reducer
